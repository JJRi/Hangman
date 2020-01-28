#Globaalit muuttujat
peli_tila = True
winner = True
arvattava_sana="Suihkari"
nmbr_guess=0
peli_lista = []
counter=0


#TODO näytä sana tyhjät ja arvatut kirjaimet -> tee lista
#TODO arvattavan sanan hakeminen listasta
#peruspeli toimii



#aloitus funktio, tervetuloa pelaamaan
def welcome_game():
    global arvattava_sana
    print('Tervetuloa Hirsipuuhun!\n'
          'Aloitetaan pelaaminen.\n'
          '\n')
    sanan_pituus = len(arvattava_sana)
    arvattava_sana=arvattava_sana.lower()
    print('Pelattava sana:')
    print('_ ' * sanan_pituus)
    print('\n'*2)
    return


#tekee tulosteen hirsipuun tilasta
def print_hangman(counter):
    hirsipuu=['jalusta', 'pystypuu', 'poikkipuu', 'tukipuu', 'köysi', 'pää', 'keho', 'jalat', 'kädet']
    if counter > 0:
        print('Hirsipuussa on: '+ str(hirsipuu[0:counter]))
    return


#arvauksen vastaanottaminen ja muuttaminen pieneksi kirjaimeksi
def make_guess():
    players_guess=str(input('Arvaa kirjain'))
    players_guess=players_guess.lower()
    return players_guess


#näyttää pelattavan sanan pelin alussa
def display_word():
    for letter in arvattava_sana:
        peli_lista.append('_ ')
    print(peli_lista)
    return


#pelin pääfunktio, tarkastaa onko arvaus oikein ja palauttaa tuloksen
def determine_result(the_guess):
    global counter
    empty_spaces = peli_lista.count('_ ')
    for position, item in enumerate(arvattava_sana):
        if item == the_guess:
            peli_lista.insert(position, the_guess)
            peli_lista.pop(position+1)
    print(peli_lista)
    check_if_letter_in_word = peli_lista.count('_ ')
    if check_if_letter_in_word >= empty_spaces:
        print ("väärin meni")
        counter = counter + 1
    return


#tarkistaa häviääkö pelaaja
def check_if_loose():
    global peli_tila
    global winner
    if counter == 9:
        peli_tila = False
        winner = False
    return


#tarkistaa voittaako pelaaja
def check_if_win():
    global peli_tila
    empty_left=int(peli_lista.count('_ '))
    if empty_left == 0:
        peli_tila = False
    return


#pelin pääfunktio
def main_game():
    while peli_tila==True:
        the_guess=make_guess()
        determine_result(the_guess)
        print_hangman(counter)
        check_if_win()
        check_if_loose()
    return

#itse ohjelma alkaa tästä
welcome_game()
display_word()
main_game()
#pelin lopputuloksen ilmoittaminen
if winner == True:
    print('Voitit')
elif winner == False:
    print('Hävisit')
print('Kiitoksia pelaamisesta!')
