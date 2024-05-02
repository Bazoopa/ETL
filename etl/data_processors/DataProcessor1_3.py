from etl.data_processors.DataProcessor import DataProcessor
from etl.transformer.Transformer import Transformer


class DataProcessor1_3(DataProcessor):

    def __init__(self, file_name, column_names, entities):
        super().__init__(file_name)
        self.column_names = column_names
        self.entities = entities
        self.processed_data = self.process_data()

    def process_data(self):

        df = Transformer.change_header_names(self.data, self.column_names)
        df = Transformer.delete_column(df, "Code")
        df = Transformer.select_years(df, 'Year', [1965])

        #@todo: this might need changing
        # Select the data for the 'World' entity
        df = Transformer.filter_by_entity(df, 'Entity', ['World'])

        # Delete irrelevant columns for pie chart plotting
        # toDO: I think this could be altered to make it clearer, will think of solution later.
        columns_to_delete = ['Entity', 'Year', 'Solar', 'Wind']
        for column in columns_to_delete:
            df = Transformer.delete_column(df, column)

        self.df = df

        # Select the first row only and transpose the DataFrame for pie chart data
        df = df.iloc[0].T
        # Update the dataframe attribute so that I can load the dataframe as a CSV

        return df
