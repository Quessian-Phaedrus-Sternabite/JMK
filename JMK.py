import random
from random import randint
import time
import playsound
from playsound import playsound
import threading
from threading import Thread

def getcmd(cmdlist):
    cmd = input(">>> ")
    if cmd in cmdlist:
        return cmd
    elif cmd == "Music":
        Thread(target = sound).start()
        return getcmd(cmdlist)
    else:
        print("Invalid command")

print("Welcome to Juck! Marry! KILL!!!!!")
print("Choose an option by typing the number!")
print("\n Start Game [1]")
print("\n Help [2]")
print("\n Credits [3]")
cmdlist = ['1', '2', '3', 'music']
cmd = getcmd(cmdlist)
if cmd == '1':
    startfunc()
elif cmd == '2':
    print("Type Music for music to play (Only turns it on, not off.)"
          "and type the number of the card/option you want to .")
    getcmd(cmdlist)
elif cmd == '3':
    print("Credits go to the team behind Mission to Zyxx, for creating this podcast.")
    print("Check out their website at Missiontozyxx.space")
    print("Thank you for making this awesome podcast")
    getcmd(cmdlist)

def startfunc():
    J = int(0)
    M = int(0)
    K = int(0)

    X = randint(1, 50)
    Y = randint(1, 50)
    Z = randint(1, 50)
    if X and Y and Z == 50:
        J += 9999999999
        M += 9999999999
        K += 9999999999
        print("ERROR 404 - CARD NULL DETECTED ---"
              "CARD == ROD."
              "TOTAL SCORE - 9...9...9...9...9...9...9")
        print("GAME COMPLETE")
    if X == 1:
        print("Card 1: A C.L.I.N.T.")
        print("Where do you want to place this card?")
        XI = input("J/M/K? ")
        if XI == 'j' or 'J':
            J += 2
        elif XI == 'm' or 'M':
            M += 3
        elif XI == 'k' or 'K':
            K += 1
    if X == 2:
        print("Card 1: A P.L.I.N.T.")
        print("Where do you want to place this card?")
        XI = input("J/M/K?")
        if XI == 'j' or 'J':
            J += 1
        elif XI == 'm' or 'M':
            M += 3
        elif XI == 'k' or 'K':
            K += 2
    if X == 3:
        print("Card 1: Dar")
        print("Where do you want to place this card?")
        XI = input("J/M/K?")
        if XI == 'j' or 'J':
            J += 4
        elif XI == 'm' or 'M':
            M += 1
        elif XI == 'k' or 'K':
            K += 1
    if X == 4:
        print("Card 1: Pleck")
        print("Where do you want to place this card?")
        XI = input("J/M/K?")
        if XI == 'j' or 'J':
            J += 2
        elif XI == 'm' or 'M':
            M += 1
        elif XI == 'k' or 'K':
            K += 3
    if X == 5:
        print("Card 1: Samo and Wink")
        print("Where do you want to place this card?")
        XI = input("J/M/K? ")
        if XI == 'j' or 'J':
            J += 4
        elif XI == 'm' or 'M':
            M += 1
        elif XI == 'k' or 'K':
            K += 1
    if X == 6:
        print("Card 1: Best friend Number 1")
        print("Where do you want to place this card?")
        XI = input("J/M/K? ")
        if XI == 'j' or 'J':
            J += 3
        elif XI == 'm' or 'M':
            M += 1
        elif XI == 'k' or 'K':
            K += 1
    if X == 7:
        print("Card 1: Best friend Number 2")
        print("Where do you want to place this card?")
        XI = input("J/M/K? ")
        if XI == 'j' or 'J':
            J += 2
        elif XI == 'm' or 'M':
            M += 2
        elif XI == 'k' or 'K':
            K += 1
    if X == 8:
        print("Card 1: Best friend Number 3")
        print("Where do you want to place this card?")
        XI = input("J/M/K? ")
        if XI == 'j' or 'J':
            J += 1
        elif XI == 'm' or 'M':
            M += 3
        elif XI == 'k' or 'K':
            K += 2
    if X == 9:
        print("Card 1: Best friend Number 4")
        print("Where do you want to place this card?")
        XI = input("J/M/K? ")
        if XI == 'j' or 'J':
            J += 2
        elif XI == 'm' or 'M':
            M += 1
        elif XI == 'k' or 'K':
            K += 2
    if X == 10:
        print("Card 1: Best friend Number 5")
        print("Where do you want to place this card?")
        XI = input("J/M/K? ")
        if XI == 'j' or 'J':
            J += 1
        elif XI == 'm' or 'M':
            M += 2
        elif XI == 'k' or 'K':
            K += 1
    if X == 11:
        print("Card 1: Best friend Number 6")
        print("Where do you want to place this card?")
        XI = input("J/M/K? ")
        if XI == 'j' or 'J':
            J += 3
        elif XI == 'm' or 'M':
            M += 1
        elif XI == 'k' or 'K':
            K += 1
    if X == 12:
        print("Card 1: Best friend Number 7")
        print("Where do you want to place this card?")
        XI = input("J/M/K? ")
        if XI == 'j' or 'J':
            J += 1
        elif XI == 'm' or 'M':
            M += 1
        elif XI == 'k' or 'K':
            K += 4
    if X == 13:
        print("Card 1: Peter 3 Fab")
        print("Where do you want to place this card?")
        XI = input("J/M/K? ")
        if XI == 'j' or 'J':
            J += 2
        elif XI == 'm' or 'M':
            M += 2
        elif XI == 'k' or 'K':
            K += 2
    if X == 14:
        print("Card 1: Nermut Bundaloy (Emporer)")
        print("Where do you want to place this card?")
        XI = input("J/M/K? ")
        if XI == 'j' or 'J':
            J += 1
        elif XI == 'm' or 'M':
            M += 1
        elif XI == 'k' or 'K':
            K += 4
    if X == 15:
        print("Card 1: Nermut Bundaloy (Crew)")
        print("Where do you want to place this card?")
        XI = input("J/M/K? ")
        if XI == 'j' or 'J':
            J += 3
        elif XI == 'm' or 'M':
            M += 2
        elif XI == 'k' or 'K':
            K += 1
    if X == 16:
        print("Card 1: Bermut Nundaloy (Emporer)")
        print("Where do you want to place this card?")
        XI = input("J/M/K? ")
        if XI == 'j' or 'J':
            J += 4
        elif XI == 'm' or 'M':
            M += 0
        elif XI == 'k' or 'K':
            K += 2
    if X == 17:
        print("Card 1: Bermut Nundaloy (Crew)")
        print("Where do you want to place this card?")
        XI = input("J/M/K? ")
        if XI == 'j' or 'J':
            J += 1
        elif XI == 'm' or 'M':
            M += 1
        elif XI == 'k' or 'K':
            K += 4
    if X == 18:
        print("Card 1: Beanochron(Beano)")
        print("Where do you want to place this card?")
        XI = input("J/M/K? ")
        if XI == 'j' or 'J':
            J += 3
        elif XI == 'm' or 'M':
            M += 3
        elif XI == 'k' or 'K':
            K += 0
    if X == 19:
        print("Card 1: Young Durf")
        print("Where do you want to place this card?")
        XI = input("J/M/K? ")
        if XI == 'j' or 'J':
            J += 1
        elif XI == 'm' or 'M':
            M += 1
        elif XI == 'k' or 'K':
            K += 4
    if X == 20:
        print("Card 1: C-53 (Midnight Shadow)")
        print("Where do you want to place this card?")
        XI = input("J/M/K? ")
        if XI == 'j' or 'J':
            J += 2
        elif XI == 'm' or 'M':
            M += 4
        elif XI == 'k' or 'K':
            K += 0
    if X == 21:
        print("Card 1: C-53 (Skin)")
        print("Where do you want to place this card?")
        XI = input("J/M/K? ")
        if XI == 'j' or 'J':
            J += 3
        elif XI == 'm' or 'M':
            M += 1
        elif XI == 'k' or 'K':
            K += 2
    if X == 22:
        print("Card 1: C-53 (original)")
        print("Where do you want to place this card?")
        XI = input("J/M/K? ")
        if XI == 'j' or 'J':
            J += 2
        elif XI == 'm' or 'M':
            M += 2
        elif XI == 'k' or 'K':
            K += 2
    if X == 23:
        print("Card 1: C-53 (Kill droid)")
        print("Where do you want to place this card?")
        XI = input("J/M/K? ")
        if XI == 'j' or 'J':
            J += 1
        elif XI == 'm' or 'M':
            M += 5
        elif XI == 'k' or 'K':
            K += 0
    if X == 24:
        print("Card 1: B-69 420 (Dehumidifier)")
        print("Where do you want to place this card?")
        XI = input("J/M/K? ")
        if XI == 'j' or 'J':
            J += 3
        elif XI == 'm' or 'M':
            M += 2
        elif XI == 'k' or 'K':
            K += 1
    if X == 25:
        print("Card 1: Bargie")
        print("Where do you want to place this card?")
        XI = input("J/M/K? ")
        if XI == 'j' or 'J':
            J += 3
        elif XI == 'm' or 'M':
            M += 1
        elif XI == 'k' or 'K':
            K += 2
    if X == 26:
        print("Card 1: Rolfus Tittle")
        print("Where do you want to place this card?")
        XI = input("J/M/K? ")
        if XI == 'j' or 'J':
            J += 2
        elif XI == 'm' or 'M':
            M += 1
        elif XI == 'k' or 'K':
            K += 3
    if X == 27:
        print("Card 1: Centurion Tittle")
        print("Where do you want to place this card?")
        XI = input("J/M/K? ")
        if XI == 'j' or 'J':
            J += 0
        elif XI == 'm' or 'M':
            M += 0
        elif XI == 'k' or 'K':
            K += 4
    if X == 28:
        print("Card 1: Sistu Gunduu")
        print("Where do you want to place this card?")
        XI = input("J/M/K? ")
        if XI == 'j' or 'J':
            J += 2
        elif XI == 'm' or 'M':
            M += 2
        elif XI == 'k' or 'K':
            K += 2
    if X == 29:
        print("Card 1: Poof the Wiffle")
        print("Where do you want to place this card?")
        XI = input("J/M/K? ")
        if XI == 'j' or 'J':
            J += 3
        elif XI == 'm' or 'M':
            M += 1
        elif XI == 'k' or 'K':
            K += 2
    if X == 30:
        print("Card 1: Fluff the Wiffle")
        print("Where do you want to place this card?")
        XI = input("J/M/K? ")
        if XI == 'j' or 'J':
            J += 3
        elif XI == 'm' or 'M':
            M += 1
        elif XI == 'k' or 'K':
            K += 2
    if X == 31:
        print("Card 1: Hark Tardigast")
        print("Where do you want to place this card?")
        XI = input("J/M/K? ")
        if XI == 'j' or 'J':
            J += 3
        elif XI == 'm' or 'M':
            M += 2
        elif XI == 'k' or 'K':
            K += 1
    if X == 32:
        print("Card 1: AJ 2884")
        print("Where do you want to place this card?")
        XI = input("J/M/K? ")
        if XI == 'j' or 'J':
            J += 4
        elif XI == 'm' or 'M':
            M += 0
        elif XI == 'k' or 'K':
            K += 2
    if X == 33:
        print("Card 1: Blimpie")
        print("Where do you want to place this card?")
        XI = input("J/M/K? ")
        if XI == 'j' or 'J':
            J += 0
        elif XI == 'm' or 'M':
            M += 2
        elif XI == 'k' or 'K':
            K += 3
    if X == 34:
        print("Card 1: Kitty")
        print("Where do you want to place this card?")
        XI = input("J/M/K? ")
        if XI == 'j' or 'J':
            J += 0
        elif XI == 'm' or 'M':
            M += 0
        elif XI == 'k' or 'K':
            K += 0
    if X == 35:
        print("Card 1: Tiny Toots")
        print("Where do you want to place this card?")
        XI = input("J/M/K? ")
        if XI == 'j' or 'J':
            J += 2
        elif XI == 'm' or 'M':
            M += 0
        elif XI == 'k' or 'K':
            K += 4
    if X == 36:
        print("Card 1: Gerp")
        print("Where do you want to place this card?")
        XI = input("J/M/K? ")
        if XI == 'j' or 'J':
            J += 2
        elif XI == 'm' or 'M':
            M += 2
        elif XI == 'k' or 'K':
            K += 2
    if X == 37:
        print("Card 1: The K'hekk")
        print("Where do you want to place this card?")
        XI = input("J/M/K? ")
        if XI == 'j' or 'J':
            J += 5
        elif XI == 'm' or 'M':
            M += 0
        elif XI == 'k' or 'K':
            K += 1
    if X == 38:
        print("Card 1: The Grower Mind")
        print("Where do you want to place this card?")
        XI = input("J/M/K? ")
        if XI == 'j' or 'J':
            J += 5
        elif XI == 'm' or 'M':
            M += 0
        elif XI == 'k' or 'K':
            K += 1
    if X == 39:
        print("Card 1: Allen")
        print("Where do you want to place this card?")
        XI = input("J/M/K? ")
        if XI == 'j' or 'J':
            J += 4
        elif XI == 'm' or 'M':
            M += 1
        elif XI == 'k' or 'K':
            K += 1
    if X == 40:
        print("Card 1: Dar(Norm)")
        print("Where do you want to place this card?")
        XI = input("J/M/K? ")
        if XI == 'j' or 'J':
            J += 3
        elif XI == 'm' or 'M':
            M += 1
        elif XI == 'k' or 'K':
            K += 2
    if X == 41:
        print("Card 1: Old Durf")
        print("ALERT: CARD ACCESS OVER 42")
        print("SPECIAL CARD WORTH MORE THAN 6 POINTS TOTAL")
        print("The space guides you.")
        print("Where do you want to place this special card?")
        XI = input("J/M/K? ")
        if XI == 'j' or 'J':
            J += 5
        elif XI == 'm' or 'M':
            M += 2
        elif XI == 'k' or 'K':
            K += 0
    if X == 42:
        print("Card 1: Goerlich")
        print("The power of Rodd boosts your card's value")
        print("Where do you want to place this special card?")
        XI = input("J/M/K? ")
        if XI == 'j' or 'J':
            J += 5
        elif XI == 'm' or 'M':
            M += 2
        elif XI == 'k' or 'K':
            K += 1
    if X == 43:
        print("Card 1: TWO")
        print("ALERT: Universe CANNOT comprehend 2 2 2 2 2 2 2.. ZZZZT~")
        time.sleep(2)
        print("SPECIAL CARD WORTH MORE THAN 6 POINTS TOTAL")
        print("Where do you want to place this special card?")
        XI = input("J/M/K? ")
        if XI == 'j' or 'J':
            J += 5
        elif XI == 'm' or 'M':
            M += 4
        elif XI == 'k' or 'K':
            K += 0
    if X == 44:
        print("Card 1: ACTIVATED BEANOCHRON")
        print("ALERT: WISH DETECTED")
        print("What is yo-")
        print("Hollowood!")
        time.sleep(1)
        print("In Hollowood, you see 3 places for the card.")
        XI = input("J/M/K? ")
        if XI == 'j' or 'J':
            J += 7
        elif XI == 'm' or 'M':
            M += 0
        elif XI == 'k' or 'K':
            K += 0
    if X == 45:
        print("Card 1: B-69 420")
        print("ALERT: LARGE AMOUNTS OF DUST IN AIR!!!")
        print("*Sniff*")
        print("?drac laiceps siht ecalp ot tnaw uoy od erehW")
        XI = input("J/M/K? ")
        if XI == 'j' or 'J':
            J += 9
        elif XI == 'm' or 'M':
            M += 0
        elif XI == 'k' or 'K':
            K += 0
    if X == 46:
        print("Card 1: Finniford J. Ryan")
        print("Who are you?")
        print("which card do you give him?")
        XI = input("J/M/K? ")
        if XI == 'j' or 'J':
            J += 3
        elif XI == 'm' or 'M':
            M += 0
        elif XI == 'k' or 'K':
            K += 4
    if X == 47:
        print("Card 1: Dodecahelen")
        print("ALERT: UNIMAGINABLE POWER")
        print("%$^&*£%&^%^$&*9509*&^&*(01100001")
        XI = input("J/M/K? ")
        if XI == 'j' or 'J':
            J += 6
        elif XI == 'm' or 'M':
            M += 1
        elif XI == 'k' or 'K':
            K += 0
    if X == 48:
        print("Card 1: AllWHEAT")
        print("ALERT: Meeeeeeeeeeeeeeeerge")
        print("Mwahahahahahahaaa")
        XI = input("J/M/K? ")
        if XI == 'j' or 'J':
            J += 2
        elif XI == 'm' or 'M':
            M += 1
        elif XI == 'k' or 'K':
            K += 6
    if X == 49:
        print("Card 1: Pho Enix Ash (Phoenix Ash)")
        print("ALERT: SPY")
        print("How do you deal with him?")
        XI = input("J/M/K? ")
        if XI == 'j' or 'J':
            J += 3
        elif XI == 'm' or 'M':
            M += 3
        elif XI == 'k' or 'K':
            K += 3
    if X == 50:
        print("Card 1: MARF")
        print("ALERT: ZIMA ENERGY DETECTED")
        print("What do you give her.")
        XI = input("J/M/K? ")
        if XI == 'j' or 'J':
            J += 5
        elif XI == 'm' or 'M':
            M += 5
        elif XI == 'k' or 'K':
            K += 5

    if Y == 1:
        print("Card 2: A C.L.I.N.T.")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 2
        elif YI == 'm' or 'M':
            M += 3
        elif YI == 'k' or 'K':
            K += 1
    if Y == 2:
        print("Card 2: A P.L.I.N.T.")
        print("Where do you want to place this card?")
        YI = input("J/M/K?")
        if YI == 'j' or 'J':
            J += 1
        elif YI == 'm' or 'M':
            M += 3
        elif YI == 'k' or 'K':
            K += 2
    if Y == 3:
        print("Card 2: Dar")
        print("Where do you want to place this card?")
        YI = input("J/M/K?")
        if YI == 'j' or 'J':
            J += 4
        elif YI == 'm' or 'M':
            M += 1
        elif YI == 'k' or 'K':
            K += 1
    if Y == 4:
        print("Card 2: Pleck")
        print("Where do you want to place this card?")
        YI = input("J/M/K?")
        if YI == 'j' or 'J':
            J += 2
        elif YI == 'm' or 'M':
            M += 1
        elif YI == 'k' or 'K':
            K += 3
    if Y == 5:
        print("Card 2: Samo and Wink")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 4
        elif YI == 'm' or 'M':
            M += 1
        elif YI == 'k' or 'K':
            K += 1
    if Y == 6:
        print("Card 2: Best friend Number 1")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 3
        elif YI == 'm' or 'M':
            M += 1
        elif YI == 'k' or 'K':
            K += 1
    if Y == 7:
        print("Card 2: Best friend Number 2")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 2
        elif YI == 'm' or 'M':
            M += 2
        elif YI == 'k' or 'K':
            K += 1
    if Y == 8:
        print("Card 2: Best friend Number 3")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 1
        elif YI == 'm' or 'M':
            M += 3
        elif YI == 'k' or 'K':
            K += 2
    if Y == 9:
        print("Card 2: Best friend Number 4")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 2
        elif YI == 'm' or 'M':
            M += 1
        elif YI == 'k' or 'K':
            K += 2
    if Y == 10:
        print("Card 2: Best friend Number 5")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 1
        elif YI == 'm' or 'M':
            M += 2
        elif YI == 'k' or 'K':
            K += 1
    if Y == 11:
        print("Card 2: Best friend Number 6")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 3
        elif YI == 'm' or 'M':
            M += 1
        elif YI == 'k' or 'K':
            K += 1
    if Y == 12:
        print("Card 2: Best friend Number 7")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 1
        elif YI == 'm' or 'M':
            M += 1
        elif YI == 'k' or 'K':
            K += 4
    if Y == 13:
        print("Card 2: Peter 3 Fab")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 2
        elif YI == 'm' or 'M':
            M += 2
        elif YI == 'k' or 'K':
            K += 2
    if Y == 14:
        print("Card 2: Nermut Bundaloy (Emporer)")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 1
        elif YI == 'm' or 'M':
            M += 1
        elif YI == 'k' or 'K':
            K += 4
    if Y == 15:
        print("Card 2: Nermut Bundaloy (Crew)")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 3
        elif YI == 'm' or 'M':
            M += 2
        elif YI == 'k' or 'K':
            K += 1
    if Y == 16:
        print("Card 2: Bermut Nundaloy (Emporer)")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 4
        elif YI == 'm' or 'M':
            M += 0
        elif YI == 'k' or 'K':
            K += 2
    if Y == 17:
        print("Card 2: Bermut Nundaloy (Crew)")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 1
        elif YI == 'm' or 'M':
            M += 1
        elif YI == 'k' or 'K':
            K += 4
    if Y == 18:
        print("Card 2: Beanochron(Beano)")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 3
        elif YI == 'm' or 'M':
            M += 3
        elif YI == 'k' or 'K':
            K += 0
    if Y == 19:
        print("Card 2: Young Durf")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 1
        elif YI == 'm' or 'M':
            M += 1
        elif YI == 'k' or 'K':
            K += 4
    if Y == 20:
        print("Card 2: C-53 (Midnight Shadow)")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 2
        elif YI == 'm' or 'M':
            M += 4
        elif YI == 'k' or 'K':
            K += 0
    if Y == 21:
        print("Card 2: C-53 (Skin)")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 3
        elif YI == 'm' or 'M':
            M += 1
        elif YI == 'k' or 'K':
            K += 2
    if Y == 22:
        print("Card 2: C-53 (original)")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 2
        elif YI == 'm' or 'M':
            M += 2
        elif YI == 'k' or 'K':
            K += 2
    if Y == 23:
        print("Card 2: C-53 (Kill droid)")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 1
        elif YI == 'm' or 'M':
            M += 5
        elif YI == 'k' or 'K':
            K += 0
    if Y == 24:
        print("Card 2: B-69 420 (Dehumidifier)")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 3
        elif YI == 'm' or 'M':
            M += 2
        elif YI == 'k' or 'K':
            K += 1
    if Y == 25:
        print("Card 2: Bargie")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 3
        elif YI == 'm' or 'M':
            M += 1
        elif YI == 'k' or 'K':
            K += 2
    if Y == 26:
        print("Card 2: Rolfus Tittle")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 2
        elif YI == 'm' or 'M':
            M += 1
        elif YI == 'k' or 'K':
            K += 3
    if Y == 27:
        print("Card 2: Centurion Tittle")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 0
        elif YI == 'm' or 'M':
            M += 0
        elif YI == 'k' or 'K':
            K += 4
    if Y == 28:
        print("Card 2: Sistu Gunduu")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 2
        elif YI == 'm' or 'M':
            M += 2
        elif YI == 'k' or 'K':
            K += 2
    if Y == 29:
        print("Card 2: Poof the Wiffle")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 3
        elif YI == 'm' or 'M':
            M += 1
        elif YI == 'k' or 'K':
            K += 2
    if Y == 30:
        print("Card 2: Fluff the Wiffle")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 3
        elif YI == 'm' or 'M':
            M += 1
        elif YI == 'k' or 'K':
            K += 2
    if Y == 31:
        print("Card 2: Hark Tardigast")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 3
        elif YI == 'm' or 'M':
            M += 2
        elif YI == 'k' or 'K':
            K += 1
    if Y == 32:
        print("Card 2: AJ 2884")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 4
        elif YI == 'm' or 'M':
            M += 0
        elif YI == 'k' or 'K':
            K += 2
    if Y == 33:
        print("Card 2: Blimpie")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 0
        elif YI == 'm' or 'M':
            M += 2
        elif YI == 'k' or 'K':
            K += 3
    if Y == 34:
        print("Card 2: Kitty")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 0
        elif YI == 'm' or 'M':
            M += 0
        elif YI == 'k' or 'K':
            K += 0
    if Y == 35:
        print("Card 2: Tiny Toots")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 2
        elif YI == 'm' or 'M':
            M += 0
        elif YI == 'k' or 'K':
            K += 4
    if Y == 36:
        print("Card 2: Gerp")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 2
        elif YI == 'm' or 'M':
            M += 2
        elif YI == 'k' or 'K':
            K += 2
    if Y == 37:
        print("Card 2: The K'hekk")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 5
        elif YI == 'm' or 'M':
            M += 0
        elif YI == 'k' or 'K':
            K += 1
    if Y == 38:
        print("Card 2: The Grower Mind")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 5
        elif YI == 'm' or 'M':
            M += 0
        elif YI == 'k' or 'K':
            K += 1
    if Y == 39:
        print("Card 2: Allen")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 4
        elif YI == 'm' or 'M':
            M += 1
        elif YI == 'k' or 'K':
            K += 1
    if Y == 40:
        print("Card 2: Dar(Norm)")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 3
        elif YI == 'm' or 'M':
            M += 1
        elif YI == 'k' or 'K':
            K += 2
    if Y == 41:
        print("Card 2: Old Durf")
        print("ALERT: CARD ACCESS OVER 42")
        print("SPECIAL CARD WORTH MORE THAN 6 POINTS TOTAL")
        print("The space guides you.")
        print("Where do you want to place this special card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 5
        elif YI == 'm' or 'M':
            M += 2
        elif YI == 'k' or 'K':
            K += 0
    if Y == 42:
        print("Card 2: Goerlich")
        print("The power of Rodd boosts your card's value")
        print("Where do you want to place this special card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 5
        elif YI == 'm' or 'M':
            M += 2
        elif YI == 'k' or 'K':
            K += 1
    if Y == 43:
        print("Card 2: TWO")
        print("ALERT: Universe CANNOT comprehend 2 2 2 2 2 2 2.. ZZZZT~")
        time.sleep(2)
        print("SPECIAL CARD WORTH MORE THAN 6 POINTS TOTAL")
        print("Where do you want to place this special card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 5
        elif YI == 'm' or 'M':
            M += 4
        elif YI == 'k' or 'K':
            K += 0
    if Y == 44:
        print("Card 2: ACTIVATED BEANOCHRON")
        print("ALERT: WISH DETECTED")
        print("What is yo-")
        print("Hollowood!")
        time.sleep(1)
        print("In Hollowood, you see 3 places for the card.")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 7
        elif YI == 'm' or 'M':
            M += 0
        elif YI == 'k' or 'K':
            K += 0
    if Y == 45:
        print("Card 2: B-69 420")
        print("ALERT: LARGE AMOUNTS OF DUST IN AIR!!!")
        print("*Sniff*")
        print("?drac laiceps siht ecalp ot tnaw uoy od erehW")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 9
        elif YI == 'm' or 'M':
            M += 0
        elif YI == 'k' or 'K':
            K += 0
    if Y == 46:
        print("Card 2: Finniford J. Ryan")
        print("Who are you?")
        print("which card do you give him?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 3
        elif YI == 'm' or 'M':
            M += 0
        elif YI == 'k' or 'K':
            K += 4
    if Y == 47:
        print("Card 2: Dodecahelen")
        print("ALERT: UNIMAGINABLE POWER")
        print("%$^&*£%&^%^$&*9509*&^&*(01100001")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 6
        elif YI == 'm' or 'M':
            M += 1
        elif YI == 'k' or 'K':
            K += 0
    if Y == 48:
        print("Card 2: AllWHEAT")
        print("ALERT: Meeeeeeeeeeeeeeeerge")
        print("Mwahahahahahahaaa")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 2
        elif YI == 'm' or 'M':
            M += 1
        elif YI == 'k' or 'K':
            K += 6
    if Y == 49:
        print("Card 2: Pho Enix Ash (Phoenix Ash)")
        print("ALERT: SPY")
        print("How do you deal with him?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 3
        elif YI == 'm' or 'M':
            M += 3
        elif YI == 'k' or 'K':
            K += 3
    if Y == 50:
        print("Card 2: MARF")
        print("ALERT: ZIMA ENERGY DETECTED")
        print("What do you give her.")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 5
        elif YI == 'm' or 'M':
            M += 5
        elif YI == 'k' or 'K':
            K += 5

    if Z == 1:
        print("Card 3: A C.L.I.N.T.")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 2
        elif YI == 'm' or 'M':
            M += 3
        elif YI == 'k' or 'K':
            K += 1
    if Z == 2:
        print("Card 3: A P.L.I.N.T.")
        print("Where do you want to place this card?")
        YI = input("J/M/K?")
        if YI == 'j' or 'J':
            J += 1
        elif YI == 'm' or 'M':
            M += 3
        elif YI == 'k' or 'K':
            K += 2
    if Z == 3:
        print("Card 3: Dar")
        print("Where do you want to place this card?")
        YI = input("J/M/K?")
        if YI == 'j' or 'J':
            J += 4
        elif YI == 'm' or 'M':
            M += 1
        elif YI == 'k' or 'K':
            K += 1
    if Z == 4:
        print("Card 3: Pleck")
        print("Where do you want to place this card?")
        YI = input("J/M/K?")
        if YI == 'j' or 'J':
            J += 2
        elif YI == 'm' or 'M':
            M += 1
        elif YI == 'k' or 'K':
            K += 3
    if Z == 5:
        print("Card 3: Samo and Wink")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 4
        elif YI == 'm' or 'M':
            M += 1
        elif YI == 'k' or 'K':
            K += 1
    if Z == 6:
        print("Card 3: Best friend Number 1")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 3
        elif YI == 'm' or 'M':
            M += 1
        elif YI == 'k' or 'K':
            K += 1
    if Z == 7:
        print("Card 3: Best friend Number 2")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 2
        elif YI == 'm' or 'M':
            M += 2
        elif YI == 'k' or 'K':
            K += 1
    if Z == 8:
        print("Card 3: Best friend Number 3")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 1
        elif YI == 'm' or 'M':
            M += 3
        elif YI == 'k' or 'K':
            K += 2
    if Z == 9:
        print("Card 3: Best friend Number 4")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 2
        elif YI == 'm' or 'M':
            M += 1
        elif YI == 'k' or 'K':
            K += 2
    if Z == 10:
        print("Card 3: Best friend Number 5")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 1
        elif YI == 'm' or 'M':
            M += 2
        elif YI == 'k' or 'K':
            K += 1
    if Z == 11:
        print("Card 3: Best friend Number 6")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 3
        elif YI == 'm' or 'M':
            M += 1
        elif YI == 'k' or 'K':
            K += 1
    if Z == 12:
        print("Card 3: Best friend Number 7")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 1
        elif YI == 'm' or 'M':
            M += 1
        elif YI == 'k' or 'K':
            K += 4
    if Z == 13:
        print("Card 3: Peter 3 Fab")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 2
        elif YI == 'm' or 'M':
            M += 2
        elif YI == 'k' or 'K':
            K += 2
    if Z == 14:
        print("Card 3: Nermut Bundaloy (Emporer)")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 1
        elif YI == 'm' or 'M':
            M += 1
        elif YI == 'k' or 'K':
            K += 4
    if Z == 15:
        print("Card 3: Nermut Bundaloy (Crew)")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 3
        elif YI == 'm' or 'M':
            M += 2
        elif YI == 'k' or 'K':
            K += 1
    if Z == 16:
        print("Card 3: Bermut Nundaloy (Emporer)")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 4
        elif YI == 'm' or 'M':
            M += 0
        elif YI == 'k' or 'K':
            K += 2
    if Z == 17:
        print("Card 3: Bermut Nundaloy (Crew)")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 1
        elif YI == 'm' or 'M':
            M += 1
        elif YI == 'k' or 'K':
            K += 4
    if Z == 18:
        print("Card 3: Beanochron(Beano)")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 3
        elif YI == 'm' or 'M':
            M += 3
        elif YI == 'k' or 'K':
            K += 0
    if Z == 19:
        print("Card 3: Young Durf")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 1
        elif YI == 'm' or 'M':
            M += 1
        elif YI == 'k' or 'K':
            K += 4
    if Z == 20:
        print("Card 3: C-53 (Midnight Shadow)")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 2
        elif YI == 'm' or 'M':
            M += 4
        elif YI == 'k' or 'K':
            K += 0
    if Z == 21:
        print("Card 3: C-53 (Skin)")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 3
        elif YI == 'm' or 'M':
            M += 1
        elif YI == 'k' or 'K':
            K += 2
    if Z == 22:
        print("Card 3: C-53 (original)")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 2
        elif YI == 'm' or 'M':
            M += 2
        elif YI == 'k' or 'K':
            K += 2
    if Z == 23:
        print("Card 3: C-53 (Kill droid)")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 1
        elif YI == 'm' or 'M':
            M += 5
        elif YI == 'k' or 'K':
            K += 0
    if Z == 24:
        print("Card 3: B-69 420 (Dehumidifier)")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 3
        elif YI == 'm' or 'M':
            M += 2
        elif YI == 'k' or 'K':
            K += 1
    if Z == 25:
        print("Card 3: Bargie")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 3
        elif YI == 'm' or 'M':
            M += 1
        elif YI == 'k' or 'K':
            K += 2
    if Z == 26:
        print("Card 3: Rolfus Tittle")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 2
        elif YI == 'm' or 'M':
            M += 1
        elif YI == 'k' or 'K':
            K += 3
    if Z == 27:
        print("Card 3: Centurion Tittle")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 0
        elif YI == 'm' or 'M':
            M += 0
        elif YI == 'k' or 'K':
            K += 4
    if Z == 28:
        print("Card 3: Sistu Gunduu")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 2
        elif YI == 'm' or 'M':
            M += 2
        elif YI == 'k' or 'K':
            K += 2
    if Z == 29:
        print("Card 3: Poof the Wiffle")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 3
        elif YI == 'm' or 'M':
            M += 1
        elif YI == 'k' or 'K':
            K += 2
    if Z == 30:
        print("Card 3: Fluff the Wiffle")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 3
        elif YI == 'm' or 'M':
            M += 1
        elif YI == 'k' or 'K':
            K += 2
    if Z == 31:
        print("Card 3: Hark Tardigast")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 3
        elif YI == 'm' or 'M':
            M += 2
        elif YI == 'k' or 'K':
            K += 1
    if Z == 32:
        print("Card 3: AJ 2884")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 4
        elif YI == 'm' or 'M':
            M += 0
        elif YI == 'k' or 'K':
            K += 2
    if Z == 33:
        print("Card 3: Blimpie")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 0
        elif YI == 'm' or 'M':
            M += 2
        elif YI == 'k' or 'K':
            K += 3
    if Z == 34:
        print("Card 3: Kitty")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 0
        elif YI == 'm' or 'M':
            M += 0
        elif YI == 'k' or 'K':
            K += 0
    if Z == 35:
        print("Card 3: Tiny Toots")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 2
        elif YI == 'm' or 'M':
            M += 0
        elif YI == 'k' or 'K':
            K += 4
    if Z == 36:
        print("Card 3: Gerp")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 2
        elif YI == 'm' or 'M':
            M += 2
        elif YI == 'k' or 'K':
            K += 2
    if Z == 37:
        print("Card 3: The K'hekk")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 5
        elif YI == 'm' or 'M':
            M += 0
        elif YI == 'k' or 'K':
            K += 1
    if Z == 38:
        print("Card 3: The Grower Mind")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 5
        elif YI == 'm' or 'M':
            M += 0
        elif YI == 'k' or 'K':
            K += 1
    if Z == 39:
        print("Card 3: Allen")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 4
        elif YI == 'm' or 'M':
            M += 1
        elif YI == 'k' or 'K':
            K += 1
    if Z == 40:
        print("Card 3: Dar(Norm)")
        print("Where do you want to place this card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 3
        elif YI == 'm' or 'M':
            M += 1
        elif YI == 'k' or 'K':
            K += 2
    if Z == 41:
        print("Card 3: Old Durf")
        print("ALERT: CARD ACCESS OVER 42")
        print("SPECIAL CARD WORTH MORE THAN 6 POINTS TOTAL")
        print("The space guides you.")
        print("Where do you want to place this special card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 5
        elif YI == 'm' or 'M':
            M += 2
        elif YI == 'k' or 'K':
            K += 0
    if Z == 42:
        print("Card 3: Goerlich")
        print("The power of Rodd boosts your card's value")
        print("Where do you want to place this special card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 5
        elif YI == 'm' or 'M':
            M += 2
        elif YI == 'k' or 'K':
            K += 1
    if Z == 43:
        print("Card 3: TWO")
        print("ALERT: Universe CANNOT comprehend 2 2 2 2 2 2 2.. ZZZZT~")
        time.sleep(2)
        print("SPECIAL CARD WORTH MORE THAN 6 POINTS TOTAL")
        print("Where do you want to place this special card?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 5
        elif YI == 'm' or 'M':
            M += 4
        elif YI == 'k' or 'K':
            K += 0
    if Z == 44:
        print("Card 3: ACTIVATED BEANOCHRON")
        print("ALERT: WISH DETECTED")
        print("What is yo-")
        print("Hollowood!")
        time.sleep(1)
        print("In Hollowood, you see 3 places for the card.")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 7
        elif YI == 'm' or 'M':
            M += 0
        elif YI == 'k' or 'K':
            K += 0
    if Z == 45:
        print("Card 3: B-69 420")
        print("ALERT: LARGE AMOUNTS OF DUST IN AIR!!!")
        print("*Sniff*")
        print("?drac laiceps siht ecalp ot tnaw uoy od erehW")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 9
        elif YI == 'm' or 'M':
            M += 0
        elif YI == 'k' or 'K':
            K += 0
    if Z == 46:
        print("Card 3: Finniford J. Ryan")
        print("Who are you?")
        print("which card do you give him?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 3
        elif YI == 'm' or 'M':
            M += 0
        elif YI == 'k' or 'K':
            K += 4
    if Z == 47:
        print("Card 3: Dodecahelen")
        print("ALERT: UNIMAGINABLE POWER")
        print("%$^&*£%&^%^$&*9509*&^&*(01100001")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 6
        elif YI == 'm' or 'M':
            M += 1
        elif YI == 'k' or 'K':
            K += 0
    if Z == 48:
        print("Card 3: AllWHEAT")
        print("ALERT: Meeeeeeeeeeeeeeeerge")
        print("Mwahahahahahahaaa")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 2
        elif YI == 'm' or 'M':
            M += 1
        elif YI == 'k' or 'K':
            K += 6
    if Z == 49:
        print("Card 3: Pho Enix Ash (Phoenix Ash)")
        print("ALERT: SPY")
        print("How do you deal with him?")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 3
        elif YI == 'm' or 'M':
            M += 3
        elif YI == 'k' or 'K':
            K += 3
    if Z == 50:
        print("Card 3: MARF")
        print("ALERT: ZIMA ENERGY DETECTED")
        print("What do you give her.")
        YI = input("J/M/K? ")
        if YI == 'j' or 'J':
            J += 5
        elif YI == 'm' or 'M':
            M += 5
        elif YI == 'k' or 'K':
            K += 5

    score = str(J + M + K)
    print("Congratulations! You got " + score)
    print("Restart? Y/N ")
    cmd = input("Restart")
    if cmd == 'y' or 'Y':
        print("BEGIN!")
        Thread(target = startfunc).start()
    if cmd == 'n' or 'N':
        print("Have a good one!")
def sound():
    playsound('missiontozyxx.wav')

if __name__ == '__main__':
    Thread(target=startfunc).start()
    Thread(target=sound).start()
