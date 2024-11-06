import dash
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div("Hello, Dash!")

if __name__ == '__main__':
    app.run_server(debug=True)
