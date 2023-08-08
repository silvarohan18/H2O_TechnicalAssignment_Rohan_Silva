import pandas as pd
import data_model as dm


data = pd.read_csv(dm.TRAIN_DATA_FILE_PATH)


# Check for leading or trailing whitespaces in column names
data.columns = data.columns.str.strip()

column_name = dm.TableColumns.EDUCATION

if column_name not in data.columns:
    raise ValueError(f"Column '{column_name}' not found in the data.")

column_edu_counts = data[column_name].value_counts()

educations = column_edu_counts.to_dict()

# hold row data
rows = []


total_educations = sum(educations.values())


for occupation, count in educations.items():
    label = occupation
    row_data = (label,count)

    rows.append(row_data)


