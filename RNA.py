#!/usr/bin/python

"""
Problem

An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.

Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.

"""
# read in data
import sys

dataIn = open(sys.argv[1],'r')
text = dataIn.read()

# replace all incidents of T with U
newText = text.replace('T','U')
dataIn.close()

# now write it out
out = open('Q2out.txt', 'w')
for i in newText:
    out.write('%s' %i)
out.close()


