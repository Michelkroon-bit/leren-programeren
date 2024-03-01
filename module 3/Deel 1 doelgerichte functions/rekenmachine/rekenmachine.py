from my_functions import *



lijst_met_opties = ['A) getallen optellen', 'B) getallen aftrekken', 'C) getallen vermenigvuldigen', 'D) getallen delen', 'E) getal ophogen', 'F) getal verlagen','G) getal verdubbelen', 'H) getal halveren?']

print('wat wilt u doen')
for x in lijst_met_opties:
    print (x)
print('\n')
choice = input('>> ')
choice = choice.upper()

if choice == 'A':
    print('getallen optellen')
    n1 = int(input('welk getal wilt u invullen: \n'))
    n2 = int(input(f'welk getal optellen bij {n1} \n'))
    uitkomst = addition(n1 , n2)
    print(uitkomst)