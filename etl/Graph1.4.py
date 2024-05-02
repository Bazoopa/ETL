import matplotlib.pyplot as plt

from data_processors.DataProcessor1_4 import DataProcessor1_4

'''
============================
Data Frame creation
============================
'''

# Specify the CSV file from which the data will be extracted
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

data_processor = DataProcessor1_4(fileName, column_names, entities)
data_processor.load_data("CSVsExtracted/Graph1.4-CSV")

'''
============================
Graph Plotting
============================
'''

df = data_processor.processed_data

# Define the labels and colors for the pie chart

labels = ['Other', 'Solar', 'Wind', 'Hydro']
colors = ['#be4d23', '#beaa23', '#46be23', '#2394be']


# Plot the data as a pie chart
df.plot(kind='pie', labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors=colors,
        wedgeprops={'linewidth': 0.8, 'edgecolor': 'white'})

# Set the title and hide the default 'None' ylabel
plt.title('Distribution of renewable Energy sources in the world in 2022')
plt.ylabel('')

# Display the generated plot
plt.show()

# Optionally, use Loader to save the transformed DataFrame back to a new CSV file
# Uncomment the line below and specify 'outputFileName' to do so
# Loader.toCSV(outputFileName, df)