import pandas as pd
import data_model as dm

# Load the data
data = pd.read_csv(dm.TRAIN_DATA_FILE_PATH)


# Check for leading or trailing whitespaces in column names
data.columns = data.columns.str.strip()

# categorize the 'age' column:
column_name = dm.TableColumns.AGE

if column_name not in data.columns:
    raise ValueError(f"Column '{column_name}' not found in the data.")

column_age_counts = data[column_name].value_counts()

ages = column_age_counts.to_dict()

# hold row data for chart
rows = []

total_occupations = sum(ages.values())


for occupation, count in ages.items():
    rows.append((occupation, count))



