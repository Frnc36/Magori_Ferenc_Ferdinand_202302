def feladat_bekeres():
    print("I/A.feladat bekérés")
    nev = str(input("Név: "))
    kor = int(input("kor: "))

    print("I/B feladat, kiírás")
    if kor < 14:
        print(f"{nev} kora {kor} év, még gyerek")
    elif kor < 18:
        print(f"{nev} kora {kor} év, még kiskorú")
    else:
        print(f"{nev} kora {kor} év, már nagykórú")