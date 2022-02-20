import os
import pandas as pd
import plotly.graph_objects as go

print('\tStarting /home/duck/scripts/reproduce_historical_sales_data_diagram.py…')

path = '/home/duck/data'
csv_file_path = path + '/historical_sales_data_csv_format.csv'
image_path = '/home/duck/images'

df = pd.read_csv(csv_file_path, index_col=0)
print('Reading csv file…')

year = df['Year']
months = df['Month']
fish = df['Fish']
ducks = df['Ducks']
total = df['Total']

monthList = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
          'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

indexMonths = 0
index = 0

date_data = []

for month in months:
    date_data.append(monthList[indexMonths] + ' ' + str(year[index]))
    index += 1
    indexMonths += 1
    if indexMonths == 12:
        indexMonths = 0


df = df.drop(columns=['Month', 'Year'])
df['Date'] = date_data

print('Creating Figure…')
fig = go.Figure()

fig.add_trace(go.Scatter(x=df['Date'], y=ducks, line_color='red', name='Ducks'))
fig.add_trace(go.Scatter(x=df['Date'], y=fish, line_color='blue', name='Fish'))
fig.add_trace(go.Scatter(x=df['Date'], y=total, line_color='green', name='Total'))

fig.update_xaxes(title_text="Months")
fig.update_yaxes(title_text="Units sold")

print('Saving Figure…')

fig.write_image(image_path + '/hist_sales_graph.png')

print('Figure saved!')
print('\tFinished /home/duck/scripts/reproduce_historical_sales_data_diagram.py!')