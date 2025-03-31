import datetime
import pandas as pd
import yfinance as yf

symbols = [
    ["^BVSP",       "IBOVESPA"],
    ["BRL=X",       "Dólar Câmbio"],
    ["^DJI",        "Dow Jones"],
    ["^GSPC",       "S&P500"],
    ["^IXIC",       "Nasdaq"],
    ["000001.SS",   "Shanghai SE"],
    ["^N225",       "Nikkei"],
    ["^HSI",        "HanSeng Index"],
    ["^KS11",       "Kospi"],
    ["^AXJO",       "ASX 200"],
    ["^FTSE",       "FTSE 100"],
    ["^GDAXI",      "DAX"],
    ["^FCHI",       "CAC 40"],
    ["FTSEMIB.MI",  "FTSE MIB"],
    ["^STOXX",      "STOXX 600"],
    ["CL=F",        "Petróleo WTI"],
    ["BZ=F",        "Petróleo Brent"],
    ["TIO=F",       "Minério de Ferro"],
    ["BTC-USD",     "Bitcoin"]
]

YFdata = yf.download(list(map(lambda x:x[0], symbols)), start = "1994-01-03", end=datetime.datetime.today().strftime('%Y-%m-%d'), interval="1d") #end= "2024-10-10",

# # mock data
# YFdata = pd.DataFrame({
#     ('Open', '^BVSP'): [100, 101, 102],
#     ('Close', '^BVSP'): [105, 106, 107],
#     ('High', '^BVSP'): [110, 111, 112],
#     ('Low', '^BVSP'): [95, 96, 97],
#     ('Volume', '^BVSP'): [1000, 2000, 3000],
#     ('Open', 'BRL=X'): [1.5, 1.6, 1.7],
#     ('Close', 'BRL=X'): [1.55, 1.65, 1.75],
#     ('High', 'BRL=X'): [1.6, 1.7, 1.8],
#     ('Low', 'BRL=X'): [1.4, 1.5, 1.6],
#     ('Volume', 'BRL=X'): [5000, 6000, 7000],
#     ('Open', '^DJI'): [25000, 25100, 25200],
#     ('Close', '^DJI'): [25500, 25600, 25700],
#     ('High', '^DJI'): [26000, 26100, 26200],
#     ('Low', '^DJI'): [24500, 24600, 24700],
#     ('Volume', '^DJI'): [1000000, 1100000, 1200000],
#     ('Open', '^GSPC'): [3000, 3100, 3200],
#     ('Close', '^GSPC'): [3050, 3150, 3250],
#     ('High', '^GSPC'): [3100, 3200, 3300],
#     ('Low', '^GSPC'): [2900, 2950, 3000],
#     ('Volume', '^GSPC'): [2000000, 2100000, 2200000],
#     ('Open', '^IXIC'): [8000, 8100, 8200],
#     ('Close', '^IXIC'): [8050, 8150, 8250],
#     ('High', '^IXIC'): [8100, 8200, 8300],
#     ('Low', '^IXIC'): [7900, 7950, 8000],
#     ('Volume', '^IXIC'): [3000000, 3100000, 3200000],
#     ('Open', '000001.SS'): [3000, 3100, 3200],
#     ('Close', '000001.SS'): [3050, 3150, 3250],
#     ('High', '000001.SS'): [3100, 3200, 3300],
#     ('Low', '000001.SS'): [2900, 2950, 3000],
#     ('Volume', '000001.SS'): [4000000, 4100000, 4200000],
#     ('Open', '^N225'): [20000, 20100, 20200],
#     ('Close', '^N225'): [20500, 20600, 20700],
#     ('High', '^N225'): [21000, 21100, 21200],
#     ('Low', '^N225'): [19500, 19600, 19700],
#     ('Volume', '^N225'): [5000000, 5100000, 5200000],
#     ('Open', '^HSI'): [25000, 25100, 25200],
#     ('Close', '^HSI'): [25500, 25600, 25700],
#     ('High', '^HSI'): [26000, 26100, 26200],
#     ('Low', '^HSI'): [24500, 24600, 24700],
#     ('Volume', '^HSI'): [6000000, 6100000, 6200000],
#     ('Open', '^KS11'): [2000, 2010, 2020],
#     ('Close', '^KS11'): [2050, 2060, 2070],
#     ('High', '^KS11'): [2100, 2110, 2120],
#     ('Low', '^KS11'): [1950, 1960, 1970],
#     ('Volume', '^KS11'): [7000000, 7100000, 7200000],
#     ('Open', '^AXJO'): [6000, 6010, 6020],
#     ('Close', '^AXJO'): [6050, 6060, 6070],
#     ('High', '^AXJO'): [6100, 6110, 6120],
#     ('Low', '^AXJO'): [5950, 5960, 5970],
#     ('Volume', '^AXJO'): [8000000, 8100000, 8200000],
#     ('Open', '^FTSE'): [7000, 7010, 7020],
#     ('Close', '^FTSE'): [7050, 7060, 7070],
#     ('High', '^FTSE'): [7100, 7110, 7120],
#     ('Low', '^FTSE'): [6950, 6960, 6970],
#     ('Volume', '^FTSE'): [9000000, 9100000, 9200000],
#     ('Open', '^GDAXI'): [12000, 12010, 12020],
#     ('Close', '^GDAXI'): [12050, 12060, 12070],
#     ('High', '^GDAXI'): [12100, 12110, 12120],
#     ('Low', '^GDAXI'): [11950, 11960, 11970],
#     ('Volume', '^GDAXI'): [10000000, 10010000, 10020000],
#     ('Open', '^FCHI'): [5000, 5010, 5020],
#     ('Close', '^FCHI'): [5050, 5060, 5070],
#     ('High', '^FCHI'): [5100, 5110, 5120],
#     ('Low', '^FCHI'): [4950, 4960, 4970],
#     ('Volume', '^FCHI'): [11000000, 11010000, 11020000],
#     ('Open', 'FTSEMIB.MI'): [25000, 25100, 25200],
#     ('Close', 'FTSEMIB.MI'): [25500, 25600, 25700],
#     ('High', 'FTSEMIB.MI'): [26000, 26100, 26200],
#     ('Low', 'FTSEMIB.MI'): [24500, 24600, 24700],
#     ('Volume', 'FTSEMIB.MI'): [12000000, 12010000, 12020000],
#     ('Open', '^STOXX'): [3500, 3510, 3520],
#     ('Close', '^STOXX'): [3550, 3560, 3570],
#     ('High', '^STOXX'): [3600, 3610, 3620],
#     ('Low', '^STOXX'): [3450, 3460, 3470],
#     ('Volume', '^STOXX'): [13000000, 13010000, 13020000],
#     ('Open', 'CL=F'): [50, 51, 52],
#     ('Close', 'CL=F'): [55, 56, 57],
#     ('High', 'CL=F'): [60, 61, 62],
#     ('Low', 'CL=F'): [45, 46, 47],
#     ('Volume', 'CL=F'): [14000000, 14010000, 14020000],
#     ('Open', 'BZ=F'): [60, 61, 62],
#     ('Close', 'BZ=F'): [65, 66, 67],
#     ('High', 'BZ=F'): [70, 71, 72],
#     ('Low', 'BZ=F'): [55, 56, 57],
#     ('Volume', 'BZ=F'): [15000000, 15010000, 15020000],
#     ('Open', 'TIO=F'): [1000, 1010, 1020],
#     ('Close', 'TIO=F'): [1050, 1060, 1070],
#     ('High', 'TIO=F'): [1100, 1110, 1120],
#     ('Low', 'TIO=F'): [950, 960, 970],
#     ('Volume', 'TIO=F'): [16000000, 16010000, 16020000],
#     ('Open', 'BTC-USD'): [30000, 30100, 30200],
#     ('Close', 'BTC-USD'): [30500, 30600, 30700],
#     ('High', 'BTC-USD'): [31000, 31100, 31200],
#     ('Low', 'BTC-USD'): [29500, 29600, 29700],
#     ('Volume', 'BTC-USD'): [17000000, 17010000, 17020000]
# }, index=pd.date_range(start='2023-01-01', periods=3, freq='D'))

