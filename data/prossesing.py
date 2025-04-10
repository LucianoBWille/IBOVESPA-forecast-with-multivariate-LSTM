import pandas as pd
import numpy as np

# configuratio
FILE = "1 - aggregated/All indicators aggregated and filled (B - Holidays).csv"
REMOVE_VOLUME = True

# Load the data with error handling
try:
    crude_Indicators_df = pd.read_csv(
        FILE, 
        index_col=0, 
        low_memory=False  # Prevents dtype inference issues
    )
except Exception as e:
    print(f"Error loading CSV: {e}")
    exit()

# Debugging: Check for inconsistent data types
# print("Column Data Types:")
# print(crude_Indicators_df.dtypes)

# Cleaning: Convert problematic columns to numeric, coercing errors
for col in crude_Indicators_df.columns:
    if crude_Indicators_df[col].dtype == 'object':
        crude_Indicators_df[col] = pd.to_numeric(crude_Indicators_df[col], errors='coerce')

# Debugging: Check for NaN values introduced by coercion
# print("Columns with NaN values after coercion:")
# print(crude_Indicators_df.isna().sum())

# Drop columns with all NaN values
crude_Indicators_df.dropna(axis=1, how='all', inplace=True)
# Drop rows with all NaN values
crude_Indicators_df.dropna(axis=0, how='all', inplace=True)

# Fill or drop NaN values as needed
crude_Indicators_df.ffill()

# remove volume column if it exists
if REMOVE_VOLUME:
    crude_Indicators_df = crude_Indicators_df.loc[:, ~crude_Indicators_df.columns.str.contains('Volume', case=False)]

print("Crude:")
print(crude_Indicators_df.head())


# Calculate spread (High - Low)
indicator_with_spread_df = crude_Indicators_df.copy()

# Filtrar colunas que contêm "High" e "Low"
high_columns = [col for col in indicator_with_spread_df.columns if "High" in col]
low_columns = [col for col in indicator_with_spread_df.columns if "Low" in col]

# Garantir que as colunas "High" e "Low" correspondem ao mesmo indicador
# Isso assume que as colunas "High" e "Low" têm o mesmo sufixo após " - "
for high_col, low_col in zip(sorted(high_columns), sorted(low_columns)):
    # Extrair o nome do indicador (sufixo após " - ")
    indicator_name = high_col.split(" - ")[0]
    indicator_name_L = low_col.split(" - ")[0]

    # Verificar se os nomes dos indicadores correspondem
    if indicator_name != indicator_name_L:
        raise ValueError(f"Mismatch between high and low columns for indicator: {indicator_name} and {indicator_name_L}")
    
    # Calcular o spread e adicionar ao DataFrame
    indicator_with_spread_df[f"{indicator_name} - Spread"] = indicator_with_spread_df[high_col] - indicator_with_spread_df[low_col]

# remover infinite values
indicator_with_spread_df = indicator_with_spread_df.replace([np.inf, -np.inf], np.nan)

# Fill NaN values with forward fill
indicator_with_spread_df = indicator_with_spread_df.ffill()

# Save the DataFrame with spread to a new CSV file
indicator_with_spread_df.to_csv("2 - processed/Indicators_with_spread.csv", index=True)

print("With Spread: ")
print(indicator_with_spread_df.head())



# Calculate percentual variation
variation_df = pd.DataFrame(index=indicator_with_spread_df.index)

for col in indicator_with_spread_df.columns:
    # Calculate percentual change starting from the first valid index
    first_valid_index = indicator_with_spread_df[col].first_valid_index()
    if first_valid_index is not None:
        # Slice the column from the first valid index and calculate pct_change
        pct_change_series = indicator_with_spread_df[col].loc[first_valid_index:].pct_change()
        
        # Rename the column to include the percentage symbol
        pct_change_series = pct_change_series.rename(col + " %")
        
        # Concatenate the renamed Series to the DataFrame
        variation_df = pd.concat([variation_df, pct_change_series], axis=1)

# remove invalid values (inf, NaN) from the percentual variation
variation_df = variation_df.replace([np.inf, -np.inf], np.nan)

# Coerce to numeric
variation_df = variation_df.apply(pd.to_numeric, errors='coerce')

# Fill NaN values with forward fill
variation_df = variation_df.ffill()

# Save the percentual variation to a new CSV file
variation_df.to_csv("2 - processed/percentual_variation.csv", index=True)

print("Percentual Variation: ")
print(variation_df.head())



# add the percentual variation to the normalized data
all_data = pd.concat([indicator_with_spread_df, variation_df], axis=1)

# Save the DataFrame with percentual variation to a new CSV file
all_data.to_csv("2 - processed/Indicators_with_spread_and_variation.csv", index=True)

print("All Data: ")
print(all_data.head())



# find and save all first and last valid indexes of the indicators
first_valid_indexes_df = all_data.apply(pd.Series.first_valid_index)
first_valid_indexes_df.columns = ['First Valid Index']
last_valid_indexes_df = all_data.apply(pd.Series.last_valid_index)
last_valid_indexes_df.columns = ['Last Valid Index']
valid_indexes_df = pd.concat([first_valid_indexes_df, last_valid_indexes_df], axis=1)
valid_indexes_df.columns = ['First Valid Index', 'Last Valid Index']
valid_indexes_df.to_csv("2 - processed/valid_indexes.csv", index=True)

print("Valid Indexes: ")
print(valid_indexes_df.head())



# remove invalid values (inf, NaN) from the percentual variation
all_data = all_data.replace([np.inf, -np.inf], np.nan)
# Coerce to numeric
all_data = all_data.apply(pd.to_numeric, errors='coerce')
# Fill NaN values with forward fill
all_data = all_data.ffill()

print("All Data after removing invalid values: ")
print(all_data.head())



# Normalize the data
normalization_values = all_data.describe().T[['min', 'max']]
# Save normalization values
normalization_values.to_csv("2 - processed/normalization_values.csv", index=True)

print("Normalization Values: ")
print(normalization_values.head())



# Normalize the data using min-max normalization
normalized_df = (all_data - normalization_values['min']) / (normalization_values['max'] - normalization_values['min'])

# Remove invalid values (inf, NaN) from the normalized data
normalized_df = normalized_df.replace([np.inf, -np.inf], np.nan)
# Coerce to numeric
normalized_df = normalized_df.apply(pd.to_numeric, errors='coerce')
# Fill NaN values with forward fill
normalized_df = normalized_df.ffill()
# fill all remaining NaN values with 0
normalized_df = normalized_df.fillna(0)

# Save normalized data
normalized_df.to_csv("2 - processed/normalized_data.csv", index=True)

print("Normalized Data: ")
print(normalized_df.head())