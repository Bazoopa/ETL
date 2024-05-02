import matplotlib.pyplot as plt

from data_processors.DataProcessor1_1 import DataProcessor1_1

'''
============================
Data Frame creation
============================
'''

# Define source file to extract data from
fileName = "data/primary-energy-cons.csv"

# Define column renaming dictionary where current column names are keys and new column names are values
column_names = {
    'Primary energy consumption (TWh)': 'Energy Consumption'
}

# Set up the entity on which to focus analysis. In this case we are focusing on the 'World'
entities = ['World']

data_processor = DataProcessor1_1(fileName, column_names, entities)
data_processor.load_data("CSVsExtracted/Graph1.1-CSV")


'''
============================
Graph Plotting
============================
'''

df = data_processor.processed_data

# For each group (here only 'World'), plot the trend of energy consumption over the years
for name, group in df:
    plt.plot(group['Year'], group['Energy Consumption'], label=name)

# Set graph title, labels, add grid and legend
plt.title('Amount of energy produced in the world from 1965 - 2022', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Energy Generated (TWh)', fontsize=12)
plt.grid(True)
plt.legend(loc='upper left')

# Display the plot
plt.show()

# The Loader can also be used to save the transformed DataFrame back to a CSV file
# In future use, provide the name of output file
# Loader.toCSV(outputFileName, df)