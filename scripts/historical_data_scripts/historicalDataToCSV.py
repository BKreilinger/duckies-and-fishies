import pandas as pd

path = '/home/duck/data'
data = path + '/historical_sales_data.xls'
csv_file_path = path + '/historical_sales_data_csv_format.csv'

print('Creating CSV file from excel file…')
df = pd.read_excel(data)
csv_file = df.to_csv(csv_file_path)