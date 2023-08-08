import pandas as pd
from h2o_wave import ui, data

import random

def generate_random_color():
    """
    Generate a random color in hexadecimal format.

    Returns:
        str: Random color in the format '#RRGGBB', where RR, GG, and BB are two-digit hexadecimal values for red, green, and blue channels.
    """
    # Generate random values for red, green, and blue channels
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    # Convert the values to hexadecimal and format the color string
    color_hex = "#{:02x}{:02x}{:02x}".format(r, g, b)

    return color_hex

# Load the data into a DataFrame
data = pd.read_csv('census_data.csv')


# Check for leading or trailing whitespaces in column names
data.columns = data.columns.str.strip()

# categorize the 'occupation' column:
column_name = 'occupation'

if column_name not in data.columns:
    raise ValueError(f"Column '{column_name}' not found in the data.")

column_4_counts = data[column_name].value_counts()

# Convert the counts to a dictionary
occupations = column_4_counts.to_dict()

# Create an empty list to hold the pie data
rows = []


# Calculate the total count of all occupations
total_occupations = sum(occupations.values())

# Iterate through the occupations dictionary and create pie data for each category
for occupation, count in occupations.items():
    label = occupation
    # Calculate the percentage of each occupation based on the total count
    fraction = count / total_occupations
    # Format the percentage to show two decimal places
    percentage_str = f'{fraction:.2%}'
    # Create pie data for each occupation
    pie_data = ui.pie(label=label, value='', fraction=fraction, color=generate_random_color(), aux_value=f'{count}'+' ('+ percentage_str +')')
    # Append the pie data to the pies list

    row_data = (label,count)

    rows.append(row_data)


