#!/usr/bin/python

"""Problem

A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s."""

import sys

dataIn = open(sys.argv[1],'r')

nA = 0
nT = 0
nC = 0
nG = 0
for i in dataIn.read():
    if i == 'A':
        nA = nA + 1
    elif i == 'T':
        nT = nT + 1
    elif i == 'C':
        nC = nC + 1
    elif i == 'G':
        nG = nG + 1

print '%i %i %i %i \n' %(nA, nC, nG, nT)

dataIn.close()
