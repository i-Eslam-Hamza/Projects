
# Import necessary libraries
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from flask import Flask, render_template
import plotly.express as px
import plotly.tools as tls
import folium
from folium.plugins import MarkerCluster
import time
import pandas as pd
import warnings 
warnings.filterwarnings('ignore')

# Initialize the Dash app
app = dash.Dash(__name__)



# Load and clean the data as before
data_cleaned = pd.read_csv("D:/PYTHON/app/cleaned_happiness_data.csv")

# Create figures for each chart
# Scatter Plot: GDP per Capita vs. Happiness Score by Region
fig_scatter = px.scatter(data_cleaned, 
                         x='Economy (GDP per Capita)', 
                         y='Happiness Score', 
                         color='Region', 
                         title='Effect of GDP per Capita on Happiness Score by Region',
                         hover_name='Country', 
                         template='plotly_white')

fig_scatter.update_layout(legend=dict(title='Region', orientation='h', yanchor='bottom', 
                              y=1.02, xanchor='center', x=0.5), title_y=0.98)

# Bar Chart: Top 10 Countries by Economy (GDP per Capita)
top_10_economy = data_cleaned.nlargest(10, 'Economy (GDP per Capita)')
fig_economy = px.bar(top_10_economy, 
                         x='Country', 
                         y='Economy (GDP per Capita)',
                         color = 'Country', 
                         title='Top 10 Countries by Economy (GDP per Capita)',
                         labels={'Economy (GDP per Capita)': 'GDP per Capita'},
                         template='plotly_white')
fig_economy.update_xaxes(tickangle=45)

# Bar Chart: Top 10 Countries by Health (Life Expectancy)
top_10_health = data_cleaned.nlargest(10, 'Health (Life Expectancy)')
fig_health = px.bar(top_10_health, 
                        x='Country', 
                        y='Health (Life Expectancy)',
                        color = 'Country', 
                        title='Top 10 Countries by Health (Life Expectancy)',
                        labels={'Health (Life Expectancy)': 'Life Expectancy'},
                        template='plotly_white')
fig_health.update_xaxes(tickangle=45)

# Correlation Heatmap for Key Features
correlation_columns = ['Economy (GDP per Capita)', 'Family', 
                       'Health (Life Expectancy)', 'Freedom', 
                       'Trust (Government Corruption)', 'Generosity', 
                       'Happiness Score']
correlation_matrix = data_cleaned[correlation_columns].corr()
fig_correlation = px.imshow(correlation_matrix, 
                        title='Correlation Matrix for Key Features', 
                        color_continuous_scale='icefire',
                        labels=dict(x="Features", y="Features", color='red'))
fig_correlation.update_layout(template='plotly_white')

# Pie Chart: Happiness Score by Region
happiness_by_region = data_cleaned.groupby('Region')['Happiness Score'].mean().reset_index()
fig_pie = px.pie(happiness_by_region, 
                 values='Happiness Score', 
                 names='Region', 
                 title='Happiness Score Distribution by Region',
                 template='plotly_white')

#  Map: GDP per Capita by Country with Healthy Life Expectancy Tooltip
  # Filter out countries where coordinates could not be found
map_data = data_cleaned.dropna(subset=['Latitude', 'Longitude'])

# Initialize the Folium map
world_map = folium.Map(location=[20, 0], zoom_start=2, tiles="CartoDB positron")

# Add a marker cluster
marker_cluster = MarkerCluster().add_to(world_map)

# # Add markers to the map
# for idx, row in map_data.iterrows():
#     folium.Marker(
#         location=[row['Latitude'], row['Longitude']],
#         popup=f"<strong>{row['Country']}</strong><br>GDP per Capita: {row['Economy (GDP per Capita)']}<br>Healthy Life Expectancy: {row['Health (Life Expectancy)']}",
#         tooltip=row['Country']
#     ).add_to(marker_cluster)
#     time.sleep(1)  # Add delay to avoid hitting geocoding API limits

# # Save the map to an HTML file
# map_file = "map.html"
# world_map.save(map_file)


# Layout of the dashboard
app.layout = html.Div(style={'font-family': 'Arial, sans-serif'}, children=[
    html.H1("Happiness Survey Data 2016 Dashboard", style={'textAlign': 'center'}),

    # First Division: Bar Charts Side by Side
    html.Div(style={'display': 'flex', 'justify-content': 'center', 'backgroundColor': 'grey', 'border-radius': '10px', 'padding': '10px'}, children=[
        dcc.Graph(figure=fig_economy, style={'flex': '1', 'margin': '10px'}),
        dcc.Graph(figure=fig_health, style={'flex': '1', 'margin': '10px'})
    ]),

    # Second Division: Scatter Plot
    html.Div(style={'backgroundColor': 'grey', 'border-radius': '10px', 'padding': '10px', 'margin-top': '10px'}, children=[
        dcc.Graph(figure=fig_scatter)
    ]),

    # Third Division: Pie Plot and Correlation Figure Side by Side
    html.Div(style={'display': 'flex', 'justify-content': 'center', 'backgroundColor': 'grey', 'border-radius': '10px', 'padding': '10px', 'margin-top': '10px'}, children=[
        dcc.Graph(figure=fig_pie, style={'flex': '1', 'margin': '10px'}),
        dcc.Graph(figure=fig_correlation, style={'flex': '1', 'margin': '10px'})
    ]),

    # Fourth Division: World Map
    html.Div( style={'backgroundColor': 'grey', 'border-radius': '10px', 'padding': '10px', 'margin-top': '10px'}, children=[
    html.Iframe(src="/assets/map.html", width='100%', height='600px', style={'border': 'none', 'border-radius': '10px'})
    ]),

])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=8049, host='127.0.0.1')









