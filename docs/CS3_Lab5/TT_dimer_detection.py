#!/usr/bin/env python3
##This line tells the computer to use python3 to run this code

import sys
##sys is a python package that makes using file inputs much easier

filename = sys.argv[1]
##This tells the script to use the first argument passed to it as the input filename

dna = ""
##This creates an empty string that we can add to later (this is called "initalizing" an object)

with open(filename, "r") as f:
##This opens the file in read-only ("r") mode
    for line in f:
##This takes every line in the file one by one
        line = line.strip()   
##This removes any newline characters so the string will only contain base pairs
        if not line.startswith(">"):   
            dna += line        
##This makes sure header lines (lines starting with ">" are not counted), and any other lines are appended to the empty dna string

dna = dna.upper()
##This converts the complete DNA string to uppercase, which makes the count easier as we don't have to make everything case insensitive

tt_count = 0
##This initializes an integer value for our TT count, starting at 0

for i in range(len(dna) - 1):
##This considers each character in the string one by one, except for the last character because that can't be followed by anything
    if dna[i] == "T" and dna[i+1] == "T":
##This statement checks whether the current character is a T and, if so, whether the next character is a T
        tt_count += 1
##This iteratively increases our count for every TT dimer identified
    else:
        pass
##This statement tells the script to move onto the next character if the current character doesn't meet the requirements

percent_tt = (tt_count / (len(dna)-1))*100
##This statement converts the raw number of TT pairs into a percentage of the overall number of pairs in the genome (sequence length -1)

print("Percentage of TT dimers:", round(percent_tt, 2))
##This returns to the terminal the percentage of identified TT dimers, rounded to two decimal places.