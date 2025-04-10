import datetime
import pandas as pd

useYahooFinance = True
useYahooFinanceBigFile = False

START_DATE = "1994-01-03"
# END_DATE = datetime.datetime.today().strftime('%Y-%m-%d')
END_DATE = "2025-03-31"

# crate da dataframe to aggregate the data with length of START_DATE to END_DATE
base_df = pd.DataFrame(index=pd.date_range(start=START_DATE, end=END_DATE, freq='D'))
# convert the index to the format "%Y-%m-%d"
base_df.index = base_df.index.strftime("%Y-%m-%d")

if useYahooFinance:
    if useYahooFinanceBigFile:
        # Read the data from Yahoo Finance
        YFdata = pd.read_csv("0 - asDownloaded/YahooFinance/_All Yahoo Finance Indicators Big File_.csv", index_col=0)
        # add the data to the base_df dataframe
        base_df = pd.concat([base_df, YFdata], axis=1)
    else:
        IBOV_df = pd.read_csv("0 - asDownloaded/YahooFinance/0-IBOVESPA.csv", index_col=0)
        IBOV_df.columns = [f"IBOVESPA - {col}" for col in IBOV_df.columns]
        base_df = pd.concat([base_df, IBOV_df], axis=1)

        Dolar_df = pd.read_csv("0 - asDownloaded/YahooFinance/1-Dólar Câmbio.csv", index_col=0)
        Dolar_df.columns = [f"Dólar - {col}" for col in Dolar_df.columns]
        base_df = pd.concat([base_df, Dolar_df], axis=1)

        Dow_df = pd.read_csv("0 - asDownloaded/YahooFinance/2-Dow Jones.csv", index_col=0)
        Dow_df.columns = [f"Dow Jones - {col}" for col in Dow_df.columns]
        base_df = pd.concat([base_df, Dow_df], axis=1)

        SP500_df = pd.read_csv("0 - asDownloaded/YahooFinance/3-S&P 500.csv", index_col=0)
        SP500_df.columns = [f"S&P 500 - {col}" for col in SP500_df.columns]
        base_df = pd.concat([base_df, SP500_df], axis=1)

        Nasdaq_df = pd.read_csv("0 - asDownloaded/YahooFinance/4-Nasdaq.csv", index_col=0)
        Nasdaq_df.columns = [f"Nasdaq - {col}" for col in Nasdaq_df.columns]
        base_df = pd.concat([base_df, Nasdaq_df], axis=1)

        Shanghai_df = pd.read_csv("0 - asDownloaded/YahooFinance/5-Shanghai SE.csv", index_col=0)
        Shanghai_df.columns = [f"Shanghai SE - {col}" for col in Shanghai_df.columns]
        base_df = pd.concat([base_df, Shanghai_df], axis=1)

        Nikkei_df = pd.read_csv("0 - asDownloaded/YahooFinance/6-Nikkei.csv", index_col=0)
        Nikkei_df.columns = [f"Nikkei - {col}" for col in Nikkei_df.columns]
        base_df = pd.concat([base_df, Nikkei_df], axis=1)

        HanSeng_df = pd.read_csv("0 - asDownloaded/YahooFinance/7-HanSeng Index.csv", index_col=0)
        HanSeng_df.columns = [f"HanSeng Index - {col}" for col in HanSeng_df.columns]
        base_df = pd.concat([base_df, HanSeng_df], axis=1)

        Kospi_df = pd.read_csv("0 - asDownloaded/YahooFinance/8-Kospi.csv", index_col=0)
        Kospi_df.columns = [f"Kospi - {col}" for col in Kospi_df.columns]
        base_df = pd.concat([base_df, Kospi_df], axis=1)

        ASX_df = pd.read_csv("0 - asDownloaded/YahooFinance/9-ASX 200.csv", index_col=0)
        ASX_df.columns = [f"ASX 200 - {col}" for col in ASX_df.columns]
        base_df = pd.concat([base_df, ASX_df], axis=1)

        FTSE_df = pd.read_csv("0 - asDownloaded/YahooFinance/10-FTSE 100.csv", index_col=0)
        FTSE_df.columns = [f"FTSE 100 - {col}" for col in FTSE_df.columns]
        base_df = pd.concat([base_df, FTSE_df], axis=1)

        DAX_df = pd.read_csv("0 - asDownloaded/YahooFinance/11-DAX.csv", index_col=0)
        DAX_df.columns = [f"DAX - {col}" for col in DAX_df.columns]
        base_df = pd.concat([base_df, DAX_df], axis=1)

        CAC_df = pd.read_csv("0 - asDownloaded/YahooFinance/12-CAC 40.csv", index_col=0)
        CAC_df.columns = [f"CAC 40 - {col}" for col in CAC_df.columns]
        base_df = pd.concat([base_df, CAC_df], axis=1)

        FTSE_MIB_df = pd.read_csv("0 - asDownloaded/YahooFinance/13-FTSE MIB.csv", index_col=0)
        FTSE_MIB_df.columns = [f"FTSE MIB - {col}" for col in FTSE_MIB_df.columns]
        base_df = pd.concat([base_df, FTSE_MIB_df], axis=1)

        STOXX_df = pd.read_csv("0 - asDownloaded/YahooFinance/14-STOXX 600.csv", index_col=0)
        STOXX_df.columns = [f"STOXX 600 - {col}" for col in STOXX_df.columns]
        base_df = pd.concat([base_df, STOXX_df], axis=1)

        WTI_df = pd.read_csv("0 - asDownloaded/YahooFinance/15-Petróleo WTI.csv", index_col=0)
        WTI_df.columns = [f"Petróleo WTI - {col}" for col in WTI_df.columns]
        base_df = pd.concat([base_df, WTI_df], axis=1)

        Brent_df = pd.read_csv("0 - asDownloaded/YahooFinance/16-Petróleo Brent.csv", index_col=0)
        Brent_df.columns = [f"Petróleo Brent - {col}" for col in Brent_df.columns]
        base_df = pd.concat([base_df, Brent_df], axis=1)

        Minério_df = pd.read_csv("0 - asDownloaded/YahooFinance/17-Minério de Ferro.csv", index_col=0)
        Minério_df.columns = [f"Minério de Ferro - {col}" for col in Minério_df.columns]
        base_df = pd.concat([base_df, Minério_df], axis=1)

        Bitcoin_df = pd.read_csv("0 - asDownloaded/YahooFinance/18-Bitcoin.csv", index_col=0)
        Bitcoin_df.columns = [f"Bitcoin - {col}" for col in Bitcoin_df.columns]
        base_df = pd.concat([base_df, Bitcoin_df], axis=1)

