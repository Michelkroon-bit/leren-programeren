boodschappen_lijst = []
dup = False
print("Start Programma")
while True:
    voeg_boodschap_toe = input("Voeg een item toe ")
    if voeg_boodschap_toe != (""):
        hoeveelheid=int(input("Hoeveel wilt u toevoegen "))    
        
        boodschap = {'boodschap':voeg_boodschap_toe, 'hoeveel':hoeveelheid}
        if len(boodschappen_lijst) <=0:
            boodschappen_lijst.append(boodschap)
        else:
            for x in boodschappen_lijst:
                # print(f"Debug: {x['boodschap']}")
                if x['boodschap'].lower() == voeg_boodschap_toe.lower():
                    print(f"Debug: {x['boodschap'].lower()} is al toegevoegd")
                    uitkomst = (x['hoeveel'] + hoeveelheid)
                    x.update({'hoeveel': uitkomst})
                    dup = True
            if dup != True:
                boodschappen_lijst.append(boodschap)
                
    nog_een_item_toevoegen = input('Wilt u nog een item toevoegen? ')
    dup = False
    if nog_een_item_toevoegen == "nee":
    
        break
print("")
print('-[Boodschappenlijst]-')
print("")
for a in boodschappen_lijst:
    print(f"| {a['hoeveel']}x {a['boodschap']}")
    print("")
print('---------------------')
