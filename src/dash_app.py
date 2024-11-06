import pandas as pd
from dash import dcc, html
import dash
import plotly.express as px

# Initialize the Dash app
app = dash.Dash(__name__)

# Load the data
data = pd.read_csv('formatted_sales_data.csv')

# Ensure 'sales' column is numeric, removing any unwanted characters (e.g., dollar sign)
data['sales'] = pd.to_numeric(data['sales'], errors='coerce')

# Convert the 'date' column to datetime format
data['date'] = pd.to_datetime(data['date'], errors='coerce')

# Check for missing data (NaT, NaN)
print("Missing data count:\n", data.isna().sum())

# Drop any rows with missing or invalid data
data = data.dropna()

# Create the line chart using Plotly Express
fig = px.line(data, x='date', y='sales', title='Pink Morsel Sales Over Time',
              labels={'sales': 'Sales ($)', 'date': 'Date'})

# Highlight the price increase date (15th January 2021)
price_increase_date = pd.to_datetime('2021-01-15')

# Convert the datetime to a timestamp (number of seconds since Unix epoch)
price_increase_timestamp = price_increase_date.timestamp()

# Add the vertical line for the price increase
fig.add_vline(x=price_increase_timestamp, line=dict(color='red', dash='dash'),
              annotation_text='Price Increase', annotation_position='top')

# Define the layout of the app
app.layout = html.Div([
    html.H1('Soul Foods Pink Morsel Sales Visualization', style={'text-align': 'center'}),

    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    ),
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
