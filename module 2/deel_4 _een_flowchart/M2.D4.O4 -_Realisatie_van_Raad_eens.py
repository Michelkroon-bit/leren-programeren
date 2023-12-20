import random
ronde = 0
punt = 0

print("start programma")
random_getal=random.randint(1,1000)
print(random_getal)
raden = int(input("probeer het getal te raden "))
if raden == random_getal:
    print("goedzo je hebt het geraden")
    punt +=1 
    ronde+=1
    if ronde == 20:
        print("einde programma")
        print(punt)
    