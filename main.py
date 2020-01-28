import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.properties import ObjectProperty
import random

#Globaalit variaabelit:
counter = 0
arvattava_sana = []
kierroksen_sana = ' '
arvatut_sanat = []
class Hangman(Widget):
    sana = ObjectProperty(None)
    kirjain = ObjectProperty(None)
    arvaus = ObjectProperty(None)
    tulos = ObjectProperty(None)

#pelaamisen aloittava funktio
    def game(self):
        global arvattava_sana
        global kierroksen_sana

        self.tulos.source = 'Hang00.png'
        arvattava_sana = []
#haetaan sanakirjasta pelattavat sanat
        pelin_sanat = []
        with open('sanakirja.txt', 'r') as tiedosto:
            pelin_sanat = [joka_sana.rstrip() for joka_sana in tiedosto.readlines()]
#arvotaan pelattava sana
        kierroksen_sana = random.choice(pelin_sanat)
#muutetaan kierroksen sana isoiksi kirjaimiksi
        kierroksen_sana = kierroksen_sana.upper()
        for letter in kierroksen_sana:
            arvattava_sana.append('_ ')
        show_word = ' '.join(arvattava_sana)
        self.sana.text = show_word
        return

#tämä metodi hoitaa arvauksen ja tarkistaa onko kirjain pelattavassa sanassa
    def play(self):
        global arvattava_sana
        global kierroksen_sana
        global counter
        made_guess = self.arvaus.text
        made_guess = made_guess.upper()
        print(made_guess)
        print(arvattava_sana)
#laskee kuinka paljon on tyhjää arvattavassa sanassa
        empty_spaces = arvattava_sana.count('_ ')
#varsinainen kirjainten etsiminen ja sijoittaminen
        for position, item in enumerate(kierroksen_sana):
            if item == made_guess:
                arvattava_sana.insert(position, made_guess)
                arvattava_sana.pop(position + 1)
        print(arvattava_sana)
#pelitilanteen muodostaminen arvattavasta sanasta
        show_word = ' '.join(arvattava_sana)
        self.sana.text = show_word
        check_if_letter_in_word = arvattava_sana.count('_ ')
        if check_if_letter_in_word >= empty_spaces:
            print("väärin meni")
            counter = counter + 1
            print(counter)
#lisätään kirjain arvattujen kirjaimien joukkoon
        self.kirjain.text = self.kirjain.text + ' ' + made_guess + ','
#Hirsipuu kuvan päivittäminen

        if counter >= 0:
            self.tulos.source = 'Hang0{}.png'.format(counter)
        if counter >= 9:
            self.sana.text = 'Hävisit tämän pelin. Aloita uudestaan painamalla \" Aloita alusta \"'
        #if counter > 0:
        #    self.tulos.text = 'Hirsipuussa on: ' + str(hirsipuu[0:counter])
        #if counter >= 9:
        #    self.tulos.text = 'Hävisit luuseri!!!'
        self.arvaus.text = ''
        return



    def game2(self):
        global arvattava_sana
        global kierroksen_sana
        global counter

        arvattava_sana = []
        self.tulos.source = 'Hang00.png'
        self.kirjain.text = 'Arvatut kirjaimet:'
        counter = 0
#haetaan sanakirjasta pelattavat sanat
        pelin_sanat = []
        with open('sanakirja.txt', 'r') as tiedosto:
            pelin_sanat = [joka_sana.rstrip() for joka_sana in tiedosto.readlines()]
#arvotaan pelattava sana
        kierroksen_sana = random.choice(pelin_sanat)
#muutetaan kierroksen sana isoiksi kirjaimiksi
        kierroksen_sana = kierroksen_sana.upper()
        for letter in kierroksen_sana:
            arvattava_sana.append('_ ')
        show_word = ' '.join(arvattava_sana)
        self.sana.text = show_word
        return


    def lopeta(self):
        exit()






class HirsipuuApp(App):

    def build(self):
        return Hangman()



if __name__ == '__main__':
    HirsipuuApp().run()

