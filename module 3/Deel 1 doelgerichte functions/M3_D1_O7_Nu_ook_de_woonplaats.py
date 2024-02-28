#functie 1 (laat met rust)
namen_dict = []
def naam_en_leeftijd_invullen() -> str:
    name = input('vul uw naam in: ').capitalize()
    age = int(input('vul uw leeftijd in: '))
    woonplaats = input('vul je woonplaats in: ')
    namen_dict.append({'naam':name , 'leeftijd' :age , 'city': woonplaats})
    return namen_dict
    
#functie 2     
def meer_namen_toevoegen ():
    while True:
        print('druk op "ENTER" om door te gaan of type "STOP" om te printen. ')
        nog_een_naam_toevoegen = input('>> ')
        if nog_een_naam_toevoegen == '':
            naam_en_leeftijd_invullen()
        else:
            return namen_dict

naam_en_leeftijd_invullen()
meer_namen_toevoegen()
namen_output = namen_dict
for x in namen_output:
    print(f"{x['naam']} die in {x['city']} woont is {x['leeftijd']} jaar oud")


