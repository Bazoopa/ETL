import matplotlib.pyplot as plt

from data_processors.DataProcessor2_1 import DataProcessor2_1

'''
============================
Data Frame creation
============================
'''

# Specify the CSV file to extract data from
fileName = "data/number-of-deaths-by-risk-factor.csv"

# Define the global scope (i.e., the world) for data extraction
entities = ['World']

data_processor = DataProcessor2_1(fileName, entities)
data_processor.load_data("CSVsExtracted/Graph2.1-CSV")

'''
============================
Graph Plotting
============================
'''

df = data_processor.processed_data

# Plot the DataFrame as a horizontal bar plot
df.plot(kind='barh', figsize=(10, 20), width=0.8, color=['#d25f2d', '#2da0d2'])

# Set the title for the plot and the label for the x-axis
plt.title('Number of deaths attributed to various risk factors in 1990 and 2019 (World)')
plt.xlabel('Number of Deaths')

# Show grid for better visualization and display the plot
plt.grid(True)
plt.show()
