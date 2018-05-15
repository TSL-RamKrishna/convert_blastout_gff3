#!/usr/bin/env python3

# program to convert blast output to gff3
import sys
print("##gff-version 3")

blastoutput=sys.argv[1]
blastout=open(blastoutput, 'r')
querylist=[]
for line in blastout:
    linearray=line.split()

    if linearray[0] in querylist:
        counter+=1
    else:
        querylist.append(linearray[0])
        counter=1
    if linearray[0] in linearray[1]:    #strand is  +
        if int(linearray[8]) < int(linearray[9]):
            print(linearray[0] + "\t" + "blast" + "\t" + "CDS" + "\t" + linearray[8] + "\t" + linearray[9] + "\t" + "." + "\t" + "+" + "\t" + "." + "\t" + "ID=exon" + str(counter) + ";Parent=" + linearray[1])
        else:
            print(linearray[0] + "\t" + "blast" + "\t" + "CDS" + "\t" + linearray[8] + "\t" + linearray[9] + "\t" + "." + "\t" + "-" + "\t" + "." + "\t" + "ID=exon" + str(counter) + ";Parent=" + linearray[1])

    else:
        continue

exit(0)
