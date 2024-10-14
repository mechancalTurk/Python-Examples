# Import required libraries
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Read the airline data into a pandas dataframe
spacex_data = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_data['Payload Mass (kg)'].max()
min_payload = spacex_data['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                # dcc.Dropdown(id='site-dropdown',...)
                                dcc.Dropdown(id='site-dropdown',
                                             options=[
                                                 {'label': 'All Sites', 'value': 'ALL'},
                                                 {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
                                                 {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'},
                                                 {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
                                                 {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
                                             ],
                                             value='ALL',
                                             placeholder="Select a Launch Site here",
                                             searchable=True
                                             ),
                                html.Br(),
                                
                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site:
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),
                                html.P("Payload range (Kg):"),
                                
                                # TASK 3: Add a slider to select payload range
                                #dcc.RangeSlider(id='payload-slider',...)
                                html.Div(dcc.RangeSlider(id='payload-slider',
                                                        min=0, max=10000, step=1000,
                                                        marks={0: '0', 100: '100'},
                                                        value=[min_payload, max_payload])),
                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success:
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output:
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(entered_site):
    if entered_site == 'ALL':
        # Count the total success launches (class == 1) for all sites
        success_counts = spacex_data[spacex_data['class'] == 1].groupby('Launch Site').size().reset_index(name='counts')
        result = px.pie(success_counts, values='counts', names='Launch Site', 
                        title='Total Success Launches By Site')
    else:
        # Count the Success vs Failed launches for the selected site
        filtered_data = spacex_data[spacex_data['Launch Site'] == entered_site]
        success_fail_counts = filtered_data['class'].value_counts().reset_index(name='counts')
        success_fail_counts.columns = ['class', 'counts']
        result = px.pie(success_fail_counts, values='counts', names='class', 
                        title=f'Success vs Failure Launches for {entered_site}')
    return result


# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output:
@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
              [Input(component_id='site-dropdown', component_property='value'),
               Input(component_id='payload-slider', component_property='value')])
def get_scatter_chart(selected_site, payload_range):
    low, high = payload_range
    if selected_site == 'ALL':
        df = spacex_data
    else:
        df = spacex_data[spacex_data['Launch Site'] == selected_site]
    
    df_mask = df[(df['Payload Mass (kg)'] > low) & (df['Payload Mass (kg)'] < high)]
    
    result = px.scatter(df_mask, x='Payload Mass (kg)', y='class', color='Booster Version',
                     hover_data=['Payload Mass (kg)'])
    
    return result

# Run the app:
if __name__ == '__main__':
    app.run_server()