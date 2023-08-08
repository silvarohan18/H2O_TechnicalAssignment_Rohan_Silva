import pandas as pd
from h2o_wave import ui, data

data = pd.read_csv('test.csv')
subset_df = data.head(100)

# Create columns for table.
width = '100'
column = [
    ui.table_column(name='age', label='Age', sortable=True, searchable=True, max_width=width, cell_overflow='wrap'),
    ui.table_column(name='work', label='Work', sortable=True, searchable=True, max_width=width, cell_overflow='wrap'),
    ui.table_column(name='fnlwgt', label='F Weight', sortable=True, searchable=True, max_width=width,
                    cell_overflow='wrap'),
    ui.table_column(name='education', label='Education', sortable=True, searchable=True, max_width='200',
                    cell_overflow='wrap'),
    ui.table_column(name='education-num', label='Education-Num', sortable=True, searchable=True, max_width='200',
                    cell_overflow='wrap'),
    ui.table_column(name='marital-status', label='Marital Status', sortable=True, searchable=True, max_width='200',
                    cell_overflow='wrap'),
    ui.table_column(name='occupation', label='Occupation', sortable=True, searchable=True, max_width=width,
                    cell_overflow='wrap'),
    ui.table_column(name='relationship', label='Relationship', sortable=True, searchable=True, max_width=width,
                    cell_overflow='wrap'),
    ui.table_column(name='race', label='Race', sortable=True, searchable=True, max_width=width, cell_overflow='wrap'),
    ui.table_column(name='sex', label='Sex', sortable=True, searchable=True, max_width=width, cell_overflow='wrap'),
    ui.table_column(name='capital-gain', label='Capital-Gain', sortable=True, searchable=True, max_width='200',
                    cell_overflow='wrap'),
    ui.table_column(name='capital-loss', label='Capital-Loss', sortable=True, searchable=True, max_width='200',
                    cell_overflow='wrap'),
    ui.table_column(name='hour-per-week', label='Hour-Per-Week', sortable=True, searchable=True, max_width='200',
                    cell_overflow='wrap'),
    ui.table_column(name='native-country', label='Native-Country', sortable=True, searchable=True, max_width='200',
                    cell_overflow='wrap'),
    ui.table_column(name='amount', label='amount', sortable=True, searchable=True, max_width=width,
                    cell_overflow='wrap'),

]
