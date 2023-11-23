aantal_keer_gesteld = 0

while True:
    print("vul je naam in of vul quit in om te stoppen ")
    naam=input("")
    aantal_keer_gesteld += 1
    if naam =="quit":
        break
print (f"de vraag is {aantal_keer_gesteld} keer gesteld")