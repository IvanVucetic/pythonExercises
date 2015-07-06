# Ivan Vucetic
# vuceta87@yahoo.com
#
# Challenge 4 -easy; r/dailyprogrammer
# 01/07/2015

#Password generator

import random

# dodati jos neku grupu po potrebi; mogli smo i samo da izpisemo znakove
m_slova = [chr(x) for x in range(97,123)]
v_slova = [chr(x) for x in range(65,91)]
cifre = [str(x) for x in range(0,10)]

znakovi = m_slova + v_slova + cifre
pass_list = list()

print "Koliko sifara zelite da izgenerisete?"
broj_sifri = int(raw_input("> "))

print "Koliko zelite da svaka sifra bude dugacka?"
duzina = int(raw_input("> "))

for i in range(0, broj_sifri):
    # random.randint(a, b) --------> a <= N <= b
    # iz znakova uzimamo element sa random pozicije i stavljamo u pass_list
    for j in range (0, duzina):
        pass_list.append(znakovi[random.randint(0,len(znakovi)-1)])
        password = ''.join(pass_list)
    print password
    pass_list = list() # moramo da obrisemo listu da ne dodajemo na staro
    
 # dosta elegantnije resenje drugog lika:
 # for b in range(bar):
 #      place = random.randint(0, len(chars) - 1)
 #      result = result + chars[place]
 #   

