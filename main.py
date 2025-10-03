"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Pavlína Čepcová
email: cepcovap@gmail.com
"""
import sys
import random
import time
#Uvod do hry
#Rozdelovac slouzi pro grafické oddělení textu
rozdelovac = ("-") * 47 
print("Hi there!")
print(rozdelovac)
print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
print(rozdelovac)

#Funkce pro generování tajného čísla
def generate_secret_number() -> int:
    """ 
    Funkce generující 4 neopakující se čísla. (Nesmí začínat nulou.)
    """
    hadanka = []
    while len(hadanka) < 4:
        cislo = random.randint(0,9)
        if len(hadanka) == 0:
            hadanka.append(random.randint(1,9))
        if cislo not in hadanka:
            hadanka.append(cislo)
    retezec = "".join(str(cislo) for cislo in hadanka)
    return retezec

#Funkce pro vstup hráče
def user_input() -> str:
    """ Funkce zajišťující správný vstup od uživatele.
    """
    while True:
        volba = input("Enter a number: ")
        if not volba.isdigit(): 
            print("Invalid choice.\nYou have to enter digits only")
            continue
        if len(volba) != 4:
            print("Invalid choice.\nPlease enter 4 digits.")
            continue
        if len(set(volba)) < 4:
            print("The number must not contain duplicate digits.")
            continue
        if (volba[0]) == "0":
            print("Invalid choice.\nZero cannot be the first digit.")
            continue
        else:
            return(volba)

# Funkce pro porovnání vstupu a tajného čísla - 
tajne_cislo = generate_secret_number()
def evaluate_guess(tajne_cislo: str):
    volba_hrace = user_input()
    bulls = 0
    cows = 0
    for cislo1,cislo2 in (zip(volba_hrace, tajne_cislo)):
        if cislo2 == cislo1:
            bulls +=1
    for cislo1,cislo2 in zip(volba_hrace, tajne_cislo):
        if cislo1 != cislo2 and cislo1 in tajne_cislo:
            cows +=1
    return bulls, cows

#Vyhodnocení
pocet = 0
start_time = time.time()
while True:
    bulls, cows = evaluate_guess(tajne_cislo)
    if bulls == 1 and cows == 1:
        print(f"{bulls} bull, {cows} cow")
    elif bulls == 1 and cows != 1:
        print(f"{bulls} bull, {cows} cows")
    elif bulls != 1 and cows == 1:
        print(f"{bulls} bulls, {cows} cows")
    else:
        print(f"{bulls} bulls, {cows} cow")
    print(rozdelovac)
    pocet += 1
    if bulls == 4:
        print(
            f"Correct, you've guessed the right number\n"
            f"in {pocet} guesses!"
              )
        end_time = time.time()
        print(rozdelovac)
        if pocet <= 7:
            print("That's amazing!:O")
        elif 7 < pocet <= 13:
            print("Not bad. Pretty average :)")
        else:
            print("That took a while. Try again?")
        break
    
#Prepočet času hry   
print(rozdelovac)
game_time = end_time - start_time
minutes = int(game_time // 60) 
seconds = int(game_time % 60)
print(f"Time taken: {minutes} min. {seconds}sec.")
print(rozdelovac)

#Ukončení hry a nový pokus
while True:
    nova_hra = input(
        "START the GAME again?\nPress 'y' for yes or 'q' fot qiut. "
        )
    if nova_hra  == "y":
        print(rozdelovac)
        tajne_cislo = generate_secret_number()
        evaluate_guess(tajne_cislo)
    elif nova_hra == "q":
        sys.exit()
    else:
        print("Invalid choice.")