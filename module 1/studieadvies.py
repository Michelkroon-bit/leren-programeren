from studieadviestext import * 
print(STUDIEDOKTER_TITEL)
print(OPTIES)
print(COMPETENTIE_STELLING_1)
antwoord_1 = int(input())

antwoord_2 = int(input(COMPETENTIE_STELLING_2))

antwoord_3 = int(input(COMPETENTIE_STELLING_3))

antwoord_4 = int(input(COMPETENTIE_STELLING_4))

antwoord_5 = int(input(COMPETENTIE_STELLING_5))

antwoord_6 = int(input(COMPETENTIE_STELLING_6))

antwoord_7 = int(input(COMPETENTIE_STELLING_7))

antwoorden_lijst = list[antwoord_1 , antwoord_2 , antwoord_3, antwoord_4 , antwoord_5 , antwoord_6 , antwoord_7]  
count = 0

for x in antwoorden_lijst:
    if (x == 0) or (x ==1): 
        count += 1

uitkomst = antwoord_1+antwoord_2+antwoord_3+antwoord_4+antwoord_5+antwoord_6+antwoord_7
uitkomst_1=uitkomst//7
print (uitkomst) #for debugging
print(uitkomst_1) #for debugging

if uitkomst == 3:
    print(COMPETENTIE_ADVIES_TITEL)
    print('Advies is twijfelachtig')
    
if uitkomst == 2 or count >= 4:
    print(COMPETENTIE_ADVIES_ZORGELIJK)

if uitkomst == 1:
    print('Advies is ZEER zorgelijk')


else:
    print('Advies is geruststellend')