def save_each_indicator_in_one_file():
    """
    Save each indicator in one file
    """
    # save each indicator in one file
    for i, symbol in enumerate(symbols):
        # use the symbol to get the data, it will be the second element of the df column tuple
        filtered_columns = [col for col in YFdata.columns if col[1] == symbol[0]]
        filtered_df = YFdata[filtered_columns]
        # edit filtered_df columns to have only the first value of the tuple
        filtered_df.columns = [col[0] for col in filtered_df.columns]
        print(f"Data for {symbol[1]}:")
        print(filtered_df.head())
        # save the data to a csv file
        filtered_df.to_csv(f"0 - asDownloaded/YahooFinance/{i}-{symbol[1]}.csv", index=True)

def save_all_data_in_one_file():
    """
    Save the data in one file
    """
    # yfinace returns the data with the columns in the format: ('Ticker', 'Attribute')
    # we need to convert the columns to the format: 'Index - Attribute'
    # where Index is the name of the index (e.g. IBOVESPA, Dow Jones, etc.)
    # and Attribute is the name of the attribute (e.g. Open, Close, High, Low, Volume)
    YFdata.columns = pd.MultiIndex.from_tuples(YFdata.columns)  
    # convert the columns to the format: 'Index - Attribute'
    YFdata.columns = [f"{symbols[i // 5][1]} - {col[0]}" for i, col in enumerate(YFdata.columns)]
    # save the data to a csv file in the 0 - asDownloaded/YahooFinance folder
    YFdata.to_csv("0 - asDownloaded/YahooFinance/_All Yahoo Finance Indicators_.csv", index=True)

save_each_indicator_in_one_file()
save_all_data_in_one_file()