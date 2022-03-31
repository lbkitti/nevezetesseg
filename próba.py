import webbrowser
lista = []

def f1(label):
    print(label)
    inputFile("adatok.txt")
    print("\tA program készen áll!")


def f2(label):
    print(label)
    while True:
        print("\t1. -", (kinézet(lista[0])))
        print("\t2. -", (kinézet(lista[1])))
        print("\t3. -", (kinézet(lista[2])))
        print("\t4. -", (kinézet(lista[3])))
        print("\t5. -", (kinézet(lista[4])))
        print("\t6. -", (kinézet(lista[5])))
        print("\t7. -", (kinézet(lista[6])))
        print("\t8. -", (kinézet(lista[7])))
        print("\t9. -", (kinézet(lista[8])))

        szám = int(input("Kérek egy számot 1-6: "))
        if(szám == 1):
            print(kinézet(lista[0]))
            webbrowser.open("https:\\https://hu.wikipedia.org/wiki/Disneyland_(P%C3%A1rizs)")

def inputFile(file):
    f = open(file, "r")
    for sor in f:
        sor = sor[0:-1].split(";")
        példány = str(sor[0]),str(sor[1]),str(sor[2])
        lista.append(példány)
    f.close()

def kinézet(lista):
    return ",".join(str(x) for x in lista)

f1("Országok")
f2("Országok")