# create a dictionary with the month names and their corresponding numbers
month_names = {
    "janeiro": 1,
    "fevereiro": 2,
    "março": 3,
    "abril": 4,
    "maio": 5,
    "junho": 6,
    "julho": 7,
    "agosto": 8,
    "setembro": 9,
    "outubro": 10,
    "novembro": 11,
    "dezembro": 12
}

quarters = {
    "1º": 1,
    "2º": 4,
    "3º": 7,
    "4º": 10
}

# function to put all days from a list of dates in business days
def put_all_days_in_business_days(dates):
    # create a list of business days
    business_days = []
    # iterate over the dates
    for date in dates:
        year, month, day = (int(i) for i in date.split("-"))
        # convert the date to datetime format
        dateTime = datetime.datetime(year, month, day)
        # find weekday of the date
        weekday = dateTime.weekday()
        # if date is a weekend, add the next business day
        if weekday == 5:
            dateTime += datetime.timedelta(days=2)
        elif weekday == 6:
            dateTime += datetime.timedelta(days=1)
        # add the date to the list
        business_days.append(dateTime.strftime("%Y-%m-%d"))
    return business_days

# # load PIB data
PIB_df = None
# load the data as a normal text file and convert it to a dataframe
with open("0 - asDownloaded/IBGE/PIB.csv", "r") as f:
    # ignore the first line
    f.readline()
    # read the dates strigs on the second line
    dates = f.readline().strip().split(";")[1:]
    # convert the dates to year-month-day format
    dates = [f"{date.split()[2]}-{quarters[date.split()[0].lower()]}-10" for date in dates]
    # put all days in business days
    dates = put_all_days_in_business_days(dates)
    # transform the dates to datetime format
    dates = [datetime.datetime.strptime(date, "%Y-%m-%d") for date in dates]
    # advance the dates by 5 months
    dates = [date + datetime.timedelta(days=30*5) for date in dates]
    # read the data on the third line
    data = f.readline().strip().split(";")[1:]
    # convert the data to float
    data = [float(i) for i in data]
    # create a dataframe with the data
    PIB_df = pd.DataFrame(data, index=dates, columns=["PIB"])
    # convert the index to the format "%Y-%m-%d"
    PIB_df.index = PIB_df.index.strftime("%Y-%m-%d")
    # print the dataframe
    # print(PIB_df.tail(10))

