namen_dict = []

def naam_en_leeftijd_invullen() -> str:
    print("welkom bij deze functie u gaat nu uw naam en leeftijd invullen")
    name = input('vul uw naam in: ').capitalize()
    age = int(input('vul uw leeftijd in: '))
    namen_dict.append({'naam':name , 'leeftijd' :age})
    return namen_dict
    
naam_en_leeftijd_invullen()
namen_output = namen_dict
for x in namen_output:
    print(f"{x['naam']} is {x['leeftijd']} jaar oud")


