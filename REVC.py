#!/usr/bin/python

"""
The Secondary and Tertiary Structures of DNAclick to expand

Problem

In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.
"""

# read in data
import sys

dataIn = open(sys.argv[1],'r')
text = dataIn.read()

# reverse input text
text2 = []
for i in range(len(text)-1,-1,-1):
    if text[i] == 'A':
        text2.append('T')
    elif text[i] == 'T':
        text2.append('A')
    elif text[i] == 'C':
        text2.append('G')
    elif text[i] == 'G':
        text2.append('C')

# convert from list to string
text2= ''.join(text2)

dataIn.close()

# now write it out
out = open('Q3out.txt', 'w')
for i in text2:
    out.write('%s' %i)
out.close()
