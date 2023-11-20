#tuple 
dagen = ("maandag" , "dinsdag" , "woensdag" , "donderdag" , "vrijdag" , "zaterdag" , "zondag")
werkdagen = ("maandag" , "dinsdag" , "woensdag" , "donderdag" , "vrijdag")
weekenddagen = ("zaterdag" , "zondag")    
reversedweekenddagen = ["zaterdag" , "zondag"]
reversedwerkdagen = ["maandag" , "dinsdag" , "woensdag" , "donderdag" , "vrijdag"]


for x in dagen:
    print (x)
print("")      



for x in werkdagen:
    print(f"de werkdagen zijn {werkdagen}")    
print("")    


for x in weekenddagen:
    print(f"de weekenddagen zijn {weekenddagen}")
print("")


reversedweekenddagen.reverse()
print(f"omgekeerde lijst{reversedweekenddagen}")
print("")


reversedwerkdagen.reverse()
print(f"omgekeerde lijst{reversedwerkdagen}")