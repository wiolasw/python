import os
import fileinput

text1 = "tekst.txt"
t1 = open(text1).read()
dict = {"oraz":"i", "i":"oraz", "nigdy":"prawie", "dlaczego":"nigdy"}
print( "PRZED ZMIANĄ: \n {}".format(t1))


for line in fileinput.input(text1, inplace=True):
    for old, new in dict.items():
        if old in line:
            line = line.replace(old, new)
    print(" \n PO ZAMIANIE:  \n {}".format(line))




