import random

aantal_kaarten=("2" , "3", "4", "5", "6", "7", "8", "9" ,"10" ,"boer" , "vrouw" , "koning" , "aas" )
soort_kaarten=("klaver", "schoppen" , "ruiten" , "harten"  )
deck_kaarten = []
remaining_deck = []
   
for o in soort_kaarten:
    for b in aantal_kaarten :
        deck_kaarten.append(f"{o} {b}")
        
deck_kaarten.append("joker")
deck_kaarten.append("joker")
random.shuffle(deck_kaarten)
kaart = 0
for x in deck_kaarten:
    if kaart < 7:
        kaart += 1
        print(F"Kaart {kaart}: {x}")
    else:
        remaining_deck.append(x)
        
print(f"deck ({len(remaining_deck)} kaarten) {remaining_deck}")