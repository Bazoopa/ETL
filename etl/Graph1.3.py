import matplotlib.pyplot as plt

from data_processors.DataProcessor1_3 import DataProcessor1_3

'''
============================
Data Frame creation
============================
'''

# Specify the CSV file from which to extract data
fileName = "data/modern-renewable-energy-consumption.csv"

# Specify dictionary for renaming columns
column_names = {
    'Other renewables (including geothermal and biomass) electricity generation - TWh': 'Other',
    'Solar generation - TWh': 'Solar',
    'Wind generation - TWh': 'Wind',
    'Hydro generation - TWh': 'Hydro'
}

# Define the global scope (i.e., the world) for data extraction
entities = ['World']

data_processor = DataProcessor1_3(fileName, column_names, entities)
data_processor.load_data("CSVsExtracted/Graph1.3-CSV")



'''
============================
Graph Plotting
============================
'''

df = data_processor.processed_data

# Specify the labels and colors for the pie chart
labels = ['Other', 'Hydro']
colors = ['#be4d23', '#2394be']


# Plot the data as a pie chart
df.plot(kind='pie', labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors=colors,
        wedgeprops={'linewidth': 0.8, 'edgecolor': 'white'})
plt.title('Distribution of renewable Energy sources in the world in 1965')
plt.ylabel('')  # omit the default 'None' ylabel

# Display the generated plot
plt.show()

# Optionally, use Loader to save the transformed DataFrame back to a new CSV file
# Uncomment the line below and specify 'outputFileName' to do so
# Loader.toCSV(outputFileName, df)