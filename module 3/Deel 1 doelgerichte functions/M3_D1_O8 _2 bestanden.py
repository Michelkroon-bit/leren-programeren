from M3_D1_O7_Nu_ook_de_woonplaats_copy import *
naam_en_leeftijd_invullen()
meer_namen_toevoegen()

output_namen = namen_dict
for x in output_namen:
    print(f"{x['naam']} die in {x['city']} woont is {x['leeftijd']} jaar")

