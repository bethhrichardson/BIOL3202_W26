#!/usr/bin/env python3
##Tells the computer this is python code

import pandas as pd
##Imports the python library pandas, giving it a short nickname (so we don't have to type "pandas" each time)

input_file = "variants.csv"
output_file = "variants_with_domain.csv"
##Define input and output file names

df = pd.read_csv(input_file)
##Read the CSV file into a pandas data frame

df["domain"] = "unknown"
##Create a new column of the data frame called "domain"

df["domain"] = "unknown"
##Make the default value of of the domain column "unknown"

df.loc[(df["aa_position"] >= 1) & (df["aa_position"] <= 58), "domain"] = "oligomerisation"
##Assign oligomerisation domain to any variants between amino acids 1 and 58
df.loc[(df["aa_position"] >= 59) & (df["aa_position"] <= 437), "domain"] = "catalytic"
##Assign catalytic domain domain to any variants between amino acids 59 and 437
df.loc[(df["aa_position"] >= 438) & (df["aa_position"] <= 574), "domain"] = "allosteric"
##Assign allosteric domain to any variants between amino acids 438 and 574

df.to_csv(output_file, index=False)
##Write the updated DataFrame back to a CSV file


