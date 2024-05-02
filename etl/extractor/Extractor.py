import pandas as pd


class Extractor:
    @staticmethod
    def fromCSV(file_path: str) -> pd.DataFrame:
        """
        Function to read a CSV file and convert it into a pandas DataFrame.
        Args:
            file_path: A string representing the path of the csv file.
        Returns:
            A pandas DataFrame representing the data loaded from the CSV file.
        """
        data = pd.read_csv(file_path)
        data.columns = data.columns.astype(str)
        return data

    # @todo, add fromJson, although none of my data is JSON.