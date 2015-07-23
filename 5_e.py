# Ivan Vucetic
# vuceta87@yahoo.com
#
# Challenge 5 -easy; r/dailyprogrammer
# 23/07/2015

#Password protected program


from getpass import getpass

userdata = open("5_e_data.txt")

lines = userdata.read()  # cita objekat userdata i ucitava u lines
splited = lines.split()  # deli lines u redove koje smesta u listu.po indexu pristupamo
userdata.close()                            

realuser = splited[0]
realpass = splited[1]

print "Unesite korisnicko ime"
a_user = raw_input(">>> ")
print "Unesite sifru"
a_pass = getpass(">>> ") #getpass omogucava da se ne vidi sta korisnik kuca

if (a_user == realuser) and (a_pass == realpass):
    print "Good, good..."
else:
    print "ERROR skrlj! Try different combination." 

'''
drugo resenje, pokupljeno s neta, za vise korisnika:
korisnicka imena i sifre su smestene u jednom fajlu, npr:

    ivan qwerty
    petar 123
    ivan 123
    petar abc
    
korisnik unese svoj username i pass, a program ih spaja i trazi takav red u fajlu

    if a_user + " " + a_pass in lines:
        print "good"
    else:
        print "bad"
        
'''
    
    
    

