from random import *

liczby = []
seed()
for i in range(50):
    liczby.append(randint(0,1000))
print ("LOSOWE LICZBY: \n {} ".format(liczby))

def sortowanie (liczby):
    for i in range(len(liczby)):
         for j in reversed(range(len(liczby)-1)):
            if (liczby[j]< liczby[j+1]):
                min = liczby[j+1]
                liczby[j+1]=liczby[j]
                liczby[j]=min
    print ("SORTOWANIE MALEJACE: \n{} ".format(liczby))


sortowanie(liczby)

