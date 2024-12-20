from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.models import TextInput, Button, Div, ColumnDataSource
from bokeh.plotting import figure
import yfinance as yf
from datetime import datetime, timedelta

# Create input widget for stock ticker
stock_ticker = TextInput(title="Enter Stock Ticker (e.g., AAPL, GOOGL)", value="AAPL")

# Create button widget
fetch_button = Button(label="Fetch Data", button_type="success")

# Create a placeholder for the output
output_div = Div(text="", width=400, height=100)

# Create a ColumnDataSource to hold the stock data
source = ColumnDataSource(data=dict(date=[], close=[]))

# Create the plot
p = figure(title="Stock Price", x_axis_label="Date", y_axis_label="Price (USD)", x_axis_type="datetime", width=800, height=400)
p.line('date', 'close', source=source, line_width=2)

def fetch_data():
    ticker = stock_ticker.value
    end_date = datetime.now()
    start_date = end_date - timedelta(days=5*365)
    
    try:
        stock = yf.Ticker(ticker)
        df = stock.history(start=start_date, end=end_date)
        
        source.data = dict(
            date=df.index,
            close=df['Close']
        )
        
        p.title.text = f"{ticker} Stock Price (Last 5 Years)"
        output_div.text = f"Data fetched successfully for {ticker}"
    except Exception as e:
        output_div.text = f"Error fetching data: {str(e)}"

# Connect the button click event to the callback function
fetch_button.on_click(fetch_data)

# Layout the widgets and plot
inputs = column(stock_ticker, fetch_button, output_div)
layout = row(inputs, p)

# Add the layout to the current document
curdoc().add_root(layout)
