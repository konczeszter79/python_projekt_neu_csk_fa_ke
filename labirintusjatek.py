tárgyak = []
import textwrap
import shutil
import os
import mentes as m

def tárgyakfájl():
    with open("targyak.txt", "w") as fájl:
        for x in tárgyak:
            print(x, end="\n", file=fájl) 
