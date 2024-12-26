from shiny import App, ui, render, reactive
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

app_ui = ui.page_fluid(
    ui.h1("Stock Price Dashboard"),
    ui.layout_sidebar(
        ui.panel_sidebar(
            ui.input_text("ticker", "Enter Stock Ticker:", placeholder="e.g., AAPL"),
            ui.input_action_button("submit", "Fetch Data"),
        ),
        ui.panel_main(
            ui.output_plot("stock_plot"),
            ui.output_text("error_message")
        )
    )
)

def server(input, output, session):
    @reactive.Calc
    def stock_data():
        input.submit()
        ticker = input.ticker()
        if not ticker:
            return None
        try:
            stock = yf.Ticker(ticker)
            data = stock.history(period="10y")
            return data
        except Exception as e:
            return str(e)

    @output
    @render.plot
    def stock_plot():
        data = stock_data()
        if isinstance(data, pd.DataFrame) and not data.empty:
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name='Close Price'))
            fig.update_layout(
                title=f"{input.ticker()} Stock Price - Last 10 Years",
                xaxis_title="Date",
                yaxis_title="Close Price",
                height=600
            )
            return fig

    @output
    @render.text
    def error_message():
        data = stock_data()
        if isinstance(data, str):
            return f"Error: {data}"
        elif data is None or data.empty:
            return "Please enter a valid stock ticker and click 'Fetch Data'."
        return ""

app = App(app_ui, server)
