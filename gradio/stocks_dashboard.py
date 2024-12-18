import gradio as gr
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta

def get_stock_data(ticker):
    end_date = datetime.now()
    start_date = end_date - timedelta(days=5*365)
    
    stock = yf.Ticker(ticker)
    df = stock.history(start=start_date, end=end_date)
    return df

def plot_stock_data(ticker):
    df = get_stock_data(ticker)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df['Close'], mode='lines', name='Close Price'))
    fig.update_layout(title=f'{ticker} Stock Price (Last 5 Years)',
                      xaxis_title='Date',
                      yaxis_title='Price (USD)',
                      template='plotly_white')
    return fig

def create_dashboard(ticker):
    df = get_stock_data(ticker)
    fig = plot_stock_data(ticker)
    return df, fig

with gr.Blocks() as demo:
    gr.Markdown("# Stock Data Visualization Dashboard")
    ticker_input = gr.Textbox(label="Enter Stock Ticker (e.g., AAPL, GOOGL)")
    submit_btn = gr.Button("Submit")
    
    with gr.Row():
        with gr.Column():
            output_table = gr.DataFrame(label="Stock Data")
        with gr.Column():
            output_plot = gr.Plot(label="Stock Price Chart")
    
    submit_btn.click(fn=create_dashboard, inputs=ticker_input, outputs=[output_table, output_plot])

demo.launch()
