aantal_lijstjes=int(input("hoeveel lijstjes wilt u hebben: "))

for x in range (aantal_lijstjes):
    lengte_lijstjes=int(input("hoe lang moet het lijstje zijn: "))
    print(list(range(x, lengte_lijstjes, x+1)))
    
    
# print (f"aantal lijstjes: {aantal_lijstjes}")#for debugging
# print (f"lengte lijstjes: {lengte_lijstjes}")#for debugging 
  
# Eerst vraagt het programma om het aantal lijstjes dat getoond moet worden en vervolgens naar de lengte van ieder lijstje.

# Vervolgens toont het programma een aantal lijstjes met de gekozen lengte, waarbij de eerste bij 1 begint en stappen van 1 neemt, de tweede bij 2 begint en stappen van 2 neemt, de derde bij 3 begint en stappen van 3 neemt, enz, enz …