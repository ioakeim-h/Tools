import pandas as pd
import tabula
import os

import warnings
warnings.filterwarnings("ignore")

input_dir = "..."
tabula.convert_into_by_batch(input_dir, output_format="csv", pages="all")

column_names = ["..."]
df = pd.DataFrame(columns = column_names)

# Multiple pdf files into one csv
csv_files = os.listdir("...")

for csv in csv_files:
    csv = pd.read_csv(f"...{csv}", names = column_names)

    df = df.append(csv, ignore_index=True)


df.to_csv("...")