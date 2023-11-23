tijd_am = 0 #om tijd de tellen
tijd_pm = 0 #om tijd te tellen 
while True:
    tijd_am = tijd_am + 1
    if tijd_am >= 1 and tijd_am <= 12:
        print (f"{tijd_am} am")
    elif tijd_am >= 13 and tijd_am <= 24:
        while True: # nested while loop
            tijd_pm += 1
            print(f"{tijd_pm} pm")
            if tijd_pm <=24:
                break