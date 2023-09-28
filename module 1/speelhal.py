aantal_personen = int(input('hoeveel personen zijn er'))
vip_vr_gameset=int(input('hoeveel minuten vr wil je'))



PRIJS_PER_PERSOON=745 #CENT
VIP_VR_GAMESET=37#CENT




uitkomst = PRIJS_PER_PERSOON * aantal_personen
print (f'de prijs per persoon is',uitkomst,'cent')


vr_vip1 = VIP_VR_GAMESET * vip_vr_gameset
vr_vip2 = vr_vip1 * 45


uitkomst_vip2 = (vr_vip1 * aantal_personen)
totaal = int(round(vr_vip1 , 2))
print ('de prijs voor de vip vr gameseat is',uitkomst_vip2,'cent')
totaal = uitkomst + uitkomst_vip2


print(f'Dit geweldige dagje-uit met {aantal_personen} mensen in de Speelhal met 45 minuten VR kost je maar',totaal,'cent')