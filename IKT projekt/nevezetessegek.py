import n_class
adatok = []

def f1(label):
    print(label)
    for i in range(len(adatok)):
        print("\t",adatok[i].ország)
    

def f2(label):
    print(label)
    orszagnev = input("\tKérek egy országot: ")
    for i in range(len(adatok)):
        if(orszagnev == adatok):
            print(ország[i])
        print('\t', adatok[i].nevezetesség)
    nevezetesseg = input("\tKérek egy város betűjelét: ")
    #break
    for i in range(len(adatok)):
        if nevezetesseg == adatok:
            print(város[i])

def f3(label):
    print(label)
    ország = input('\tKérek egy országot: ')
    #nev = len(adatok[i].ország)
    f = (adatok[0].ország and adatok[4].ország)
    usa = (adatok[1].ország)
    k = (adatok[2].ország)
    i = (adatok[7].ország)
    auszt = (adatok[8].ország)
    m = (adatok[3].ország and adatok[5].ország and adatok[6].ország)

    if ország == f:
        print('\t',adatok[0].város)

    if ország == usa:
        print('\t',adatok[1].város)

    if ország == k:
        print('\t',adatok[2].város)

    if ország == i:
        print('\t',adatok[7].város)

    if ország == auszt:
        print('\t',adatok[8].város)

    if ország == m:
        print('\t',adatok[3].város )
        print('\t',adatok[5].város)
        print('\t',adatok[6].város)
        
    
def inputFile(file): 
    f = open(file,"r",encoding="utf-8")
    for sor in f:
        sor = sor[0:-1].split(";")
        példány =n_class.Nevek(sor[0],sor[1],sor[2])
        adatok.append(példány)
    f.close()

inputFile('nevezetessegek.txt')
f1("1.feladat")
#f2("2.feladat")
f3("próba")
