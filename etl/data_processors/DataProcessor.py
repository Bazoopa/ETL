import pandas as pd
from etl.extractor import Extractor


class DataProcessor:

    def __init__(self, file_name):
        self.file_name = file_name
        self.data = self.extract_data()
        self.df = pd.DataFrame()

    def extract_data(self):
        # @todo: It would be cool to add the functionality here so that it doesn't matter whether you input a CSV or a JSON file, the method can just deal with both.
        return Extractor.Extractor.fromCSV(self.file_name)

    # @todo: change this so that it uses the Loader Class methods.
    def load_data(self, csv_file_name):
        self.df.to_csv(csv_file_name)
