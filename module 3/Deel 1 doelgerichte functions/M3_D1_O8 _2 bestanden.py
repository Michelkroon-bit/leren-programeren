from M3_D1_O7_Nu_ook_de_woonplaats_copy import *

alle_namen = [naam_en_leeftijd_invullen()] + meer_namen_toevoegen()
for x in alle_namen:
    print(f"{x['namen']} die in {x['woonplaats']} woont is {x['leeftijd']} jaar oud")

