word = 'banaani'
peli_lista = []
for letter in word:
    peli_lista.append('_ ')
counter = 0
the_guess = 'a'
empty_spaces = peli_lista.count('_ ')
the_guess = the_guess.lower()
print(the_guess)
print(peli_lista)
print(word)
for position, letter in enumerate(word):
    print(position)
    if letter == the_guess:
        print(peli_lista)
        print(position)
        peli_lista.insert(position, the_guess)
        print(peli_lista)
        peli_lista.pop(position+1)
print(peli_lista)
check_if_letter_in_word = peli_lista.count('_ ')
if check_if_letter_in_word >= empty_spaces:
    print ("väärin meni")
    counter = counter + 1
