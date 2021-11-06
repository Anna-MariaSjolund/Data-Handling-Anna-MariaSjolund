import pandas as pd

class StockDataLocal:
    """Class method to get and process local stock data."""
    
    def __init__(self, data_folder_path:str="../data/") -> None:
        self._data_folder_path = data_folder_path #Sets the data folder path
    
    def stock_dataframe(self, stockname:str) -> list: 
        """
        Returns:
            list of two dataframes, one for daily time series, one for interdaily.
            The daily is updated once a day, the intradaily is updated every 60 minutes.

        """

        stock_df_list = []

        for path_ending in ["_TIME_SERIES_DAILY.csv", "_TIME_SERIES_INTRADAY_EXTENDED.csv"]: #The ending of the file name
            path = self._data_folder_path + stockname + path_ending #Concating the data folder path
            stock = pd.read_csv(path, index_col=0, parse_dates=True) #index_col=0 set the first column as index (the dates) and parse the dates
            stock.index.rename("Date", inplace=True) #Rename index to Date, inplace=True changes the dataframe

            stock_df_list.append(stock)
        
        return stock_df_list 

#cd folder name (to go down one folder)
#Mark everything, right click and choose run in interactive window