import random

#decides what the computer plays
def computer_rps():
    x = random.randint(1, 3)
    rps = int(x)
    return rps


#beginning greetings
print("Tervetuloa kivi-paperi-sakset peliin!")
print("Aloitamme pelaamisen:")
print("Kun haluat lopettaa, valitse joku muu numero kuin 1-3.")


#the main game
while True:
    try:
        x = computer_rps()
        rps = int(x)
        print(" ")
        x = input("Jos valitset kiven, paina 1. Jos valitset paperin, anna 2. Jos valitset sakset, paina 3.")
        valinta = int(x)
        if valinta == 1:
            print("Pelaat kiven.")
            if rps == 1:
                print("ja niin pelasi tietokonekin, eli tasapeli!\n"
                      "\n")
            elif rps == 2:
                print("Sinä häviät, koska tietokone pelasi paperin.!\n"
                      "\n")
            elif rps == 3:
                print("Tietokone häviää, koska pelasi sakset.\n"
                      "\n")
        elif valinta == 2:
            print("Pelaat paperin!")
            if rps == 2:
                print("Tasapeli\n"
                      "\n")
            elif rps == 1:
                print("Sinä voitat, koska tietokone pelasi kiven.\n"
                      "\n")
            elif rps == 3:
                print("Sinä häviät, koska tietokone otti sakset!\n"
                      "\n")
        elif valinta == 3:
            print("Pelaat sakset.")
            if rps == 1:
                print("Sinä häviät, koska tietokoneella on kivi.\n"
                      "\n")
            elif rps == 2:
                print("Sinä voitat, koska kone valitsi paperin!\n"
                      "\n")
            elif rps == 3:
                print("Tasapeli, molemmilla sakset!\n"
                      "\n")
        else:
            #to end the game
            break
    #if the player tries to input a letter or something similar
    except:
        print("Peli ottaa vain numero komentoja 1-3, tai muita numeroita kun haluat lopettaa.")
        continue

#ending thanks
print("Kiitos pelaamisesta.")