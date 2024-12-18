import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import yfinance as yf
import plotly.graph_objs as go
from datetime import datetime, timedelta

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Stock Data Visualization Dashboard"),
    html.Div([
        dcc.Input(id="ticker-input", type="text", placeholder="Enter Stock Ticker (e.g., AAPL, GOOGL)", value="AAPL"),
        html.Button("Submit", id="submit-button", n_clicks=0)
    ]),
    dcc.Graph(id="stock-graph")
])

@app.callback(
    Output("stock-graph", "figure"),
    Input("submit-button", "n_clicks"),
    State("ticker-input", "value")
)
def update_graph(n_clicks, ticker):
    if n_clicks > 0:
        end_date = datetime.now()
        start_date = end_date - timedelta(days=5*365)
        
        stock = yf.Ticker(ticker)
        df = stock.history(start=start_date, end=end_date)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df.index, y=df['Close'], mode='lines', name='Close Price'))
        fig.update_layout(
            title=f'{ticker} Stock Price (Last 5 Years)',
            xaxis_title='Date',
            yaxis_title='Price (USD)',
            template='plotly_dark'
        )
        return fig
    
    return go.Figure()

if __name__ == '__main__':
    app.run_server(debug=True)
