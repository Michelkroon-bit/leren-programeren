#functie 1 (laat met rust)

def naam_en_leeftijd_invullen() -> str:
    print("welkom bij deze functie u gaat nu uw naam en leeftijd invullen")
    name = input('vul uw naam in: ').capitalize()
    age = int(input('vul uw leeftijd in: '))
    return name , age
    
    
#functie 2     
def meer_namen_toevoegen ():
    
naam,age = naam_en_leeftijd_invullen()
print (f"{naam} is {age} jaar")

