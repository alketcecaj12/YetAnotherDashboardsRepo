import altair as alt
import panel as pn
import yfinance as yf
import pandas as pd

pn.extension(sizing_mode="stretch_width")
alt.data_transformers.disable_max_rows()

def fetch_stock_data(ticker):
    stock = yf.Ticker(ticker)
    data = stock.history(period="10y")
    data = data.reset_index()
    data['Date'] = pd.to_datetime(data['Date'])
    return data

def create_stock_chart(data, ticker):
    chart = alt.Chart(data).mark_line().encode(
        x=alt.X('Date:T', title='Date'),
        y=alt.Y('Close:Q', title='Closing Price (USD)'),
        tooltip=['Date:T', 'Close:Q', 'Open:Q', 'High:Q', 'Low:Q', 'Volume:Q']
    ).properties(
        title=f"{ticker} Stock Price - Last 10 Years",
        width='container',
        height=400
    ).interactive()
    
    return chart

def update_chart(ticker):
    if not ticker:
        return pn.pane.Markdown("Please enter a valid stock ticker.")
    
    try:
        data = fetch_stock_data(ticker)
        chart = create_stock_chart(data, ticker)
        return pn.pane.Vega(chart)
    except Exception as e:
        return pn.pane.Markdown(f"Error fetching data for {ticker}: {str(e)}")

ticker_input = pn.widgets.TextInput(name="Stock Ticker", placeholder="Enter stock ticker (e.g., AAPL)")
update_button = pn.widgets.Button(name="Update Chart", button_type="primary")

@pn.depends(ticker_input.param.value, update_button.param.clicks)
def get_chart(ticker, _):
    return update_chart(ticker)

dashboard = pn.Column(
    pn.pane.Markdown("# Stock Price Dashboard"),
    pn.pane.Markdown("Enter a stock ticker and click 'Update Chart' to view the last 10 years of stock data."),
    pn.Row(ticker_input, update_button),
    get_chart
)

dashboard.servable()
