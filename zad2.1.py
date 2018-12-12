
import sys

f = open("plik", "w")
zdanie = "Czesc jestem Wiola, studiuje i pracuje"
f.write(zdanie)
f.close()

plik = open("plik")
try:
    tekst = plik.read()
finally:
    plik.close()

print (tekst)