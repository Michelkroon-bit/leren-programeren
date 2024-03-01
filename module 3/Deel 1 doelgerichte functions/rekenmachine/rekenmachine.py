from my_functions import *



lijst_met_opties = ['A) getallen optellen', 'B) getallen aftrekken', 'C) getallen vermenigvuldigen', 'D) getallen delen', 'E) getal ophogen', 'F) getal verlagen','G) getal verdubbelen', 'H) getal halveren?']


eerste_berekening = int(input('vul je eerste berekening in '))
print('wat wilt u met dit getal doen')
for x in lijst_met_opties:
    print (x)
optie_kiezen = input('>> ')

