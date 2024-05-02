from typing import List

import pandas as pd
from pandas.core.groupby import DataFrameGroupBy

# @todo, add a method that uses map or reduce etc just so I've covered it somwhere. An exmaple of doing this with Pandas can be found at this youtube Link: https://www.youtube.com/watch?v=uqRRjcsUGgk
class Transformer:
    @staticmethod
    def change_header_names(data: pd.DataFrame, column_names: dict) -> pd.DataFrame:
        """
        Function to transform the DataFrame by renaming column headers.
        Args:
            data: A pandas DataFrame that will be transformed.
            column_names: A dictionary where keys are the current column names and values are the new column names.
        Returns:
            A new DataFrame after the transformations.
        """
        df = data.rename(columns=column_names)
        return df

    @staticmethod
    def delete_column(data: pd.DataFrame, column_name: str) -> pd.DataFrame:
        """
        Function to delete a specific column from the DataFrame.
        Args:
            data: A pandas DataFrame from which the column will be deleted.
            column_name: The name of the column to delete.
        Returns:
            The DataFrame after deleting the specified column.
        """
        if column_name in data.columns:
            df = data.drop(columns=column_name)
            return df
        else:
            return data

    @staticmethod
    def filter_by_entity(data: pd.DataFrame, entity_column: str, entities: list) -> pd.DataFrame:
        """
        Function to filter the DataFrame by specific entities.
        Args:
            data: A pandas DataFrame that will be filtered.
            entity_column: The name of the column containing the entities.
            entities: A list of entities to filter by.
        Returns:
            The DataFrame after filtering by specified entities.
        """
        df = data[data[entity_column].isin(entities)]
        return df

    @staticmethod
    def group_by(data: pd.DataFrame, group_column: str) -> DataFrameGroupBy:
        """
        Function to group the DataFrame by a specific column.
        Args:
            data: A pandas DataFrame that will be grouped.
            group_column: The name of the column to group by.
        Returns:
            A GroupBy object after grouping by the specified column.
        """
        grouped_df = data.groupby(group_column)
        return grouped_df

    @staticmethod
    def select_years(data: pd.DataFrame, year_column: str, years: List[int]) -> pd.DataFrame:
        """
        Function to select specific years from the DataFrame.
        Args:
            data: A pandas DataFrame from which years will be selected.
            year_column: The name of the column containing the years.
            years: A list of years to select.
        Returns:
            The DataFrame after selecting the specified years.
        """
        df = data[data[year_column].isin(years)]
        return df

    @staticmethod
    def create_pivot(data: pd.DataFrame, index: str, columns: str, values: str) -> pd.DataFrame:
        """
        Function to create a pivot table from the DataFrame.
        Args:
            data: A pandas DataFrame from which the pivot table will be created.
            index: The name of the column to use as the pivot table index.
            columns: The name of the column to use as the pivot table columns.
            values: The name of the column to use as the pivot table values.
        Returns:
            The pivot table as a DataFrame.
        """
        pivot_df = data.pivot(index=index, columns=columns, values=values)
        return pivot_df

    @staticmethod
    def filter_by_year_range(data: pd.DataFrame, year_column: str, start_year: int, end_year: int) -> pd.DataFrame:
        """
        Function to filter the DataFrame by a range of years.
        Args:
            data: A pandas DataFrame that will be filtered.
            year_column: The name of the column containing the years.
            start_year: The first year of the range.
            end_year: The last year of the range.
        Returns:
            The DataFrame after filtering by the specified year range.
        """
        df = data[(data[year_column] >= start_year) & (data[year_column] <= end_year)]
        return df
