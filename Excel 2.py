
import pandas as pd
import os
df = pd.read_excel('Financial Sample.xlsx')
column = 'Product'
unique_values = df[column].unique()
output_dir = 'Financial Sample Separated'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
for unique_value in unique_values:
    df_output = df[df[column] == unique_value]
    output_path = os.path.join(output_dir, f'{unique_value}.xlsx')
    df_output.to_excel(output_path, sheet_name=unique_value, index=False)
