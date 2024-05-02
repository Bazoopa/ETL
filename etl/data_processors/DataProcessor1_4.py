from etl.data_processors.DataProcessor import DataProcessor
from etl.transformer.Transformer import Transformer


class DataProcessor1_4(DataProcessor):

    def __init__(self, file_name, column_names, entities):
        super().__init__(file_name)
        self.column_names = column_names
        self.entities = entities
        self.processed_data = self.process_data()

    def process_data(self):

        df = Transformer.change_header_names(self.data, self.column_names)
        df = Transformer.delete_column(df, "Code")
        df = Transformer.select_years(df, 'Year', [2022])
        df = Transformer.filter_by_entity(df, 'Entity', ['World'])

        # Delete irrelevant columns for pie chart plotting
        columns_to_delete = ['Entity', 'Year']
        for column in columns_to_delete:
            df = Transformer.delete_column(df, column)

        self.df = df

        # Select the first row only and transpose the DataFrame for pie chart data
        df = df.iloc[0].T

        return df
