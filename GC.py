#!/usr/bin/python

"""
The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.

DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.

In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.
"""


import sys
import re

dataIn = open(sys.argv[1],'r')
dataIn = open('/Users/akiko/Downloads/rosalind_gc.txt','r')
text = dataIn.read()
dataIn.close()

#text = '>Rosalind_6404\nCCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC\nTCCCACTAATAATTCTGAGG\n>Rosalind_5959\nCCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT\nATATCCATTTGTCAGCAGACACGC\n>Rosalind_0808\nCCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC\nTGGGAACCTGCGGGCAGTAGGTGGAAT'

textList = re.split(">", text)
GCcountList = []
GCstringList = []
for m in textList:
    if len(m) > 0:
        m2 = re.sub('Rosalind_\w*|\n', '',m)
        #print m2

        for m3 in re.finditer('Rosalind_\w*', m):
            GCcountList.append(float(len(re.findall('G|C',m)))/float(len(re.findall('A|T|G|C',m)))*100)
            GCstringList.append(m[m3.start():m3.end()])

GCcountList = map(float, GCcountList)
maxIdx = GCcountList.index(max(GCcountList))

print GCstringList[maxIdx]
print round(max(GCcountList),6)




