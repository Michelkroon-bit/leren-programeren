import os
from time import sleep
import random 

def complementen_generator () ->str:
        
        COMPLIMENTEN = ("je bent een topper", "je doet het goed", "je bent geweldig")
        random_compliment = random.choice(COMPLIMENTEN)
        return random_compliment
    
naam = input("wat is uw naam: ") 

print("generating.")
sleep(1) 
print("generating..")
sleep(1)
print("generating...")
sleep(1)
print(complementen_generator() , naam)

# localscoping = een locale variable die je alleen in een functie kan gebruiken 
# globalscoping = een variable die je overal in je file mag gebruiken