peli = True
arvauksia = 0
sana = 'suihkuhävittäjä'
uusi_kirjain = " "


def aloitus_ruutu():
    print('\n'
          '\n'
          'Tervetuloa hirsipuu-pelin pariin!\n'
          '\n')


while peli == True:

    #uusi_ruutu tuo pelitulosteen ruutuun ja rytmittää peliä.
    def tulos_ruutu(arvauksia):
        if arvauksia == 9:
            print('*********************************************')
            print('Hirsipuussa on kaikki:\n'
                  'Jalusta, pystypuu, vaakapuu, tukipuu, köysi,\n'
                  'pää, keho, jalat kädet.')
            print('*********************************************')
        elif arvauksia == 8:
            print('*********************************************')
            print('Hirsipuussa on:\n'
                  'Jalusta, pystypuu, vaakapuu, tukipuu, köysi,\n'
                  'pää, keho, jalat.')
            print('*********************************************')
        elif arvauksia ==7:
            print('*********************************************')
            print('Hirsipuussa on:\n'
                  'Jalusta, pystypuu, vaakapuu, tukipuu, köysi,\n'
                  'pää, keho, jalat.')
            print('*********************************************')
        elif arvauksia == 6:
            print('*********************************************')
            print('Hirsipuussa on:\n'
                  'Jalusta, pystypuu, vaakapuu, tukipuu, köysi,\n'
                  'pää, keho.')
            print('*********************************************')
        elif arvauksia == 5:
            print('*********************************************')
            print('Hirsipuussa on:\n'
                  'Jalusta, pystypuu, vaakapuu, tukipuu, köysi,\n'
                  'pää.')
            print('*********************************************')
        elif arvauksia == 4:
            print('*********************************************')
            print('Hirsipuussa on:\n'
                  'Jalusta, pystypuu, vaakapuu, tukipuu, köysi.')
            print('*********************************************')
        elif arvauksia == 3:
            print('*********************************************')
            print('Hirsipuussa on:\n'
                  'Jalusta, pystypuu, vaakapuu.')
            print('*********************************************')
        elif arvauksia == 2:
            print('*********************************************')
            print('Hirsipuussa on:\n'
                  'Jalusta, pystypuu.')
            print('*********************************************')
        elif arvauksia == 1:
            print('*********************************************')
            print('Hirsipuussa on:\n'
                  'Jalusta.')
            print('*********************************************')
        elif arvauksia == 0:
            print('*********************************************')
            print('Hirsipuussa ei ole\n'
                  'vielä yhtään mitään.')
            print('*********************************************')

    def display_word(sana):

        x = len(sana)
        word_lenght = int(x)
        print('\n' * 2)
        print('_ ' * word_lenght)

    def game_turn(game_status='continue'):

        x = input('Arvaatko kirjaimen vai koko sanan?\n'
              'Paina valitse 1, jos kirjain ja valitse 2 jos arvaat sanan.')
        valinta = int(x)
        if valinta == 1:
            uusi_kirjain = str(input('Anna kirjain:'))

        return uusi_kirjain
        if valinta == 2:
            uusi_arvaus = input('Uusi arvauksesi on:')
            if uusi_arvaus == sana:
                print('Voitit')
                game_status = 'win'
        return game_status
    def hit_or_miss(uusi_kirjain):
        global tulos
        tulos = None
        if uusi_kirjain in sana:
            tulos = True
        else:
            tulos = False
        return tulos

    display_word(sana)
    game_status = game_turn()
    arvauksia += 1
    print(uusi_kirjain)
    hit_or_miss(uusi_kirjain)
    print(tulos)
    print(game_status)
    if game_status == 'win':
        peli = False

