from etl.data_processors.DataProcessor import DataProcessor
from etl.transformer.Transformer import Transformer


class DataProcessor2_1(DataProcessor):

    def __init__(self, file_name, entities):
        super().__init__(file_name)
        self.entities = entities
        self.processed_data = self.process_data()

    def process_data(self):
        # @todo, entities isn't actually doing anything right now, need to change this.
        df = Transformer.delete_column(self.data, "Code")
        df = Transformer.select_years(df, 'Year', [1990, 2019])
        df = Transformer.filter_by_entity(df, 'Entity', ['World'])
        df = Transformer.delete_column(df, "Entity")

        # @todo: could add these to the Transformer class
        df = df.set_index('Year')
        df = df.transpose()
        df = df.sort_values(by=[2019], ascending=True)
        self.df = df
        # Clean data labels by removing the repeated end of the strings from the index labels
        df.rename(index=lambda x: str(x)[:-29], inplace=True)

        return df
