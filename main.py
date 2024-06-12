import pandas as csv_reader
import os
import math

file_path = r'credentials.csv'

sector_column = 'Sector'
faction_column = 'Faction'
key_a_column = 'Key A'
key_b_column = 'Key B'


def generate_key():
    return os.urandom(6).hex()

def open_csv():
    return csv_reader.read_csv(file_path)

def generate_all_keys():
    data = open_csv()
    key_b = generate_key()
    for index, row in data.iterrows():
        if not is_nan_or_string(data, row.at[faction_column]):
            key_a = generate_key()
            data.at[index, key_a_column] = key_a
            data.at[index, key_b_column] = key_b
    
    data.to_csv('credentials_updated.csv', index=False)

def is_nan_or_string(data, value):
    # Check if the value is a string
    if isinstance(value, str):
        return False
    # Check if the value is NaN
    if math.isnan(value):
        return True
    # Otherwise, consider it not NaN
    return False


generate_all_keys()