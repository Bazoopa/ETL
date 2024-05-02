import pandas as pd


class Loader:
    @staticmethod
    def toCSV(file_path: str, df: pd.DataFrame):
        """
        Function to write the DataFrame to a CSV file.
        Args:
            file_path: The string file path where the new csv file will be saved.
            df : The pandas DataFrame that you want to write.
        """
        df.to_csv(file_path, index=False)
