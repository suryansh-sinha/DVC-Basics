import pandas as pd
import os

data = {'Name': ['Alice', 'Bob', 'Adam'],
        'Age': [25, 30, 35],
        'City': ['Chicago', 'Amsterdam', 'New Jersey']}

df = pd.DataFrame(data)

# Adding new data
new_row_loc = {'Name':'V2', 'Age': 20, 'City': 'Kanpur'}
df.loc[len(df.index)] = new_row_loc

# new_row_loc2 = {'Name':'V3', 'Age': 23, 'City': 'Patna'}
# df.loc[len(df.index)] = new_row_loc2

data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, 'sample_data.csv')
df.to_csv(file_path, index=False)

print(f"CSV file saved to {file_path}")