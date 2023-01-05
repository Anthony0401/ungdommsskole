from random import randint
import time
import os
plankton = ()
play_again = ()
pokemonlist = ["[1]multiplikasjon", "[2]divisjon", "[3]subtraksjon", "[4]addisjon"]
pokemonlist2 = ["", "[nivå] ", "[nivå] ", "[nivå]"]
score = 0
b = ()
def clear(): os.system('cls')

play = True
while play:
    a=input("Er du klar til å starte mattespillet???: ")
    time.sleep(1)
    clear()
    for number, letter in enumerate(pokemonlist):
        print(letter) 
    print()    
    print("[VELG VED Å SKRIVE NED TALLET]")
    choose_task = input("Hva har du lyst til å jobbbe med??? : ")
    time.sleep(1)
    clear()
    ant_stykker = int(input("Hvor mange ganger har du lyst til å spille: "))
    time.sleep(1)
    clear()
    for number, letter in enumerate(pokemonlist2):
        print(number, letter)
    nivå = input("Hvilken vansklighet???: ")
    time.sleep(1)
    clear()
    play = False
def multiplikasjon1(level):
    global score
    global plankton
    for _ in range(ant_stykker):
        num1 = randint(level, level*10) 
        num2 = randint(level, level*10)
        print(f" hva er {num1} ganger {num2}")
        print()
        svar = input("skriv svare ditt her: ")
        if int(svar) == num1 * num2:
            print("Nice du klarte det! ")
            score += 1
            time.sleep(1)
            clear()
        else:
            print("Sorry prøv seinere svaret var " + str(num1 * num2))
            time.sleep(1)
            clear()
    print(f"Du har fått {score} av {ant_stykker}")
    print("skriv yes for å fortsette ")
    plankton = str(input("har du lyst til å spille igjen??? "))
def multiplikasjon():
    if nivå in ["1", "2", "3", "4"]:
        multiplikasjon1(int(nivå))
    else:
        print("pokemon er en pokmemon")
def divisjon1(level):
    global score
    global plankton
    for _ in range(ant_stykker):
        num1 = randint(level, level*10)  
        num2 = randint(level, level*10)
        print(f"Hva er {num1} delt med {num2}")
        svar = input("skriv svaret ditt her: ")
        if int(svar) == num1 / num2:
            print("Nice du klarte det! ")
            score+= 1
            time.sleep(1)
            clear()
        else:
            print("Sorry prøv seinere svaret var " + str(num1 / num2))
            time.sleep(1)
            clear()
    print(f"Du fikk {score} av {ant_stykker}")
    print("skriv yes for å fortsette ")
    plankton = str(input("Har du lyst til å spillle igjen??? "))
def divisjon():
    if nivå in ["1", "2", "3","4"]:
        divisjon1(int(nivå))
    else:
        print("pokemon er en pokemon")   
def addisjon1(level):
    global score
    global plankton
    for _ in range(ant_stykker):
        num1 = randint(level, level*10) 
        num2 = randint(level, level*10)
        print(f"hva er {num1} + {num2}")
        
        svar = input("skriv svare ditt her: ")
        
        if int(svar) == num1 + num2:
            print("Nice du klarte det! ")
            score+= 1
            time.sleep(1)
            clear()
        else:
            print("Sorry prøv seinere svaret var " + str(num1 + num2))
            time.sleep(1)
            clear()
    print(f"Du fikk {score} av {ant_stykker}")
    print("skriv yes for å fortsette ")
    plankton = str(input("Har du lyst til å spille igjen "))
def addisjon():
    if nivå in ["1", "2", "3","4"]:
        addisjon1(int(nivå))
    else:
        print("pokemon er en pokemon")
def subtraksjon1(level):
    global score
    global plankton
    for _ in range(ant_stykker):
        num1 = randint(level, level*10) 
        num2 = randint(level, level*10)

        print(f" Hva er {num1} - {num2} ")
        
        svar = input("skriv svare ditt her: ")
        
        if int(svar) == num1 - num2:
            print("Nice du klarte det! ")
            score+= 1
            time.sleep(1)
            clear()
        else:
            print("Sorry prøv seinere svaret var " + str(num1 - num2))
            time.sleep(1)
            clear()
    print(f"Du fikk {score} av {ant_stykker}")
    print("skriv yes for å fortsette ")
    plankton = str(input("Har du lyst til å spille igjen??? "))
def subtraksjon():
    if nivå in ["1", "2", "3","4", "9"]:
        subtraksjon1(int(nivå))
    else:
        print("pokmeon")

if choose_task == "1":
    multiplikasjon()
elif choose_task == "2":
    divisjon()
elif choose_task == "3":
    subtraksjon()
elif choose_task == "4":
    addisjon()
else:
    print(f"valget finnes ikke!!! Det finnes bare {pokemonlist} oki")
if plankton == "yes":
    play = True
else:
    print("[trykk enter 2 ganger for å gå ut]")
score = 0
while play:
    a=input("Er du klar til å starte mattespillet???: ")
    time.sleep(1)
    clear()
    for number, letter in enumerate(pokemonlist):
        print(letter) 
    print("[VELG VED Å SKRIVE NED TALLET]")
    choose_task = input("Hva har du lyst til å jobbbe med??? : ")
    time.sleep(1)
    clear()
    ant_stykker = int(input("Hvor mange ganger har du lyst til å spille: "))
    time.sleep(1)
    clear()
    for number, letter in enumerate(pokemonlist2):
        print(number, letter)
    nivå = input("Hvilken vansklighet???: ")
    play = False
if choose_task == "1":
    multiplikasjon()
elif choose_task == "2":
    divisjon()
elif choose_task == "3":
    subtraksjon()
elif choose_task == "4":
    addisjon()
else:
    print(f"valget finnes ikke!!! Det finnes bare {pokemonlist} oki")