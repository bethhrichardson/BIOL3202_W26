#!/usr/bin/env python3
##Tells the computer this is python code

import sys
##A package that allows us to enter file names as arguments

seq = ""
##Initializes the sequence string that will be analysed later so content from the file can be added to it

with open(sys.argv[1]) as file:
##Opens the input fasta file and feeds it to the for loop below
    for line in file:
##Runs the code below under every line in the fasta file
        if not line.startswith(">"):
##Ensures any fasta headers are not included in the GC analysis
            seq += line.strip().upper()
##Adds the nucleotide information from each line to the sequence string

gc = seq.count("G") + seq.count("C")
##Counts the number of times G and C appear in the sequence string
gc_percent = (gc / len(seq)) * 100
##Calculates the percentage of overall characters in the sequence string (calculated as the overall length of the string) are GC

print(f"{gc_percent:.2f}%")
##Prints the result