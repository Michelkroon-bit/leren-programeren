#functie 1 (laat met rust)

def naam_en_leeftijd_invullen() -> str:
    print("welkom bij deze functie u gaat nu uw naam en leeftijd invullen")
    name = input('vul uw naam in: ').capitalize()
    age = int(input('vul uw leeftijd in: '))
    return name , age
    
#functie 2     
def meer_namen_toevoegen ():
  
    namen_dict = []
    print("welkom bij deze functie u gaat nu uw naam en leeftijd invullen")
    name = input('vul uw naam in: ').capitalize()
    age = int(input('vul uw leeftijd in: '))
    namen_dict.append({'naam':name , 'leeftijd' :age})
    while True:
        print('druk op "ENTER" om door te gaan of type "STOP" om te printen. ')
        nog_een_naam_toevoegen = input('>> ')
        if nog_een_naam_toevoegen == '':
            name = input('vul nog een naam in: ').capitalize()
            age = int(input('vul nog een leeftijd in: '))
            namen_dict.append({'naam':name , 'leeftijd' :age})
            
            
        else:
            return namen_dict

#naam_en_leeftijd_invullen()
namen_output = meer_namen_toevoegen()
for x in namen_output:
    print(f"{x['naam']} is {x['leeftijd']} jaar oud")


