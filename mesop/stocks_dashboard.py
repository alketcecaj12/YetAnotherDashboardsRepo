import mesop as me
import yfinance as yf
import plotly.graph_objs as go
from datetime import datetime, timedelta

@me.stateclass
class State:
    ticker: str = ""
    stock_data: dict = {}

def fetch_stock_data(ticker: str):
    end_date = datetime.now()
    start_date = end_date - timedelta(days=5*365)
    stock = yf.Ticker(ticker)
    data = stock.history(start=start_date, end=end_date)
    return data

def update_stock_data(action: me.ClickEvent):
    state = me.state(State)
    if state.ticker:
        state.stock_data = fetch_stock_data(state.ticker)

def create_stock_chart(data):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name='Close Price'))
    fig.update_layout(
        title=f'{state.ticker} Stock Price (Last 5 Years)',
        xaxis_title='Date',
        yaxis_title='Price (USD)',
        template='plotly_dark'
    )
    return fig

@me.page(path="/stock-dashboard")
def stock_dashboard():
    state = me.state(State)

    me.text("Stock Data Visualization Dashboard", type="headline-4")
    
    me.text_input(label="Enter Stock Ticker (e.g., AAPL, GOOGL)", on_change=lambda e: setattr(state, 'ticker', e.value))
    
    me.button("Fetch Data", on_click=update_stock_data)

    if state.stock_data:
        me.plotly(create_stock_chart(state.stock_data))
        
        me.text("Stock Statistics", type="headline-5")
        current_price = state.stock_data['Close'].iloc[-1]
        price_change = state.stock_data['Close'].iloc[-1] - state.stock_data['Close'].iloc[0]
        percent_change = (price_change / state.stock_data['Close'].iloc[0]) * 100
        
        me.text(f"Current Price: ${current_price:.2f}")
        me.text(f"Price Change (5Y): ${price_change:.2f}")
        me.text(f"Percent Change (5Y): {percent_change:.2f}%")
