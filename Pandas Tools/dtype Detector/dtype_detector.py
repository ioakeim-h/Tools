# VECTORIZED VERSION

import pandas as pd
import numpy as np
import re

# Compile regular expressions
REGX = re.compile(r"^[-+]?(?:(?:\d+ |\d*[,\.])?\d+(?:[Ee][-+]?(?:\d+|\d+\/\d+|\d*[,\.]\d+)|[,\.]\d+(?:[,\.]\d+)?)?|\d+\/\d+)$")
REGX_FRONT = re.compile(REGX.pattern[0] + "\D+" + REGX.pattern[1:])
REGX_END = re.compile(REGX.pattern[:-1] + "\D+" + REGX.pattern[-1])

def find_numeric(data):
    if not isinstance(data, pd.Series):
        raise TypeError(f"Input data must be a pandas Series not {type(data)}")
    if not pd.api.types.is_object_dtype(data):
        raise TypeError(f"Series {data.name} must be of the object data type")

    # Get boolean mask for non-NaN values
    notna = pd.notna(data)
    
    # Apply regular expressions to non-NaN values
    numeric_mask = notna & data.str.match(REGX)
    ambiguous_mask = notna & ~numeric_mask & ((data.str.match(REGX_FRONT) | data.str.match(REGX_END)))
    
    numeric_values = data[numeric_mask].unique()
    ambiguous_values = data[ambiguous_mask].unique()

    print(f"numeric: {len(numeric_values)}\nambiguous: {len(ambiguous_values)}\nother: {notna.sum() - (len(numeric_values) + len(ambiguous_values))}")
    print("\nDuplicates were not considered in the above output.")
        
    # Return subsets for numeric, ambiguous and string values
    return data[numeric_mask], data[ambiguous_mask], data[~numeric_mask & ~ambiguous_mask]


##############################################################################################################################
# OLD VERSION

# import pandas as pd
# from pandas.api.types import is_object_dtype
# import numpy as np
# import re


# def find_numeric(data):
#     if not isinstance(data, pd.Series):
#         raise TypeError(f"Input data must be a pandas Series not {type(data)}")
#     if not is_object_dtype(data):
#         raise TypeError(f"Series {data.name} must be of the object data type")
    
#     unique_values = tuple(data.dropna().unique())
#     numeric_values, ambiguous_values = exhaustive_search(unique_values)

#     print(f"numeric: {len(numeric_values)}\nambiguous: {len(ambiguous_values)}\nother: {len(unique_values) - (len(numeric_values) + len(ambiguous_values))}")
#     print("\nDuplicates were not considered in the above output.")
        
#     # Return subsets for numeric, ambiguous and string values
#     return data[data.isin(numeric_values)], data[data.isin(ambiguous_values)], data[~data.isin(numeric_values) & ~data.isin(ambiguous_values)]
    

# def exhaustive_search(unique_values):
#     # Numeric values 
#     regx = re.compile(r"^[-+]?(?:(?:\d+ |\d*[,\.])?\d+(?:[Ee][-+]?(?:\d+|\d+\/\d+|\d*[,\.]\d+)|[,\.]\d+(?:[,\.]\d+)?)?|\d+\/\d+)$") # previous regx = r"^(?:[-+]?)(?:\d+|\d*[,\.]\d+)(?:[Ee][-+]?\d+)?|\d+/[1-9]\d*$"
#     # non-numeric at front (e.g. '$50')
#     regx_front = re.compile(regx.pattern[0] + "\D+" + regx.pattern[1:])
#     # non-numeric at end (e.g. '50p')
#     regx_end = re.compile(regx.pattern[:-1] + "\D+" + regx.pattern[-1])

#     numeric_values = tuple(val for val in unique_values if isinstance(val, str) and regx.match(val))
#     ambiguous_values = tuple(val for val in unique_values if val not in numeric_values and isinstance(val, str) and (regx_front.search(val) or regx_end.search(val)))
#     # ambiguous_values = tuple(val for val in unique_values if val not in numeric_values and isinstance(val, str) and (regx.match(val) or regx_front.search(val) or regx_end.search(val)))

#     return numeric_values, ambiguous_values