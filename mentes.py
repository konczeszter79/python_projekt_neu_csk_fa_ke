def mentes(j):
        with open("jatekallas.txt","w") as fájl:
            print(j, file=fájl)

def tárgyakfájl(targy):
    with open("targyak.txt", "w") as fájl:
        for x in targy:
            print(x, end="\n", file=fájl) 
