tárgyak = []
import textwrap
import shutil
import os
import mentes as m

def tárgyakfájl():
    with open("targyak.txt", "w") as fájl:
        for x in tárgyak:
            print(x, end="\n", file=fájl) 
def printszöveg(szoveg, margo=4):
    columns = shutil.get_terminal_size(). columns
    width = columns - margo * 2

    bekezdesek = szoveg.split("\n\n")

    for b in bekezdesek:
        formázás = textwrap.fill(
        szoveg,
        width=width,
        initial_indent=' ' * margo,
        subsequent_indent=' ' * margo
        )
    
    print(formázás)
    print()

def formázott_input(szoveg, margo=4): 
    printszöveg(szoveg, margo) 
    return input(" " * margo)

class LabirintusJatek:
    def __init__(self):
        printszöveg("\n\nÜdvözöllek a kalandban, amelynek során ki kell szabadulnod a gonosz varázsló tornyából, ahova bezárt, hogy az életerődből táplálkozva hajtson végre egy sötét varázslatot. Szobáról szobára kell haladnod, összegyűjteni a kiszabaduláshoz szükséges tárgyakat és információkat. Figyelj jól mindenre! A kaland során minden döntési pontnál több lehetőség közül választhatsz, a döntésedtől függ, hogy mi lesz a következő lépés. A továbblépéshez nyomd meg az Entert.")
        input()
        printszöveg("\n\nLassan térsz magadhoz. Érzed, hogy kőpadlón fekszel. Fáj a fejed. Lassan eszedbe jut, mi történt: az a kedves idegen a kocsmában meghívott több kör sörre. Jókat beszélgetettek a kalandjaitokról. Az még felvillan, hogy elindultál hazafelé, majd egy ütést éreztál a fejtetődön, és sötétség. Kinyitod a szemed. Egy szobát látsz magad körül. Lassan feltápászkodsz és körülnézel. A továbblépéshez nyomd meg az Entert.")
        input()
        self.ElsoSzoba()

            
    def ElsoSzoba(self):
        printszöveg("\n\nAz egyik falon ablakot látsz, de rács van rajta.")
        printszöveg("\n\nA szoba két rövidebb falán egy-egy ajtót látsz.")  
        printszöveg("\n\nAz ablakkal  szemben egy íróasztalt látsz, rajta pergamenek.")
        printszöveg("\n\n1. Odamégy az ablakhoz és kinézel rajta.")
        printszöveg("\n\n2. Odamégy az íróasztalhoz, és megnézed a pergament.")
        printszöveg("\n\n3. Benyitsz a két ajtón egymás után.")

        válasz = formázott_input("\n\nMelyiket választod? (1, 2 vagy 3): ")
        self.ElsőVálasztás(válasz)

    def ElsőVálasztás(self, válasz):
        if válasz == '1':
            self.ablak()
        elif válasz == '2':
            self.asztal()
        elif válasz == '3':
            self.ajtók()    
        else:
            printszöveg("\n\nHelytelen választás. Próbáld újra.")
            self.ElsoSzoba() 
            
    def ablak(self):
        printszöveg("\n\nOdalépsz az ablakhoz és kinézel rajta. Látszik, hogy magasan vagy. Ez egy toronyszoba lesz! Nyomd meg az entert a visszalépéshez! ")
        input()
        self.ElsoSzoba()

    def asztal(self):
        printszöveg("\n\nOdalépsz az asztalhoz, felveszed az első pergament. Latinul van. Próbálod lefordítani, de a latintudásod ugyancsak megkopott az iskola óta. Ezt látod:") 
        printszöveg("\n\nExsugitur vita innocentium, Spiritus rapiuntur ad sacrificium.")
        printszöveg("\n\nVis vitalis colligitur in obscuro, Potentia daemonii nutritur ex sanguine.")
        printszöveg("\n\nCum vita consumpta sit, Infernum aperitur, et lumen aeternum devoratur.")
        printszöveg("\n\nVerba arcana: Rapite spiritus, colligite vitam, Sacrificium fiat, et oblivio regnet!")
        printszöveg("\n\nMi lehet ez? Bárcsak jobban figyeltél volna a latin tanárodra…")
        printszöveg("Vita innocentium' (az ártatlanok élete) és 'spiritus rapiuntur' (a lelkek elragadtatnak) egyértelműen baljós. A 'sacrificium' és 'potentia daemonii' utal arra, hogy az életerő nem önmagában kell, hanem egy nagyobb, démoni hatalom táplálására. Az 'Infernum aperitur' (a pokol megnyílik) és 'lumen aeternum devoratur' (az örök fény elnyeltetik) jelzi, hogy az átok végső célja a világosság teljes megsemmisítése.")
        printszöveg("Ajjaj, mibe keveredtél… Ki kell innen jutnod hamar.")
        printszöveg("\n\nNyomd meg az entert a visszalépéshez! ")
        input()
        self.ElsoSzoba()

    def ajtók(self):
        printszöveg("\n\nA jobb oldali ajtó mögött egy világos szobát látsz, de nincs benne semmi különös, viszont további két ajtó nyílik belőle, az egyik előre vezet, a másik jobbbra. A bal oldali ajtó mögött csak sötétséget találsz")        
        printszöveg("\n\n1. Világos.")
        printszöveg("\n\n2. Sötét.")
        válasz = formázott_input("\n\nMelyiket választod? (1 vagy 2)")

        if válasz == '1':
            self.vilagos()
        elif válasz == '2':
            if "rozsdáskulcs" in tárgyak:
                self.kovszakasz()
            else:
                printszöveg("\n\nFurcsa érzésed támad. Valami még hiányzik. Talán meg kellene nézni a többi szobát alaposan. Folytatáshoz nyomd meg az Entert.")
            input()
            self.ajtók()
        else:
            printszöveg("\n\nHelytelen választás. Próbáld újra.")
            self.ajtók()
            
            
    def vilagos(self):
        printszöveg("\n\n Belépsz a világos szobába. A falon díszes tapéta, tájképek, de bútorok nincsenek, csak egy lovagi páncél áll az egyik sarokban.")
        printszöveg("\n\n1. Megnézed a péncélt.")
        printszöveg("\n\n2. Benyitsz az előre vezető ajtón.")
        printszöveg("\n\n3. Benyitsz a jobbra nyíló ajtón.")
        printszöveg("\n\n4. Átmégy a pergamenes szobába.")
        válasz = formázott_input("\n\nmelyiket választod? (1, 2, 3, 4)")

        if válasz == '1':
            self.pancel()
        elif válasz == '2':
            self.elore()
        elif válasz == '3':
            self.jobbra()
        elif válasz == '4':
            self.ajtók()
        else:
            printszöveg("\n\nHelytelen választás. Próbáld újra.")
            self.vilagos()

    def pancel(self):
        printszöveg("\n\nKözelebb mégy a páncélhoz, felemeled a sisakrostélyt, megkopogtatod, de nem találsz semmi különöset. A folytatáshoz nyomd meg az entert.")
        input()
        self.vilagos()

    def elore(self):
        printszöveg("\n\nA szobában ahol vagy több tárgy és bútor is található. Az ajtóval szemben lévő falon egy komód áll, balra egy ládát látsz, jobbra egy ruhásszekrény.")
        printszöveg("\n\n1. Megnézed a  ruhásszekrényt.")
        printszöveg("\n\n2. Megnézed a komódot.")
        printszöveg("\n\n3. Megnézed a ládát.")
        printszöveg("\n\n4. Átmégy a páncélos szobába.")
        válasz = formázott_input("\n\nMelyiket választod? (1, 2 , 3 vagy 4)")

        if válasz == '1':
            self.szekreny()
        elif válasz == '2':
            self.komod()
        elif válasz == '3':
            self.lada()
        elif válasz == '4':
            self.pancel()
        else:
            printszöveg("\n\nHelytelen választás. Próbáld újra.")
            self.vilagos()
            
    def jobbra(self):
        printszöveg("\n\nEgy szobába kerülsz, ahol rengeteg fénykép van a falakon, feltételezhetően a varázslót ábrázolják. Alaposan megnézed őket, némelyiktől (a varázsló fürdőruhában a  tengerparton, a varázsló az éves varázslóbálban), egyszerre hánynál és röhögnél, de nem találsz semmi használhatót, a képek a falhoz vannak mágikusan ragasztva, nem tudod megnézni a  hátuljukat. A folytatáshoz nyomd meg az Entert.")
        input()
        self.vilagos()

    def szekreny(self):
        printszöveg ("\n\nKinyitod a szekrényt,  egy kabátot találsz benne. Belenyúlsz a zsebeibe, az egyikben egy kis darab pergament találsz.  Megnézed: 15=X x 3 Elteszed a zsebedbe a pergament. Nyomd meg az Entert a folytatáshoz.")
        tárgyak.append("pergamen: 15 = X * 3")
        input()
        self.elore()
    def komod(self):
        printszöveg("\n\nSorban kihúzod a fiókokat. A felsőben alsónadrágokat találsz. Seprűs, üstös, feketemacskás, varázspálcás… Hány éves ez az ember, óvodás?  Közéjük túrsz, de nincs ott semmi. A középső fiók üres. A harmadikban egy füzet van, amiben csak az első oldalon szerepel valami: egy rajz egy  furcsa zárról, amin egy tekerőgomb található, felette egy nyíl, ami balra mutat. Elteszed a füzetet a zsebedbe.  Folytatáshoz nyomd meg az Entert.")
        tárgyak.append("füzet első oldal: tekerőgomb rajz balra mutató nyíllal")
        input()
        self.elore()
    def lada(self):
        printszöveg("\n\nA ládához mégy. Egy tekerőgombos lakat van rajta. Előveszed a zsebretett tárgyakat. Ha kettőnél kevesebb tárgy van nálad, nyomj 1-est és még néz szét. Ha két tárgy van nálad, nyomj 2-est.")

        printszöveg("A zsebedben lévő tárgyak: " + ", ".join(tárgyak))

        válasz = formázott_input("Melyiket választod? (1 vagy 2) ")

        if válasz == '1':        
            self.elore()
        else:
            printszöveg("\n\nEz éppen olyan lakat, mint a füzetben! Hogyan tekered el a  gombot?")

        printszöveg("\n\n1. 3-szor jobbra.")
        printszöveg("\n\n2. 5-ször balra")
        printszöveg("\n\n3. 10-szer balra")

        válasz = formázott_input("\n\nMit választasz? (1, 2 vagy 3)")
        if válasz == '2':
            printszöveg("\n\nA lakat kattan egyet, a láda kinyílik. Szinte teljesen üres, de az alján egy rozsdás kulcs hever. Zsebre vágod, biztos, ami biztos. ")
            tárgyak.append("rozsdáskulcs")
            printszöveg("\n\nA folytatáshoz nyomd meg az Entert. ")
            input()
            self.elore()
        else:
            printszöveg("\n\nA lakat meg sem moccan. Próbáld újra. Nyomd meg az Entert. ")
            input()
            self.lada()

    def kovszakasz(self):
        printszöveg("Miután nem volt más választásod a sötét szobába léptél be. Az előző szobából beáradó fény alig világítja meg a szobát az egyik falon halványan felsejlik valami, de amint teljesen átlépsz a szobába a mögötted lévő ajtó becsukódik és nem tudod kinyitni. Ahhoz, hogy megtaláld a kiutat szükséged van fényforrásra.")
        self.sotetszoba()
    def sotetszoba(self):
        printszöveg("1. Elkezdesz a falon tapogatózni.")
        printszöveg("2. Elkezdesz kutakodni.")
        válasz = formázott_input("Melyiket választod? (1 vagy 2) ")
        self.sotetszoba_válasz(válasz)
    
    def sotetszoba_válasz(self, válasz):
        if válasz == "1":
            self.falkutatas()
        elif válasz == "2":
            self.kutakodas()
        else:
            printszöveg("Helytelen választás. Próbáld újra.")
            self.sotetszoba()

    def falkutatas(self):
        printszöveg("\nA fal hideg és érdes. Rúnák vannak rajta, de fény nélkül nem tudod elolvasni.")
        formázott_input("Nyomj Entert a visszalépéshez...")
        self.sotetszoba()
    
    def kutakodas(self):
        printszöveg("Ahogy a sötét szobába kutakodsz a szoba közepén belerúgsz valamibe. Kínok között próbálod visszafojtani a feltörő szitkokat. Miután sikerül az önuralmadat visszaszerezni, elkezded végig tapogatni, hogy minek ütköztél neki. Rájössz, hogy egy ládába rúgtál bele. Megpróbálod kinyitni és szerencséd van mert nincs lezárva. A ládát átkutatva egy gömb alakú kristályra akadsz, ami a kezed melegétől fényesen kezd ragyogni. Ahogy a fény beteríti a szobát a falon rúnák válnak láthatóvá és két ajtó rajzolódik ki jobbra és előtted.")
        tárgyak.append("fénykristály")
        self.sotetszoba_lehetosegek()

    def sotetszoba_lehetosegek(self):
        printszöveg("1. Elolvasod a rúnákat.")
        printszöveg("2. Előtted lévő ajtó kinyítása.")
        printszöveg("3. Jobb oldali ajtó kinyítása.")
        válasz = formázott_input("Melyiket választod? (1, 2 vagy 3) ")
        
        if válasz == "1":
            self.runaolvasas()
        elif válasz == "2":
            self.szembeajto()
        elif válasz == "3":
            self.jobbajto()

    def runaolvasas(self):
        printszöveg("Örülsz, mert a rúna olvasást mindig jobban szeretted az iskolába, mint a latint. Az alábbi szöveg látható a falon: ")
        printszöveg("ᚠᚢᚦᚨᚱᚲᚷᚹᚺᚾᛁᛃᛇᛈᛉᛊᛏᛒᛖᛗᛚᛜᛞᛟᚼᚻᚯᚱᛝᛡ")
        printszöveg("Miután elolvastad rájössz, hogy ez egy találós kérdés. Ami így szól: Varázsbotja nincsen neki, de a tájat eltünteti. Mikor leszáll, azt sem tudod, merre van az orrod.")
        self.talaloskerdes()
    
    def talaloskerdes(self):
        printszöveg("1. Hóvihar")
        printszöveg("2. Köd")
        printszöveg("3. Sűrű erdő")
        tipp = formázott_input("Mi az? ")

        if tipp == "2":
            printszöveg("A válaszod helyes. Jegyez meg hátha még jól jön.")
            self.sotetszoba_lehetosegek()
            tárgyak.append('köd')
        elif tipp == "1" or "3":
            printszöveg("Nem találtad el.")
        else:
            printszöveg("Helytelen választás. Próbáld újra.")

        while tipp != "2":
            tipp = input("Mi az? ")
        if tipp == "2":
            printszöveg("A válaszod helyes. Jegyez meg hátha még jól jön.")
            tárgyak.append('köd')
            self.sotetszoba_lehetosegek()
        elif tipp == "1" or "3":
            printszöveg("Nem találtad el.")
        else:
            printszöveg("Helytelen választás. Próbáld újra.")

    def szembeajto(self):
        printszöveg("Amint átléped a küszöböt az ajtó becsukódik mögötted. Azonnal érzed, hogy valami nincs rendben: a levegő súlyos és szinte mozogni látszik. A falak mentén fekete köd gomolyog, amely néha arcokat formál -mintha réges-rég elveszett lelkek próbálnának figyelmeztetni. A szoba közepe üres, nincsenek tárgyak, nincsen más kijárat")
        printszöveg("A suttogások halkan, de tisztán hallatszanak: Vissza kell fordulnod… Ez az út nem neked való… A fény útja máshol vezet…")
        printszöveg("Ahogy tovább lépsz, a padló alatt fekete repedések nyílnak meg, mintha az árnyak széttépnék a teret. Egyetlen út van: Vissza az előző szobába.")
        self.sotetszoba_lehetosegek()    

    def jobbajto(self):
        printszöveg("Belépsz a szobába, amelyet halvány mágikus fényvilág tölt be. ")
        printszöveg("Két ajtót látsz: Az egyik zárva van, rajta egy nagy vaslakat. A másik ajtó lassan hangos nyikorgással kitárul.")
        printszöveg("Mögötte a semmi… vagy valami sokkal rosszabb, de úgy tűnik, ez vezet tovább. A szobába észreveszel egy képet, ami mintha furcsán állna.")
        self.hetedikszoba()
    
    def hetedikszoba(self):
        printszöveg("1. Megvizsgálod a képet")
        printszöveg("2. Előveszed a kulcsot és kinyitod az ajtót")
        printszöveg("3. Tovább mész a nyitott ajtón")
        válasz = formázott_input("Mit teszel? ")

        if válasz == "1":
            self.kepvizsgalat()
        if válasz == "2":
            self.zartajto()
        if válasz == "3":
            self.MegoldasSzoba()
        
    def kepvizsgalat(self):
        printszöveg("Ahogy a képet megmozdítod, egy rejtett szekrényt találsz. A felületén egy összetekeredő kígyó lenyomata rajzolódik ki.")
        printszöveg("A kígyó szemei halványan felizzanak, majd köd gomolyog körülötte.")
        printszöveg('„Csak az léphet tovább, aki emlékszik a rúnák által rejtett találóskérdésre.”')
        self.vizsalat_runa()

    def vizsalat_runa(self):
        olvas = formázott_input("Elolvastad a rúnaírást? (igen/nem) ")
        if olvas == "igen":
            self.runaelolvasva()
        if olvas == "nem":
            self.sotetszoba_lehetosegek()

    def runaelolvasva(self):        
        válasz = formázott_input("Írd be a rúnaszót: ").casefold()

        if válasz == "köd".casefold():
            printszöveg("A rúnák felizzanak, majd egy kattanás hallatszik. A rejtett szekrény kinyílik!")
            printszöveg("Belül egy pergament papír található, amin az alábbi szöveg látható.  7 + 3 x 2 = ?")
            tárgyak.append("Feladvány: 7 + 3 x 2 = ?")
            self.hetedikszoba()
        else:
            printszöveg("Hibás rúnaszó. Próbáld újra.")

        while True:
            válasz = formázott_input("Írd be a rúnaszót: ").casefold()
            if válasz == "köd".casefold():
                printszöveg("A rúnák felizzanak, majd egy csilingelő hang hallatszik. A rejtett szekrény kinyílik!")
                printszöveg("Belül egy pergament papír található, amin az alábbi szöveg található.  7 + 3 x 2 = ?")
                tárgyak.append("Feladvány: 7 + 3 x 2 = ?")
                self.hetedikszoba()
            else:
                printszöveg("Hibás rúnaszó!")
                printszöveg("Elfelejtetted a feladványt vagy nem is olvastad el a rúnaírást???")
                printszöveg("Büntetésből visszadoblak a rúna megfejtéséhez.")
                self.runaolvasas()
        
    def zartajto(self):
        printszöveg("A már megtalált kulccsal megpróbálod kinyitni az ajtót és sikerrel jász.")  
        printszöveg("Belépve a szobába a szoba közepén egy kőtalapzatot látsz rajta egy fém doboz áll.")
        printszöveg("Közeleb lépve látod meg, hogy egy számkódos lakat zárja le. A dobozon halvány kigyó lenyomat jelenik meg, mint amilyet a kép mögött láttál a szekrény felületén.")
        printszöveg("Eszedbe jut, hogy a pergamenen egy matematikai feladvány állt. Mi is volt a feldvány?")
        printszöveg(tárgyak[1])
        printszöveg("20")
        printszöveg("12")
        printszöveg("13")
        válasz = formázott_input("Írd be a megfelelő számkódot: ")

        if válasz == "13":
            printszöveg("A lakat kattan egyet, majd leesik a földre. Kinyitod a doboz fedelét és egy különös formájú kulcsot találsz benne. Elteszed a kulcsot és visszatérsz az előző szobába.")
            tárgyak.append("forma_kulcs")
            self.hetedikszoba()
        elif válasz == "20" or "12": 
            printszöveg("Hibás kódot adtál meg.")

        while True:
            válasz = formázott_input("Írd be a megfelelő számkódot: ")
            if válasz == "13":
                printszöveg("A lakat kattan egyet, majd leesik a földre. Kinyitod a doboz fedelét és egy különös formájú kulcsot találsz benne. Elteszed a kulcsot és visszatérsz az előző szobába.")
                tárgyak.append("forma_kulcs")
                self.hetedikszoba()
            elif válasz == "20" or "12":
                printszöveg("Hibás kódot adtál meg.")
                printszöveg("Hirtelen mintha valami megragadna. Majd arra eszmélsz, hogy visszakerültél az előző szobába a képhez")
                self.kepvizsgalat()


jatek = LabirintusJatek()