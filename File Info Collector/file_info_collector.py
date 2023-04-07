
import pandas as pd
import os


paths = (
    "path\\to\\directory\\1\\",
    "path\\to\\directory\\2\\"
)


def main():
    df = create_df()
    df = get_file_info(df, paths)
    df.to_excel("path\\to\\export\\file_names_sizes.xlsx")


def create_df():
    df = pd.DataFrame({
        "file_name":[],
        "file_size (bytes)":[],
        "directory":[]
    })

    return df


def get_file_info(df, paths):
    
    for path in paths:
        dir_name = path

        # List of files in given directory
        dir_files = os.listdir(path)

        for file in dir_files:
            # Get file name, size and corresponding directory
            df.loc[len(df)] = [file, os.stat(os.path.join(path, file)).st_size, dir_name]
    
    return df
        

if __name__ == "__main__":
    main()
