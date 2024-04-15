groen = 0
rijp = 1
rot = 2

verwijderde_rotten_appels = []
groenen_appels = []
appels = [groen , rijp , rijp , rot , groen , rijp , rijp , rot , groen]
lengte_appel_lijst = len(appels)

#verwijder de rotten appels
for appel in appels:
    if appel == rot:
        appels.remove(appel)
        
#for debugging niet nodig
        verwijderde_rotten_appels.append(appel)
print(f'de verwijderde rotten appels: {verwijderde_rotten_appels}')


#voeg alle goenen appels in een apparte lijst
for appel in appels:
    if appel == groen:
        groenen_appels.append(appel)
        appels.remove(appel)
print(f'lijst met groenen appels: {groenen_appels}')  
  

print(f'orginele appel lijst met de overige rijpe appels: {appels}')
  
#persentage rijpe appels berekenen
persentage_rijpe_appels = lengte_appel_lijst + len(groenen_appels)
print(f"persentage rijpe appels : {round(100-((lengte_appel_lijst-len(groenen_appels))/persentage_rijpe_appels*100), 2)}%")
 