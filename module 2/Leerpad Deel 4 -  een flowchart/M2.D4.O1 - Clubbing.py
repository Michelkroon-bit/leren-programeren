from time import sleep
bandje_kleur=()
prijs = 12.00
print("start programma")
leeftijd=int(input("hoe oud ben je? "))
jaren_Wachten = 18-leeftijd
if leeftijd <18:
    print("sorry je mag niet naar binnen")
    print(f"probeer het over {jaren_Wachten} jaar nog een keer")
    sleep(1)
    print("einde programma")
    sleep(1)
elif leeftijd >=18:
    print("wat is je naam ")
    naam = input()
    print("bent u een vip \nJa \nNee ")
    vip = input()
    if vip == "ja":
        print("bent u boven de 21 \nja \nnee")
        leeftijd_boven_21=input()  
        if leeftijd_boven_21 == "ja":
            bandje_kleur = "blauw"
            print(f"Je krijgt van mij een {bandje_kleur} bandje")
            print("wat wilt u drinken")
            drank=input()    
        elif leeftijd_boven_21 == "nee":
            bandje_kleur = "rood"
            print(f"Je krijgt van mij een {bandje_kleur} bandje")
            print("wat wilt u drinken")
            drank=input()    
    elif vip =="nee":
        print("bent u boven de 21 \nja \nnee")
        leeftijd_boven_21 = input()
        if leeftijd_boven_21 == "ja":
            print("je krijg van mij een stempel ")
            drank=input("wil je wat drinken ")
        elif leeftijd_boven_21 == "nee":
            drank=input("wil je wat drinken ")
            if drank == "cola":
                bandje=input("bandje? ")
                if bandje =="ja":
                    print("alstublieft complimenten van het huis")
                    print('einde programma')
                elif drank == "bier":
                    bandje=input("bandje of stempel?")
                    print("alstublieft complimenten van het huis")
                    print('einde programma')
                elif drank =="champagne":
                    bandje = input('bandje?')
                    if bandje == "ja" and bandje_kleur == "blauw":
                        print(f'alstublieft uw {drank} dat wordt dan €{prijs}')