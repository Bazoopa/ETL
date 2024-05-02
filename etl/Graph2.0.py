import matplotlib.pyplot as plt

from data_processors.DataProcessor2_0 import DataProcessor2_0

'''
============================
Data Frame creation
============================
'''

# Define the source data file
fileName = "data/temperature-anomaly.csv"

# Specify a dictionary to rename the columns. The keys are the old names and the values are the new names
column_names = {
    'Global average temperature anomaly relative to 1961-1990': 'Average Temp',
    'Upper bound of the annual temperature anomaly (95% confidence interval)': 'Upper Bound',
    'Lower bound of the annual temperature anomaly (95% confidence interval)': 'Lower Bound'
}

data_processor = DataProcessor2_0(fileName, column_names)
data_processor.load_data("CSVsExtracted/Graph2.0-CSV")

'''
============================
Graph Plotting
============================
'''
df = data_processor.processed_data

# Create a subplot for the csv
fig, ax = plt.subplots()

# For each group (in this case, only 'Global'), plot the temperature anomaly data (average, upper and lower bounds) over years
for name, group in df:
    group.plot(x='Year', y='Average Temp', ax=ax, label='Average Temp')
    group.plot(x='Year', y='Upper Bound', ax=ax, label='Temperature Upper Bound')
    group.plot(x='Year', y='Lower Bound', ax=ax, label='Temperature Lower Bound')

# Set the label for y-axis, activate grid, set the graph title, and display the legend
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.title('Average temperature of the world between 1965 - 2022')
plt.legend()

# Display the plot
plt.show()
