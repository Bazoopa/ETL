from etl.data_processors.DataProcessor import DataProcessor
from etl.transformer.Transformer import Transformer


class DataProcessor2_0(DataProcessor):

    def __init__(self, file_name, column_names):
        super().__init__(file_name)
        self.column_names = column_names
        self.processed_data = self.process_data()

    def process_data(self):
        df = Transformer.change_header_names(self.data, self.column_names)
        df = Transformer.delete_column(df, "Code")

        # @Todo: if I have time I could add this to the transformer class?
        # Select only the necessary columns
        df = df[['Entity', 'Year', 'Average Temp', 'Upper Bound', 'Lower Bound']]

        # Filter the data to include only years between 1965 and 2022
        df = Transformer.filter_by_year_range(df, 'Year', 1965, 2022)

        self.df = df

        # Todo: I should probably have transforming done in a seperate method because it's not returning a dataFrame format.
        # @todo: May need to add an entity, will have a think
        # @Todo: if I have time I could add this to the transformer class?
        # Select only rows where 'Entity' equals to 'Global'
        df = df[df['Entity'] == 'Global'].groupby("Entity")

        return df
