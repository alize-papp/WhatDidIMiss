import re

def parse_date_in_title(title: str):
    date_pattern = "\(\d\d\d\d\)$"
    match = re.search(date_pattern, title)
    if match is None:
        return match
    
    date = match.group()[1:5]
    date = int(date)
    return date

def get_value_for_key(df, key, col_key, col_value):
    found_key = df.loc[df[col_key] == key, col_value].values
    if found_key.shape[0] != 1:
        return None
    
    return found_key[0]