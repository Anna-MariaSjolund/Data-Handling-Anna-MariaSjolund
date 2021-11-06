import pandas as pd
from dash import dcc, html
import dash
from load_data import StockDataLocal
from dash.dependencies import Output, Input
import plotly_express as px
from time_filtering import filter_time

#We create a stock_data_object from our StockDataLocal
#In this we have a method that load our data as a dataframe
stock_data_object = StockDataLocal()

symbol_dict = dict(AAPL="Apple", NVDA="Nvidia", TSLA="Tesla", IBM="IBM")

#A dictionary of label and value
#Loops throgh the symbol_dict above
#label (name) is what we will see in the dropdown (e.g Apple)
stock_options_dropdown=[{"label":name, "value":symbol}
                        for symbol, name in symbol_dict.items()]

#A dictionary of dataframes
#We loop through the keys in the dict (if we do not use dict.items(), then we get both key and value)
df_dict = {symbol:stock_data_object.stock_dataframe(symbol)
            for symbol in symbol_dict}

#The labels for our slider
#slider_marks should be a dictionary
slider_marks = {i:mark for i, mark in enumerate(
    ["1 day", "1 week", "1 month", "3 months", "1 year", "5 years", "Max"]
)}

#In the dash module there is a class Dash (and we create such an object)
#It needs __name__ and when we run this file we get __main__
app = dash.Dash(__name__) 

#a Div is a html element where we can add different things
#The Div element has children as first argument
#We add a list to html.Div
#We use hmtl. to reach the different classes
app.layout = html.Div([
    html.H1("Stocks Viewer"), #The first heading #H2 gives the second heading
    html.P("Choose a stock"), #Paragraph tag
    dcc.Dropdown(id="stock-picker-dropdown", #We have to name it so we can control it later
        className="", #Styling
        options=stock_options_dropdown, #Set above, option takes a dictionary of label and value, now these are added to dropdown
        value="AAPL"), #It will start with AAPL
    dcc.Graph(id="stock-graph", className=""), #Adds a graph
    dcc.Slider(id="time-slider", className="", #Sets the slider, we give it an ID
        min=0, max=6, #7 steps (from 0 to 6) for our slider 
        step=None, 
        value=2, #Where the slider starts
        marks=slider_marks) #Created above
    ]) 

#A decorator that decorates a function
#The dropdown is our input
#Output is our graph
#Both Output and Input takes component_id and component_property
@app.callback(
    Output("stock-graph", "figure"), #stock_graph is the id for dcc.Graph
    Input("stock-picker-dropdown", "value"), #stock-picker-dropdown is the id of the dcc.Dropdown, value is the symbol
    Input("time-slider", "value") #value is the time_index
    )

def update_graph(stock, time_index): #stock is what we choose and it should be updated when we choose 
    #Called dff because we "filter" the df
    dff_daily, dff_intraday = df_dict[stock] #df_dict[stock] gives us a list of two stocks (both dataframes) which we unpack

    dff = dff_intraday if time_index <= 2 else dff_daily

    #It is a dictionary because we want to map 0-6 (i) to the number of days
    #The list in enumerate is the number of days (365*5 the number of days for five years)
    days = {i:day for i, day in enumerate([1, 7, 30, 90, 365, 365*5])}

    #If time_index is 6 it should be set to max
    #time_index is 0 to 6 
    dff = dff if time_index == 6 else filter_time(dff, days[time_index])

    #Creates the px figure
    fig = px.line(dff, x=dff.index, y="close")

    return fig #fig object goes into Output property, i.e. figure property

#If we run the file directly we run an app.run_server (and we want the debug output)
if __name__ == "__main__":
    app.run_server(debug=True) 

#To open an interactive window, go to:
#View -> Command Palette -> Jupyter: Create Interactive Window 
