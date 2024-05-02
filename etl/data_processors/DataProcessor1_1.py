from etl.data_processors.DataProcessor import DataProcessor
from etl.transformer.Transformer import Transformer


class DataProcessor1_1(DataProcessor):

    def __init__(self, file_name, column_names, entities):
        super().__init__(file_name)
        self.column_names = column_names
        self.entities = entities
        self.processed_data = self.process_data()

    def process_data(self):
        df = Transformer.change_header_names(self.data, self.column_names)
        df = Transformer.delete_column(df, "Code")
        df = Transformer.filter_by_entity(df, "Entity", self.entities)
        # Update the dataframe attribute so that I can load the dataframe as a CSV
        self.df = df

        # Todo: I should probably have transforming done in a seperate method because it's not returning a dataFrame format.
        df = Transformer.group_by(df, "Entity")

        return df
