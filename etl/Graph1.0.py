import matplotlib.pyplot as plt
from data_processors.DataProcessor1_0 import DataProcessor1_0

'''
============================
Data Frame creation
============================
'''

# Define the location and filename of the input CSV data file
fileName = "data/renewable-share-energy.csv"

# Set up a renaming dictionary where the current column name is the key and the new column name is the value
column_names = {
    'Renewables (% equivalent primary energy)': 'Renewables'
}

# Define the list of entities to consider for analysis
entities = ['North America', 'South America', 'Oceania', 'Europe', 'Asia', 'Africa']

data_processor = DataProcessor1_0(fileName, column_names, entities)
data_processor.load_data("CSVsExtracted/Graph1.0-CSV")

'''
============================
Graph Plotting
============================
'''

df = data_processor.processed_data

# For each group (i.e., for each 'Entity'), plot the trend of renewable energy over the years
for name, group in df:
    plt.plot(group['Year'], group['Renewables'], label=name)

# Add title, labels, and legend to the plot
plt.title('Proportion of renewable energy consumption across continents from 1965 - 2022', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Renewable energy consumption (%)', fontsize=12)
plt.grid(True)
plt.legend()

# Display the plot
plt.show()
