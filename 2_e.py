# Ivan Vucetic
# vuceta87@yahoo.com
#
# Challenge 2 -easy; r/dailyprogrammer
# 29/06/2015

def kamata():
    print "Koliko godina planirate da stedite?"
    br_god = raw_input("> ")

    print "Koliko planirate mesecno da ulazete?"
    mesecno = raw_input("> ")

    print "Kolika je godisnja kamatna stopa?"
    stopa = raw_input("> ")

    glavnica = 0
    brojac = 0

    for brojac in range (0,int(br_god)):
        glavnica = glavnica + glavnica * (int(stopa)/100.0) + 12 * int(mesecno)
        brojac =+ 1

    print "Nakon zadatog perioda imacete ukupno %s EUR" % int(glavnica)
    print "Kamata u narednoj godini iznosice %s EUR" % round((glavnica * (int(stopa)/100.0)),2)
    print "Na osnovu kamate, imacete mesecna primanja od %s EUR" % round((glavnica * (int(stopa)/1200.0)),2)
    exit(0)

def rata():
    print "Koliko godina planirate da stedite? (5/10/15/20/25/30/35/40)"
    x = True
    while x == True:
        br_god = int(raw_input("> "))

        if br_god not in (5,10,15,20,25,30,35,40):
            print "Unesite jednu od ponudjenih vrednosti."
        else:
            x = False

    print "Kolika mesecna primanja zelite da imate od kamate?"
    #cgk - ciljana godisnja kamata
    cgk = 12 * int(raw_input("> "))

    # ciljana glavnica uz 8% neto kamate
    nest_egg = cgk / 0.08

    rata = 0
    # Faktori preuzeti iz knjige 'Total Money Makeover', autor Dave Ramsey
    if br_god == 5:
        rata = nest_egg * 0.013610
    elif br_god == 10:
        rata = nest_egg * 0.005466
    elif br_god == 15:
        rata = nest_egg * 0.002890
    elif br_god == 20:
        rata = nest_egg * 0.001698
    elif br_god == 25:
        rata = nest_egg * 0.001051
    elif br_god == 30:
        rata = nest_egg * 0.000671
    elif br_god == 35:
        rata = nest_egg * 0.000436
    elif br_god == 40:
        rata = nest_egg * 0.000286

    print "Da biste za ", br_god, " godina imali zeljena primanja, uz 8% neto kamate,"
    print "morate ulagati %s EUR svakog meseca." % round(rata, 2)
    exit(0)

print "MALI FINANSIJSKI KALKULATOR"
print "-----"
print "Ukoliko zelite da saznate koliko cete primati kamate vasim tempom stednje, unesite '1'."
print "--"
print "Ukoliko vas zanima koliko treba da stedite svakog meseca kako biste"
print "imali odgovarajucu zaradu od kamate kasnije, unesite '2'."

while True:

    izbor = int(raw_input("> "))

    if izbor == 1:
        kamata()
    elif izbor == 2:
        rata()
    else:
        print "Unesite '1' ili '2'."
