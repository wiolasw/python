import os

sciezka = 'C:/Users/wiola/PycharmProjects'

def listuj(katalog):
    for element in os.listdir(katalog):
        pelna_sciezka = os.path.join(katalog, element)
        print (pelna_sciezka)
        if os.path.isdir(pelna_sciezka):
            listuj(pelna_sciezka)

listuj(sciezka)