def delen_door_twee(getal:int) -> bool:
    return getal % 2 == 0
is_deelbaar_door_twee = delen_door_twee(getal = 6)# for debugging 
print(is_deelbaar_door_twee)




def draai_zin_om(ingevulde_zin:str) -> str:
    woorden = ingevulde_zin.split() #druif -> splits 
    omgekeerd = woorden[::-1]
    print(omgekeerd)
    omgekeerde_zin = ' '.join(omgekeerd)
    return omgekeerde_zin
omgedraaide_zin = draai_zin_om("1 2 3 4 5 6 7" )
print(omgedraaide_zin)




def woorden_tellen(zinnetje_ingevuld:str) -> int:
    lijst_woorden = set(zinnetje_ingevuld)
    lengte_van_lijst_met_woorden = len(lijst_woorden)
    return lengte_van_lijst_met_woorden
zinnetje_ingevuld = woorden_tellen('hallo wereld') #telt aantal woorden in een zin
print(zinnetje_ingevuld)




def lengte_tellen_van_zin(gemaakte_zin:str) -> float:
    zin_splitsen = gemaakte_zin.split()
    
    count = 0
    for letter in zin_splitsen:
        count += len(letter)

    aantal_characters = count / len(zin_splitsen)
    return aantal_characters
aantal_characters = lengte_tellen_van_zin('hallo test python is een programeertaal')
print(aantal_characters)


def keersom(ingevulde_nummer:int, nummer:int=10) -> None:
    for x in range(1, nummer+1):
        uitkomst = x * ingevulde_nummer
        print(f'{x} x {ingevulde_nummer} = {uitkomst}')
        
uitgerekend = keersom(9, 10)
print(uitgerekend)
