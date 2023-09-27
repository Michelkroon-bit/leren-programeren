croissantjes = int(input('vul een hoeveelheid croissantjes in '))
stokbroden = int(input('vul een hoeveelheid stokbroden in '))
kortingsbonnen= int(input('vul een hoeveelheid kortingsbonnen in '))

PRIJS_CROISSANT=39#CENT
PRIJS_STOKBROOD=273#CENT
PRIJS_KORTINGSBON=50#CENT

prijs_croissantjes_in_centen = croissantjes *39#cent    
prijs_stokbroden_in_centen = stokbroden * 273#cent
prijs_kortingsbonnen_in_centen_kortingsbonnen_in_centen = kortingsbonnen *50#cent
uitkomst = croissantjes + stokbroden - kortingsbonnen

print('De feestlunch kost je bij de bakker' ,uitkomst, ' voor de' ,croissantjes,' croissantjes en de ',stokbroden,' stokbroden als de ',kortingsbonnen,' kortingsbonnen nog geldig zijn!')