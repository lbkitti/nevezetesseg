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

        szám = int(input("Kérek egy számot 1-9: "))
        if(szám == 1):
            print(kinézet(lista[0]))
            webbrowser.open("https://hu.wikipedia.org/wiki/Disneyland_(P%C3%A1rizs)")

        if(szám == 2):
            print(kinézet(lista[1]))
            webbrowser.open("https://en.wikipedia.org/wiki/Disney%27s_Hollywood_Studios")

        if(szám == 3):
            print(kinézet(lista[2]))
            webbrowser.open("https://hu.wikipedia.org/wiki/Tiltott_V%C3%A1ros")

        if(szám == 4):
            print(kinézet(lista[3]))
            webbrowser.open("https://hu.wikipedia.org/wiki/P%C3%A1l-v%C3%B6lgyi-barlangrendszer")

        if(szám == 5):
            print(kinézet(lista[4]))
            webbrowser.open("https://hu.wikipedia.org/wiki/Eiffel-torony")

        if(szám == 6):
            print(kinézet(lista[5]))
            webbrowser.open("https://hu.wikipedia.org/wiki/Balaton")

        if(szám == 7):
            print(kinézet(lista[6]))
            webbrowser.open("https://hu.wikipedia.org/wiki/Sz%C3%A9chenyi_l%C3%A1nch%C3%ADd")

        if(szám == 8):
            print(kinézet(lista[7]))
            webbrowser.open("https://en.wikipedia.org/wiki/Taj_Mahal")

        if(szám == 9):
            print(kinézet(lista[8]))
            webbrowser.open("https://hu.wikipedia.org/wiki/Sydney-i_Operah%C3%A1z")

def inputFile(file):
    f = open(file, "r", encoding="utf-8")
    for sor in f:
        sor = sor[0:-1].split(";")
        példány = str(sor[0]),str(sor[1]),str(sor[2])
        lista.append(példány)
    f.close()

def kinézet(lista):
    return ",".join(str(a) for a in lista)

f1("Országok")
f2("Országok")
