from fruitmand import *

while True:
    kleur = input("vul een kleur in ")
    if kleur in fruitmand: 
        pass
    elif kleur not in fruitmand:
        print(f"de kleur {kleur} zit er niet in de fruitmand ")
        