import plotly.graph_objects as go
import pandas as pd

path = '/home/duck/data'
save_path = path + '/images'
csv_file_path = path + '/basedata/product_mix.csv'

axis_range = 500   

def save_graph(fig, path):
    print('Saving Figure…')
    fig.write_image(path)
    print('Figure saved!')


print('\tStart /home/duck/scripts/generate_product_mixes_graphs.py…')

df = pd.read_csv(csv_file_path, index_col=0)

max_ducks = df.iloc[0]['max']
max_fish = df.iloc[1]['max']

product_mix1_ducks = df.iloc[0]['product_mix1']
product_mix1_fish = df.iloc[1]['product_mix1']

restriction_ducks = df.iloc[0]['restriction']
restriction_fish = df.iloc[1]['restriction']

print('Creating Product Mix Figure…')

fig = go.Figure()

fig.update_layout(title_text='Product Mixes', title_x=0.5)

fig.update_yaxes(range=(0,axis_range), title_text='Ducks')
fig.update_xaxes(range=(0,axis_range), title_text='Fish')

#constraints
fig.add_vline(x=max_fish, line_dash='dash', line_color='black')
fig.add_hline(y=max_ducks, line_dash='dash',line_color='black')

#product mix 1 --> 100 ducks and 200 fish --> no data for the other example product mixes!
fig.add_trace(go.Scatter(x=[product_mix1_fish], y=[product_mix1_ducks]))

save_graph(fig, save_path + '/product_mixes.png')

fig.add_shape(type='line',
    x0=0, y0=restriction_ducks, x1=restriction_fish, y1=0,
    line=dict(
        color='black',
        dash='dash',
    )
)
save_graph(fig, save_path + '/product_mix_with_scope.png')

print('\tFinished /home/duck/scripts/generate_product_mixes_graphs.py!')