# load IPCA data
IPCA_df = None
# load the data as a normal text file and convert it to a dataframe
with open("0 - asDownloaded/IBGE/IPCA.csv", "r") as f:
    # ignore the first line
    f.readline()
    # read the dates strigs on the second line
    dates = f.readline().strip().split(";")[1:]
    # convert the dates to year-month-day format
    dates = [f"{date.split()[1]}-{month_names[date.split()[0].lower()]}-10" for date in dates]
    # put all days in business days
    dates = put_all_days_in_business_days(dates)
    # read the data on the third line
    data = f.readline().strip().split(";")[1:]
    # convert the data to float
    data = [float(i) for i in data]
    # create a dataframe with the data
    IPCA_df = pd.DataFrame(data, index=dates, columns=["IPCA"])
    # convert the index to datetime format
    IPCA_df.index = pd.to_datetime(IPCA_df.index)
    # convert the index to the format "%Y-%m-%d"
    # IPCA_df.index = IPCA_df.index.strftime("%Y-%m-%d")
    # print the dataframe
    # print(IPCA_df.tail(10))

# # load INPC data
INPC_df = None
# load the data as a normal text file and convert it to a dataframe
with open("0 - asDownloaded/IBGE/INPC.csv", "r") as f:
    # ignore the first line
    f.readline()
    # read the dates strigs on the second line
    dates = f.readline().strip().split(";")[1:]
    # convert the dates to year-month-day format
    dates = [f"{date.split()[1]}-{month_names[date.split()[0].lower()]}-10" for date in dates]
    # put all days in business days
    dates = put_all_days_in_business_days(dates)
    # read the data on the third line
    data = f.readline().strip().split(";")[1:]
    # convert the data to float
    data = [float(i) for i in data]
    # create a dataframe with the data
    INPC_df = pd.DataFrame(data, index=dates, columns=["INPC"])
    # convert the index to datetime format
    INPC_df.index = pd.to_datetime(INPC_df.index)
    # convert the index to the format "%Y-%m-%d"
    INPC_df.index = INPC_df.index.strftime("%Y-%m-%d")
    # print the dataframe
    # print(INPC_df.tail(10))

# # load SELIC data
SELIC_df = pd.read_csv("0 - asDownloaded/Bacen/Selic.csv", sep=";", index_col=0)
# rename the columns
SELIC_df.columns = ["Meta Selic", "Taxa acumulada no período"]
# convert the index to datetime format
SELIC_df.index = pd.to_datetime(SELIC_df.index, format="%d-%m-%Y")
# convert the index to the format "%Y-%m-%d"
SELIC_df.index = SELIC_df.index.strftime("%Y-%m-%d")
# print the dataframe
# print(SELIC_df.tail(10))

# Reindex individual DataFrames to match base_df
PIB_df = PIB_df.reindex(base_df.index)
IPCA_df = IPCA_df.reindex(base_df.index)
INPC_df = INPC_df.reindex(base_df.index)
SELIC_df = SELIC_df.reindex(base_df.index)

# add the dataframes to the base_df dataframe
base_df = pd.concat([base_df, PIB_df], axis=1)
base_df = pd.concat([base_df, IPCA_df], axis=1)
base_df = pd.concat([base_df, INPC_df], axis=1)
base_df = pd.concat([base_df, SELIC_df], axis=1)
# print the data on the last 3 months of 2024 (they are not in the end or start of the data)
# start on index 2024-10-01 and end on index 2025-01-01
# print(base_df.loc["2024-10-01":"2024-10-11"])
# print(base_df.loc["2024-10-11":"2024-10-21"])
# print(base_df.loc["2024-10-21":"2024-11-01"])
# print(base_df.loc["2024-11-01":"2024-11-11"])
# print(base_df.loc["2024-11-11":"2024-11-21"])
# print(base_df.loc["2024-11-21":"2024-12-01"])
# print(base_df.loc["2024-12-01":"2024-12-11"])
# print(base_df.loc["2024-12-11":"2024-12-21"])
# print(base_df.loc["2024-12-21":"2024-01-01"])

# save the dataframe to a csv file
base_df.to_csv("1 - aggregated/All indicators aggregated (D).csv", index=True)

# # crate da dataframe to aggregate the data with length of START_DATE to END_DATE
# base_B_df = pd.DataFrame(index=pd.date_range(start=START_DATE, end=END_DATE, freq='B'))
# # convert the index to the format "%Y-%m-%d"
# base_B_df.index = base_B_df.index.strftime("%Y-%m-%d")
# # add the dataframes to the base_B_df dataframe
# base_B_df = pd.concat([base_B_df, base_df], axis=1)
# base_B_df = base_df[base_df.index.isin(pd.date_range(start=START_DATE, end=END_DATE, freq='B').strftime("%Y-%m-%d"))]
base_B_df = base_df.reindex(pd.date_range(start=START_DATE, end=END_DATE, freq='B').strftime("%Y-%m-%d"))

print(base_df)
print(base_B_df)
# save the dataframe to a csv file
base_B_df.to_csv("1 - aggregated/All indicators aggregated (B).csv", index=True)

