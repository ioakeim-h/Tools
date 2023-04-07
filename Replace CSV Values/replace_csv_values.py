import os
import pandas as pd


def main():
    replace_dict = {
        r"\bValue 1\b": "New Value 1",
        r"\bValue 2\b": "New Value 2"
    }
    paths = [
        "path/to/directory/1/",
        "path/to/directory/2/"
    ]
    for path in paths:
        dir_files = os.listdir(path)
        for file in dir_files:
            if file[-4:] == ".csv":
                file_path = os.path.join(path, file)
                df = pd.read_csv(file_path, low_memory=False)

                # Choose to replace full or partial
                df = replace_values_full(df, replace_dict)
                df.to_csv(file_path, index=False)
            else:
                print(f"{file} skipped")


def replace_values_full(df, replace_dict):
    for col in df:
        # Replace values using regular expressions to match full words only
        df[col].replace(replace_dict, regex=True, inplace=True)
    return df


def replace_values_partial(df, replace_dict):
    for col in df:
        # Replace values (includes partial matches)
        df[col].replace(replace_dict, inplace=True)
    return df


if __name__ == "__main__":
    main()
