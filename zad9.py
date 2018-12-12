import os
import fileinput

text1 = "tekst_d.txt"
t1 = open(text1).read()
print( "PRZED ZMIANĄ: \n {}".format(t1))

delate_words = ["się", "i", "oraz", "nidgy", "dlaczego"]
for line in fileinput.input(text1, inplace=True):
    for word in delate_words:
        if word in line:
            line = line.replace(word, "")
    print("PLIK PO USUNIECIU WYRAZOW: \n {} ".format(line))




