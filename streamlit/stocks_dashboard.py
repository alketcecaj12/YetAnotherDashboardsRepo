import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime, timedelta

st.set_page_config(layout="wide")
st.title("Stock Data Visualization Dashboard")

def get_stock_data(ticker):
    end_date = datetime.now()
    start_date = end_date - timedelta(days=5*365)
    
    stock = yf.Ticker(ticker)
    df = stock.history(start=start_date, end=end_date)
    return df

def plot_stock_data(df, ticker):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df['Close'], mode='lines', name='Close Price'))
    fig.update_layout(title=f'{ticker} Stock Price (Last 5 Years)',
                      xaxis_title='Date',
                      yaxis_title='Price (USD)',
                      template='plotly_dark')
    return fig

ticker_input = st.text_input("Enter Stock Ticker (e.g., AAPL, GOOGL)", "AAPL")

if ticker_input:
    df = get_stock_data(ticker_input)
    
    st.subheader("Stock Data")
    st.dataframe(df)
    
    st.subheader("Stock Price Chart")
    fig = plot_stock_data(df, ticker_input)
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Stock Statistics")
    current_price = df['Close'].iloc[-1]
    price_change = df['Close'].iloc[-1] - df['Close'].iloc[0]
    percent_change = (price_change / df['Close'].iloc[0]) * 100
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Current Price", f"${current_price:.2f}")
    col2.metric("Price Change (5Y)", f"${price_change:.2f}")
    col3.metric("Percent Change (5Y)", f"{percent_change:.2f}%")
