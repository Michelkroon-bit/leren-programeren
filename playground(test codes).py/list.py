# boodschappen=['melk' , 'eieren']

# boodschappen.append('brood')

# print (boodschappen)

boodschappen= []
bool_continue=True
while bool_continue:
    
    boodschap=input('wat wilt u toevoegen aan de lijst? ')
    boodschappen.append(boodschap)
    print('je item is toegevoegd')
    verder_gaan=input('wilt u nog een item toevoegen ja/nee ')
    if verder_gaan == 'nee':
        bool_continue=False


print('dit is je boodschappen lijst')
for x in boodschappen:
    print (x)