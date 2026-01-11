def mentes(j):
        with open("proba.txt","w") as fájl:
            print(j, file=fájl)

def tárgyakfájl(targy):
    with open("targyak.txt", "w") as fájl:
        for x in targy:
            print(x, end="\n", file=fájl) 
