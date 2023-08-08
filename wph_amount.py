import pandas as pd
from h2o_wave import ui, data

# Load the data into a DataFrame
data = pd.read_csv('census_data.csv')

# Check for leading or trailing whitespaces in column names
data.columns = data.columns.str.strip()

# Categorize the 'age' column:
column_name = 'age'

if column_name not in data.columns:
    raise ValueError(f"Column '{column_name}' not found in the data.")

column_4_counts = data[column_name].value_counts()

# Convert the counts to a dictionary
occupations = column_4_counts.to_dict()

# Create an empty list to hold the pie data
rows = []

# Calculate the total count of all occupations
total_occupations = sum(occupations.values())

# Count occurrences of amount <=50K and >50K based on age groups


    #rows.append((f'G1', '<=50K', f'P{p_counter}', 4))
    #rows.append((f'G2', '>50K', f'P{p_counter}', 4))

total_rows = data.shape[0]


arr_h= [5 for i in range(100)]
arr_l= [5 for i in range(100)]

for index, row in data.iterrows():
    if row[14].__contains__('>'):
        arr_h[row[12]]=arr_h[row[12]]+1
    else:
        arr_l[row[12]]=arr_l[row[12]]+1


for i in range(5,len(arr_l)):
    rows.append(('G1', '>50K', str(i), arr_h[i]))
    rows.append(('G2', '<=50K', str(i), arr_l[i]))


# Add the individual occupation counts
for occupation, count in occupations.items():
    #rows.append(('P1', 'USA', occupation, count))
    #rows.append(('P2', 'China', occupation, count))
    pass

print(arr_h)

