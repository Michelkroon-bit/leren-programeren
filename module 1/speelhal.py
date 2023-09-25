aantal_personen = int(4)
prijs = 7.45
vip_vr_gameset = 0.37

uitkomst = prijs * aantal_personen
print ('de prijs per persoon is' ,uitkomst,'euro')

uitkomst_vip = vip_vr_gameset / 5

uitkomst_vip1 = uitkomst_vip * 45

uitkomst_vip2 = round (uitkomst_vip1 *4)
print ('de prijs voor de vip vr gameseat is',uitkomst_vip2,'euro')