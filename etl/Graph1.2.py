import matplotlib.pyplot as plt

from data_processors.DataProcessor1_2 import DataProcessor1_2

'''
============================
Data Frame creation
============================
'''

# Specify the CSV file from which to load data
fileName = "data/renewable-share-energy.csv"

# Specify the dictionary for renaming columns,
# i.e., map old column names to new ones
column_names = {
    'Renewables (% equivalent primary energy)': 'Renewables'
}

# Define entities (continents) to be considered for the analysis
entities = ['North America', 'South America', 'Oceania', 'Europe', 'Asia', 'Africa']

data_processor = DataProcessor1_2(fileName, column_names, entities)
data_processor.load_data("CSVsExtracted/Graph1.2-CSV")

'''
============================
Graph Plotting
============================
'''

df = data_processor.processed_data

# Create a bar chart for each entity on energy consumption in 1965 and 2022
df.plot(kind='bar', color=['#d25f2d', '#2da0d2'])
plt.xlabel('Entity')
plt.ylabel('Primary Energy')
plt.title('Proportion of renewable energy consumption across continents in 1965 and 2022')

# Show the grid in the plot and display the plot
plt.grid(True)
plt.show()

# Optionally, we can save the transformed DataFrame as a new CSV file
# (to use, uncomment the line below and provide the 'outputFileName')
# Loader.toCSV(outputFileName, df)
