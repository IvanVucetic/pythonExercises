# Ivan Vucetic
# vuceta87@yahoo.com
#
# Challenge 3 -easy; r/dailyprogrammer
# 01/07/2015

sifrarnik = {'a':'d','b':'e','c':'f','d':'g','e':'h','f':'i','g':'j','h':'k',
'i':'l','j':'m','k':'n','l':'o','m':'p','n':'q','o':'r','p':'s','q':'t','r':'u',
's':'v','t':'w','u':'x','v':'y','w':'z','x':'a','y':'b','z':'c', ' ':' ', 
',':',','.':'.','!':'!','?':'?'}

# obrnemo recnik za desifrovanje
desifrator = {v: k for k, v in sifrarnik.items()} 

def sifriraj():
    print "Unesite frazu koju zelite da sifrirate."
    in_word = raw_input("> ")

    # list() ce frazu da pretvori u listu slova; 'ivan' --> 'i','v','a','n'
    in_list = list(in_word)
    out_list = list()
    #prevod
    for i in range(0, len(in_list)):
        out_list.append(sifrarnik[in_list[i]])

    # join() spaja listu karaktera u string
    out_word = ''.join(out_list)

    print "Prevod vase fraze je:"
    print out_word
    print "---"
        
def desifruj():
    print "Unesite frazu koju zelite da desifrujete."
    in_word = raw_input("> ")

    in_list = list(in_word)
    out_list = list()
    #prevod
    for i in range(0, len(in_list)):
        out_list.append(desifrator[in_list[i]]) #jedina razlika

    out_word = ''.join(out_list)

    print "Prevod vase fraze je:"
    print out_word
    print "---"        

# Ovde pocinje program:

print "Dobrodosli u Sifrarnik!"

while True:
    print "Zelite li da (1) sifrirate tekst ili da ga (2) desifrujete?"

    izbor = raw_input("> ")
    if izbor == '1':
        sifriraj()
    elif izbor == '2':
        desifruj()
    else:
        print "Unesite 1 da sifrirate tekst ili 2 da desifrujete."
        print "---"
        
