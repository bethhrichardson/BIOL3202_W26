#!/usr/bin/env python3
##Tells the computer this is python code

input_file = "variants.csv"
##Name of the input CSV file

output_file = "variants_with_domain.csv"
##Name of the output CSV file

infile = open(input_file, "r")
##Open the input file in read mode; prevents the raw data from being edited

outfile = open(output_file, "w")
##Open the output file in write mode

header = infile.readline().strip()
##Read the first line (the header) and remove the trailing newline character (these can mess with python list functions)

outfile.write(header + ",domain\n")
##Write the original header plus a new column name called "domain"

for line in infile:
##Loop over each remaining line in the input file

    line = line.strip()
##Remove trailing newline characters

    fields = line.split(",")
##Split the line into a list of columns using commas

    aa_position = int(fields[1])
##Convert the second column (aa_position) to an integer

    if aa_position >= 1 and aa_position <= 58:
        domain = "oligomerisation"
##Assign oligomerisation domain to any variants between amino acids 1 and 58
    elif aa_position >= 59 and aa_position <= 437:
        domain = "catalytic"
##Assign catalytic domain domain to any variants between amino acids 59 and 437
    elif aa_position >= 438 and aa_position <= 574:
        domain = "allosteric"
##Assign allosteric domain to any variants between amino acids 438 and 574
    else:
        domain = "unknown"
##Assign unknown if number is outside expected range

    outfile.write(line + "," + domain + "\n")
##Write the original line plus the new domain value

infile.close()
# Close the input file

outfile.close()
# Close the output file