# find all indexes with missing values on columns
# [IBOVESPA - Open, IBOVESPA - Close, IBOVESPA - High, IBOVESPA - Low]
# [Dólar - Open, Dólar - Close, Dólar - High, Dólar - Low]
# when both are missing the day probably is a holiday
holidays = []
columns = ["IBOVESPA - Open", "IBOVESPA - Close", "IBOVESPA - High", "IBOVESPA - Low",
           "Dólar - Open", "Dólar - Close", "Dólar - High", "Dólar - Low"]
for index in base_B_df.index:
    hasValues = False
    for column in columns:
        # check if the index has values on the columns
        if not pd.isna(base_B_df.loc[index, column]):
            hasValues = True
            break
    if not hasValues:
        # add the index to the list
        holidays.append(index)
# print the missing indexes
# print("Missing indexes:", holidays)

# create a new dataframe without the holidays
holidays_df = base_B_df.drop(holidays)
print(holidays_df)
# save the dataframe to a csv file
holidays_df.to_csv("1 - aggregated/All indicators aggregated (B - Holidays).csv", index=True)

# fill the missing values with the last value
base_df = base_df.ffill()
base_B_df = base_B_df.ffill()
holidays_df = holidays_df.ffill()

# find and save all first and last valid indexes of the indicators
first_valid_indexes_df = base_df.apply(pd.Series.first_valid_index)
first_valid_indexes_df.columns = ['First Valid Index']
last_valid_indexes_df = base_df.apply(pd.Series.last_valid_index)
last_valid_indexes_df.columns = ['Last Valid Index']
valid_indexes_df = pd.concat([first_valid_indexes_df, last_valid_indexes_df], axis=1)
valid_indexes_df.columns = ['First Valid Index', 'Last Valid Index']
valid_indexes_df.to_csv("1 - aggregated/valid_indexes_D.csv", index=True)

# find and save all first and last valid indexes of the indicators
first_valid_indexes_df = base_B_df.apply(pd.Series.first_valid_index)
first_valid_indexes_df.columns = ['First Valid Index']
last_valid_indexes_df = base_B_df.apply(pd.Series.last_valid_index)
last_valid_indexes_df.columns = ['Last Valid Index']
valid_indexes_df = pd.concat([first_valid_indexes_df, last_valid_indexes_df], axis=1)
valid_indexes_df.columns = ['First Valid Index', 'Last Valid Index']
valid_indexes_df.to_csv("1 - aggregated/valid_indexes_B.csv", index=True)

# find and save all first and last valid indexes of the indicators
first_valid_indexes_df = holidays_df.apply(pd.Series.first_valid_index)
first_valid_indexes_df.columns = ['First Valid Index']
last_valid_indexes_df = holidays_df.apply(pd.Series.last_valid_index)
last_valid_indexes_df.columns = ['Last Valid Index']
valid_indexes_df = pd.concat([first_valid_indexes_df, last_valid_indexes_df], axis=1)
valid_indexes_df.columns = ['First Valid Index', 'Last Valid Index']
valid_indexes_df.to_csv("1 - aggregated/valid_indexes_B_Holidays.csv", index=True)

# base_df = base_df.fillna(0)
# base_B_df = base_B_df.fillna(0)
# holidays_df = holidays_df.fillna(0)

# Clean data: Convert all columns to numeric where applicable
for col in base_df.columns:
    if base_df[col].dtype == 'object':
        base_df[col] = pd.to_numeric(base_df[col], errors='coerce')

# Clean data: Convert all columns to numeric where applicable
for col in base_B_df.columns:
    if base_B_df[col].dtype == 'object':
        base_B_df[col] = pd.to_numeric(base_B_df[col], errors='coerce')

# Clean data: Convert all columns to numeric where applicable
for col in holidays_df.columns:
    if holidays_df[col].dtype == 'object':
        holidays_df[col] = pd.to_numeric(holidays_df[col], errors='coerce')

# Fill or handle NaN values
# base_df.fillna(None, inplace=True)

# # Check for outliers and clip extreme values
# for col in base_df.columns:
#     if base_df[col].dtype in ['float64', 'int64']:
#         q1 = base_df[col].quantile(0.25)
#         q3 = base_df[col].quantile(0.75)
#         iqr = q3 - q1
#         lower_bound = q1 - 1.5 * iqr
#         upper_bound = q3 + 1.5 * iqr
#         base_df[col] = base_df[col].clip(lower=lower_bound, upper=upper_bound)

# Save the cleaned DataFrame
# base_df.to_csv("1 - aggregated/All indicators aggregated and cleaned.csv", index=True)

# Save the cleaned DataFrame
base_df.to_csv("1 - aggregated/All indicators aggregated and filled (D).csv", index=True)
base_B_df.to_csv("1 - aggregated/All indicators aggregated and filled (B).csv", index=True)
holidays_df.to_csv("1 - aggregated/All indicators aggregated and filled (B - Holidays).csv", index=True)