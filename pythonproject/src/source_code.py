import pandas

def descriptive_statistics(data):
    """
    Calculate descriptive statistics for a DataFrame.

    Parameters:
    data (pd.DataFrame): The input DataFrame containing numeric data.

    Returns:
    pd.DataFrame: A DataFrame containing descriptive statistics.
    """
    return data.describe()

if __name__ == "__main__":
    # Remove unused imports
    # import os
    # import sys

    # Read the CSV file
    data_sample = pandas.read_csv("pythonproject/src/data/spotify-2023.csv", encoding="ISO-8859-1")

    # Print descriptive statistics
    print(descriptive_statistics(data_sample))
