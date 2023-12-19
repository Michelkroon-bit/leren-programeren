#variable
boodschappen_lijst = {}
dup = False

print("Start Programma")

while True:
    
    voeg_boodschap_toe = input("Voeg een item toe ").lower()
    
    if voeg_boodschap_toe != (""):
        
        hoeveelheid=int(input("Hoeveel wilt u toevoegen "))    
         
         
        if voeg_boodschap_toe not in boodschappen_lijst:
            boodschappen_lijst[voeg_boodschap_toe]= hoeveelheid
        else:
            boodschappen_lijst[voeg_boodschap_toe]+=hoeveelheid
    # if dup != True:          
    nog_een_item_toevoegen = input('Wilt u nog een item toevoegen? ')
        # dup = False
    if nog_een_item_toevoegen == "nee":

        break
print("")
print('-[Boodschappenlijst]-')
print("")
for key in boodschappen_lijst:
    print(f" {key} x {boodschappen_lijst[key]}")
print("")
print('---------------------')
        
#verbetering

#
#
#
#
#
#
#
#
#
#
#
#
