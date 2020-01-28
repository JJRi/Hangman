
import random


#tekee tulosteen hirsipuun tilasta
def print_hangman(counter):
    hirsipuu=['jalusta', 'pystypuu', 'poikkipuu', 'tukipuu', 'köysi', 'pää', 'keho', 'jalat', 'kädet']
    if counter > 0:
        print('Hirsipuussa on: '+ str(hirsipuu[0:counter]))
    return


#pelin pääfunktio:
def main_game():
#pelin valmistelevat asiat aluksi
#haetaan kaikki sanat sanakirja-tiedostosta
    print('Arvon sinulle sanan:')
    f = open("sanoja.txt", "r")
    word_list_dirt = f.readlines()
    f.close()
    sana_lista = []
#siivotaan turhat lopukkeet pois sanoista
    for w in word_list_dirt:
        sana_lista.append(w.replace('\n', ''))
#arvotaan pelattava sana
    word = random.choice(sana_lista)
    print('_ ' * len(word))
    arvatut_kirjaimet = []
    peli_lista = []
#pelattavasta sanasta tehdään lista, johon täydennetään kirjaimia
    for letter in word:
        peli_lista.append('_ ')
    counter = 0
#pelin pääkierto
    while True:
        empty_spaces = peli_lista.count('_ ')
        the_guess = input('Arvaa kirjain: ')
        the_guess = the_guess.lower()
        if the_guess in word:
            print('Arvasit oikein!')
            print_hangman(counter)
        else:
            print('Väärin meni!')
            counter += 1
            print_hangman(counter)
        arvatut_kirjaimet.append(the_guess)
        for position, item in enumerate(word):
            if item == the_guess:
                peli_lista.insert(position, the_guess)
                peli_lista.pop(position + 1)
        print(peli_lista)
        print('Olet arvannut: ', arvatut_kirjaimet)
        print(' ')
        print(' ')
        print(' ')
        print(' ')
#tarkistetaan onko tullut voittoa tai tappiota
        still_game_on = peli_lista.count('_ ')
#pelin lopputuloksen ilmoittaminen
        if still_game_on == 0:
            print('Voitit. Onnea!')
            break
        if counter >= 9:
            print('Hävisit')
            print('Sana oli:', word)
            break
#selvitetään jatkuuko pelaaminen, jos voitto tai tappio
    pelaatko = 'a'
    while pelaatko.lower != 'k' or 'e':
        pelaatko = str(input('Pelaatko vielä? (k/e)? '))
        if pelaatko.lower() == 'k':
            main_game()
        if pelaatko.lower() == 'e':
            print('Kiitoksia pelaamisesta!')
            quit()
    return

#itse ohjelma alkaa tästä
if __name__ == "__main__":
    print('Tervetuloa Hirsipuuhun!\n'
          'Aloitetaan pelaaminen.\n'
          '\n')
    main_game()
