def naam_en_leeftijd_invullen() -> dict:
    print("welkom bij deze functie u gaat nu uw naam en leeftijd invullen")
    name = input('vul uw naam in: ').capitalize()
    age = int(input('vul uw leeftijd in: '))
    return {'naam':name , 'leeftijd' :age}
    
namen = naam_en_leeftijd_invullen()

print(f'{str(namen["naam"])} is {namen["leeftijd"]} jaar oud')


#je mag geen global variables gebruiken!!!! (staat niet in de opdracht had ik weer zo gezelgd moeten weten)