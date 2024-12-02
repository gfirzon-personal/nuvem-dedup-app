import os
#import csv
import uuid
from datetime import datetime
import pandas as pd
from pandas import DataFrame
from pprint import pprint

def load(file_path) -> DataFrame:
    df = pd.read_csv(file_path)
    return df

# def count_records_in_csv(file_path):
#     with open(file_path, mode='r', newline='') as file:
#         reader = csv.reader(file)
#         record_count = sum(1 for row in reader) - 1  # Subtract 1 for the header row
#     return record_count


def get_column_names(df: DataFrame):
    return df.columns.tolist()

if __name__ == "__main__":
    # Get current date and time in timestamp format
    current_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    print(f"Process started (UTC): {current_timestamp}")

    file_path = './_data/generated_batch_sample.csv'

    # Extract just the file name from the file path
    file_name = os.path.basename(file_path)

    df: DataFrame = load(file_path)
    column_names = get_column_names(df)

    # Generate a GUID
    guid = uuid.uuid4()

    print(f"File name: {file_name}")
    print(f"Number of records: {len(df)}")
    print(f"File GUID: {guid}")

    print("Column names:")
    pprint(column_names)