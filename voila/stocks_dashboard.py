import ipywidgets as widgets
from IPython.display import display
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Create input widget for stock ticker
ticker_input = widgets.Text(
    value='AAPL',
    placeholder='Enter stock ticker (e.g., AAPL)',
    description='Stock Ticker:',
    disabled=False
)

# Create button widget
fetch_button = widgets.Button(description="Fetch Data")

# Create output widget for displaying the plot
output = widgets.Output()

def fetch_stock_data(ticker):
    end_date = datetime.now()
    start_date = end_date - timedelta(days=5*365)
    
    stock = yf.Ticker(ticker)
    df = stock.history(start=start_date, end=end_date)
    return df

def plot_stock_data(df, ticker):
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['Close'])
    plt.title(f'{ticker} Stock Price (Last 5 Years)')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()

def on_button_clicked(b):
    with output:
        output.clear_output()
        ticker = ticker_input.value
        df = fetch_stock_data(ticker)
        plot_stock_data(df, ticker)
        plt.show()

# Connect the button click event to the callback function
fetch_button.on_click(on_button_clicked)

# Display the widgets
display(ticker_input, fetch_button, output)
