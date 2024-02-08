import random



while True:
    aantal_keer_vragen = 3
    lootjes = ['mama', 'michel', 'papa']
    namen = ['papa', 'mama', 'michel']
    gekozen_lootjes = []

    giver_reciever = {}
    print('start programma')

        
    # random.shuffle(namen)
    # random.shuffle(lootjes)
    laatst_gekozen = ""
    laatste_lootje = ""
    for naam in namen:
        while True:
            random_lootje = random.choice(lootjes)
            if naam != laatste_lootje:
                if naam != random_lootje:
                    giver_reciever.update({naam : random_lootje})
                    lootjes.remove(random_lootje)
                    laatste_lootje = random_lootje
                    laatst_gekozen = naam
                    break
                
                
                
            else:
                if random_lootje != laatst_gekozen:
                    if naam != random_lootje:
                        giver_reciever.update({naam : random_lootje})
                        lootjes.remove(random_lootje)
                        laatste_lootje = random_lootje
                        laatst_gekozen = naam
                        break
                

    for x, y in giver_reciever.items():
        print(x, y)
        
    input("Press enter to run again.")
