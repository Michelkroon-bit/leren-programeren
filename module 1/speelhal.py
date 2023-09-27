aantal_personen = int(input('hoeveel personen zijn er'))
prijs_per_persoon_in_centen = int(7.45)
vip_vr_gameset_in_centen = int(37)

uitkomst = prijs_per_persoon * aantal_personen
print ('de prijs per persoon is' ,uitkomst,'euro')

uitkomst_vip = vip_vr_gameset / 5

uitkomst_vip1 = uitkomst_vip * 45

uitkomst_vip2 = (uitkomst_vip1 *4)
totaal = int(round(uitkomst_vip1 , 2))
print ('de prijs voor de vip vr gameseat is',uitkomst_vip2,'euro')

totaal = uitkomst + uitkomst_vip2

print(f'Dit geweldige dagje-uit met {aantal_personen} mensen in de Speelhal met 45 minuten VR kost je maar',totaal,'eurocent')