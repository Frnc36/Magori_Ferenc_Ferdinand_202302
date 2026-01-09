import random

def velszamok():
    velszamok_lista = []
    i = 0
    while i < 7:
        velszam = random.randint(1,100)
        velszamok_lista.append(velszam)
        i += 1
    return velszamok_lista
def kiir(velszamok_lista):
    print("II/A feladat, kiírás")
    i = 0
    while i < len(velszamok_lista):
        if i < len(velszamok_lista) - 1:
            print(velszamok_lista[i], end=";")
        else:
            print(velszamok_lista[i])
        i += 1

def szamolas(velszamok_lista):
    paratlan = 0
    i = 0
    while i < len(velszamok_lista):
        if velszamok_lista[i] % 2 == 1:
            paratlan += 1
        i +=1
    return paratlan

""" def nagyobb(velszamok_lista):
    nagyobb = velszamok_lista[0]
    kisebb = velszamok_lista[0]
    i = 0
    while i < len(velszamok_lista):
        if velszamok_lista[i] > nagyobb:
            nagyobb = velszamok_lista[i]
        if velszamok_lista[i] < kisebb:
            kisebb = velszamok_lista[i]
        i += 1
    return nagyobb, kisebb """

def nagyobb(velszamok_lista):
    nagyobb = velszamok_lista[0]
    i = 0
    while i < len(velszamok_lista):
        if velszamok_lista[i] > nagyobb:
            nagyobb = velszamok_lista[i]
        i += 1
    return nagyobb

def kisebb(velszamok_lista):
    kisebb = velszamok_lista[0]
    i = 0
    while i < len(velszamok_lista):
        if velszamok_lista[i] < kisebb:
            kisebb = velszamok_lista[i]
        i += 1
    return kisebb


def kiiras(paratlan, nagyobb, kisebb):
    print("II/B feladat, számolás")
    print("páratlanok száma:",paratlan)
    print(f"legkisebb érték {kisebb}, legnagyobb érték: {nagyobb}")


def fajlba_iras(paratlan):
    with open("paratlanok.txt", "w", encoding="UTF-8") as f:
        f.write("II/C feladat, fajlba Írás\nparatlanok.txt elkészült!")