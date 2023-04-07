This code reads CSV files from directories specified in a list of paths. It replaces specific values in the CSV files with new values specified in a dictionary. The user can choose whether to replace full or partial matches of the values.

The replace_dict dictionary contains the old values as keys and the new values as values. The paths list contains the paths to the directories that contain the CSV files to be modified.

The main function loops over each path in the paths list and gets a list of files in the directory using os.listdir. For each file that ends with ".csv", it reads the CSV file into a pandas DataFrame using pd.read_csv, then calls the replace_values_full function to replace the values in the DataFrame. Finally, the modified DataFrame is written back to the CSV file using df.to_csv.

The replace_values_full function loops over each column in the DataFrame and uses regular expressions to replace the old values with new values, using the replace method of the DataFrame.

There is also a replace_values_partial function that replaces partial matches of the old values in the DataFrame.