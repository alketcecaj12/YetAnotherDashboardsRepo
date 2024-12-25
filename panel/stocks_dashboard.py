import panel as pn
import yfinance as yf
import hvplot.pandas

# Enable Panel extensions
pn.extension()

# Create input widget for stock ticker
ticker_input = pn.widgets.TextInput(name="Stock Ticker", placeholder="Enter stock ticker (e.g., AAPL)")

# Function to fetch and plot stock data
def fetch_and_plot_stock_data(ticker):
    if not ticker:
        return pn.pane.Markdown("Please enter a stock ticker.")
    
    try:
        # Download stock data
        stock = yf.Ticker(ticker)
        data = stock.history(period="10y")
        
        if data.empty:
            return pn.pane.Markdown(f"No data available for {ticker}.")
        
        # Create plot
        plot = data['Close'].hvplot.line(
            title=f"{ticker} Stock Price - Last 10 Years",
            xlabel="Date",
            ylabel="Close Price",
            height=400,
            width=800
        )
        
        return pn.Column(
            pn.pane.Markdown(f"## Stock Data for {ticker}"),
            plot
        )
    except Exception as e:
        return pn.pane.Markdown(f"Error fetching data for {ticker}: {str(e)}")

# Create reactive function
@pn.depends(ticker_input.param.value)
def update_plot(ticker):
    return fetch_and_plot_stock_data(ticker)

# Create dashboard layout
dashboard = pn.Column(
    pn.pane.Markdown("# Stock Price Dashboard"),
    ticker_input,
    update_plot
)

# Serve the dashboard
dashboard.servable()
