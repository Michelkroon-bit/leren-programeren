from M3_D1_O7_Nu_ook_de_woonplaats_copy import meer_namen_toevoegen

namen_output = meer_namen_toevoegen()
for x in namen_output:
    print(f"{x['naam']} die in {x['woonplaats']} woont is {x['leeftijd']} jaar")

