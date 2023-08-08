import pandas as pd
import data_model as dm

# Load the data
data = pd.read_csv(dm.TRAIN_DATA_FILE_PATH)

# Check for leading or trailing whitespaces in column names
data.columns = data.columns.str.strip()

# Categorize the 'age' column:
column_name = dm.TableColumns.AGE

if column_name not in data.columns:
    raise ValueError(f"Column '{column_name}' not found in the data.")

column_age_counts = data[column_name].value_counts()
ages = column_age_counts.to_dict()

# Hold the rows data
rows = []

# total count of all ages
total_occupations = sum(ages.values())

total_rows = data.shape[0]

# store total count of 50K> for each age groups
arr_h= [10 for i in range(92)]

# store total count of <=50K for each age groups
arr_l= [10 for j in range(92)]

for index, row in data.iterrows():
    if row[14].__contains__('>'):
        arr_h[row[0]]=arr_h[row[0]]+1
    else:
        arr_l[row[0]]=arr_l[row[0]]+1


for i in range(10,len(arr_l)):
    rows.append(('G1', '>50K', str(i), arr_h[i]))
    rows.append(('G2', '<=50K', str(i), arr_l[i]))



