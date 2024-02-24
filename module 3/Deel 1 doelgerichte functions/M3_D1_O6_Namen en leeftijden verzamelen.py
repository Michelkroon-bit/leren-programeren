#functie 1 (laat met rust)

def naam_en_leeftijd_invullen() -> str:
    print("welkom bij deze functie u gaat nu uw naam en leeftijd invullen")
    name = input('vul uw naam in: ').capitalize()
    age = int(input('vul uw leeftijd in: '))
    return name , age
    
#functie 2     
def meer_namen_toevoegen ():
    print('wilt u nog een naam invullen: ')
    nog_een_naam_toevoegen = input('>> ')
    if nog_een_naam_toevoegen == 'ja':
        name = input('vul uw naam in: ').capitalize()
        age = int(input('vul uw leeftijd in: '))     
    else:
        return name , age

naam_en_leeftijd_invullen()
meer_namen_toevoegen()
name , age = meer_namen_toevoegen()
print (f"{name} is {age} jaar")

