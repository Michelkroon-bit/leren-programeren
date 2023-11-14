from time import sleep
from colorama import Fore
import os

lives = 3
doorKey = False
chestkey = False

#functions
#function for start and name 

def clear():
    os.system('cls')
    return


def dead():
    print("***you died***")
    global lives
    lives -= 1
    if lives <= 0:
        "Game Over :("
        sleep(10)
        (start())
    else:
        print(f"{lives} lives remaining, respawning")
        sleep(5)


def start():
    clear()
    print("***********************************************************************************")
    print('                             	   Welcome to:                                 ')
    print('''  
     _____                                        ____                  _   
    |  __ \                                      / __ \                | |      
    | |  | |_   _ _ __   __ _  ___  ___  _ __   | |  | |_   _  ___  ___| |_ 
    | |  | | | | | '_ \ / _` |/ _ \/ _ \| '_ \  | |  | | | | |/ _ \/ __| __|
    | |__| | |_| | | | | (_| |  __/ (_) | | | | | |__| | |_| |  __/\__ \ |_ 
    |_____/ \__,_|_| |_|\__, |\___|\___/|_| |_|  \___\_\\__,_|\___||___/\__|
                        __/ |                                              
                        |___/                                               
                                ⣀⠤⠔⠒⠒⠒⠒⠒⠒⠒⠦⢄⣀⠀⠀⠀⠀
                            ⠀⢀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⢄⠀⠀
                            ⢀⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢣⠀
                            ⢸⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢢⠈⡇
                            ⢸⠀⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠀⡇
                            ⠘⡆⢸⠀⢀⣀⣤⣄⡀⠀⠀⠀⢀⣤⣤⣄⡀⠀⡇⡸⠀
                            ⠀⠘⣾⠀⣿⣿⣿⣿⣿⠀⠀⠀⣿⣿⣿⣿⣿⠀⡗⠁⠀
                            ⠀⠀⣿⠀⠙⢿⣿⠿⠃⢠⢠⡀⠙⠿⣿⠿⠃⠀⡇⠀⠀
                            ⠀⠀⠘⣄⡀⠀⠀⠀⢠⣿⢸⣿⠀⠀⠀⠀⠀⣠⠇⠀⠀
                            ⠀⠀⠀⠀⡏⢷⡄⠀⠘⠟⠈⠿⠁⠀⢠⡞⡹⠁⠀⠀⠀
                            ⠀⠀⠀⠀⢹⠸⠘⢢⢠⠤⠤⡤⡄⢰⢡⠁⡇⠀⠀⠀⠀
                            ⠀⠀⠀⠀⢸⠀⠣⣹⢸⠒⠒⡗⡇⣩⠌⢀⡇⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠈⢧⡀⠀⠉⠉⠉⠉⠁⠀⣀⠜⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠀⠉⠓⠢⠤⠤⠤⠔⠊⠁⠀⠀⠀⠀⠀
        ''')
    print("**********************************************************************************")


    name_input=(input("whats your name: "))
    print(f"hello {name_input} welcome to dungeon quest")
    begin = (input("press enter to begin "))
    if begin == "":
        print('loading...')
        sleep(1)
        print("downloading data...")
        sleep (2)
    else:
        print ('nevermind 🖕🏻')
    clear()
    story()      
    return

# function for story
def story():
    story = input("would you like to start with the story yes / no ")
    if story == "yes":
        sleep(1)
        print("the story begins I hope your ready")
        sleep(1)
        print("*******************************************************")
        print('''The Dungeon Quest - Echoes of the Forgotten Depths." Traverse trough chilly chambers, from a haunted prison and an ancient lunchroom frozen in time to a suspicious library filled with forbidden knowledge and a mysterious chestroom guarded by mystical forces. Uncover the secrets of tortured souls, solve puzzles, and confront spectral challenges to unveil the mysteries hidden within the dungeon's depths. Your choices will shape the fate of the forgotten depths, and the echoes of your journey will resonate through time in this atmospheric world. Are you ready for the challenge?''')
        print("*******************************************************")
        print("you wake up *ugh* another day ")
        input("Press enter to continue.")
    elif story == "no":
        print ("okay then lets start")
        sleep (5) 
        print("you wake up")
    clear()
    choice()
    return

#function choice 1
def choice():
    print("stand up and walk down the hall what do you do \n(A) you go downstairs \n(B) you go to the bathroom to shower")
    choice = input (">> ")
    if choice in ["A" , "a"]:
        clear()
        breakfast()
    elif choice in ["B" , "b"]:
        clear()
        bathroom()
        # bathroom()
    return

def breakfast():
    print ("you go downstairs what do you do \n(A) eat breakfast \n(B) you grab yourself a drink")
    downstairs = input (">> ")
    if downstairs in ["A" , "a"]:
        print("you make yourself a sandwich")
        clear()
        going_on_a_adventure()
    elif downstairs in ["B" , "b"]:
        print("you grab yourself a drink")
        clear()
        going_on_a_adventure()
    return

def going_on_a_adventure():
    print ("you ate your breakfast and your ready to go on your adventure but do you check your inventory before you go \n(A)yes check your inventory \n(B) no go without checking") 
    inventory = input (">> ")
    if inventory in["A" , "a"]:
        print("**inventory**", "sword" , "shield" , "candle")
        heading_out()
    elif inventory in["B" , "b"]:
        print("i have to check my inventory before i go")
        clear()
        going_on_a_adventure()
    return   
        
def bathroom():
    print ("went to the bathroom what are you going to do \n(A) shower \n(B) brush your teeth")
    bathroom = input(">> ")
    if bathroom in["A", "a"]:
        print("you showered and went downstairs")
        breakfast()
    elif bathroom in ["B","b"]:
        print("you brushed your teeth and went downstairs")
        clear()
        breakfast()
    return
        
def heading_out():
    print("your gonna head to the dungeon but what way do you take \n(A) trough the village \n(B) trough the woods")
    heading_out = input(">> ")
    if heading_out in["A","a"]:
        print("you go trough the village")
        sleep(0.5)
        clear()
        arrival_at_dungeon()
    elif heading_out in["B","b"]:
        print("you go trough the woods")
        clear()
        arrival_at_dungeon()
    return
    
def arrival_at_dungeon():
    print ("you arrived at the dungeon do you go inside \n(A) yes i go inside \n(B) no im not ready yet")
    entering_the_dungeon = input(">> ")
    if entering_the_dungeon in ["A","a"]:
        print("its pretty dark in here do you wanna equip your candle \n(A) yes  \n(B) no ")
        equip_candle = input(">> ")
        if equip_candle in ["A","a"]:
            print ("*Equiped candle*")
            clear()
            first_chambers()
        elif equip_candle in ["B","b"]:
            print("You are killed by a unknown monster.")
            clear
            dead()
            
    elif entering_the_dungeon in ["B" , "b"]:
        print("wrong choice returning to start")
        sleep(1)
        clear()
        start()
    return

def first_chambers():
    print("you reach the first chamber in the dungeon and you find 2 hallways each hallway has a sign which says: left chamber the haunted prisons right chamber the suspicious library which do you go first choose wisely \n(A) chamber on the left side of you \n(B) chamber on the right side of you")
    chamber = input(">> ")
    if chamber in ["A" , "a"]:
        print("you decide to go in the hallway to your left you look around and find multiple prison cells and you find a key do you pick it up \n(A) yes \n(B) no ")
        key= input(">> ")
        if key in["A","a"]:
            print ("you picked up the key and saw a little tag on it do you read the text on the tag \n(A) yes \n(B) no")
            text_on_tag= input(">> ")
            if text_on_tag in ["A", "a"]:
                print ("the tag says 12b it looks like the key of a cell i should look for the correct cell")
                print("finaly i found the correct celldoor now do i open the key or wait \n(A) open the door \n(B) wait" )
                open_cell_door = input(">> ")
                if open_cell_door in ["A" , "a"]:
                    print ("you opened the door and found another key you wonder what it is for")
                    print("i should head back to the main chamber")
                    global chestkey
                    chestkey = True
                    sleep(2)
                print("im finaly back")
                clear()
                second_chamber()
            elif open_cell_door in ["B" , "b"]:
                print("i should wait a little and come back here later")
                print("i should head back to the main chamber")
                sleep(2)
                print("im finaly back")
                    
            elif text_on_tag in ["B" , "b"]:
                print ("i wonder what it says but i will come back to it later")
        elif key in["B" , "b"]:
            print("you did not pick up the key and keep wandering trough the prison")
            print ("you decided to go back to the main chamber")
    elif chamber in ["B" , "b"]:
        clear()
        second_chamber()
            
            
def second_chamber():
    print("You decide to take the right halway to the suspicious library you enter the chamber and see a lot of ancient books and bookshelves you also hear some strange sounds behind a closed door do you check it out? \n(A) yes \n(B) no im good ")
    strange_sound= input(">> ")
    if strange_sound in ["A" , "a"]:
        print ("you force open the closed door and find out that there's a big monster type of fugure sleeping in the corner what do you do \n(A)  investigate the area around the sleeping monster with the chance of waking him up \n(B) walk away" ) 
        investegate = input(">> ")
        if investegate in["A" , "a"]:
            print("you deside to go investegate but you trip and wake up the monster")
            clear()
            dead()
            arrival_at_dungeon()
        elif investegate in["B","b"]:
            print ("you decide to walk away and wander trough the rest of the library you find a chest but its locked what do you do now \n(A) try to lockpick it \n(B) look for the key")
            chest = input(">> ")
            if chest in ["A" , "a"]:
                print("you tried to lockpick the chest but it failed you have to look for the key")
            elif chest in ["B","b"]:
                global chestkey
                if chestkey == True:
                    print("you opened the chest and found another key")
                    global doorKey
                    doorKey = True
                else:
                    print("You don't have a key.")
                    print("I should return to the other chamber and look for the key.")
                    print("Returning to chamber one.")
                    sleep(3)
                    clear()
                    first_chambers()                   
    elif strange_sound in ["B" , "b"]:
        print("you walk away from the door and deside to walk further until you find a locked chest what do you do \n(A) try to lockpick it \n(B) look for the key")
        chest = input(">> ")
        if chest in ["A" , "a"]:
                print("you tried to lockpick the chest but it failed you have to look for the key")
        elif chest in ["B" , "b"]:
            if chestkey == True:
                print("you opened the chest and found another key")
                print ("do i wanna look further into the room \n (A)yes \n (B)no")
                continue_ = input("")
                if continue_ in ["A" , "a"]:
                    clear()
                    third_chamber()
                elif continue_ in ["B" , "b"]:  
                    clear()
                    first_chambers()
                    #global doorKey
                    #doorKey = True
            else:
                print ("you dont have a key")
                print("i should return and look for the key or continue looking in this room what do you do \n(A) continue back to the main hall to look for the key \n(B) you go to look further in the room")
                return_or_continue = input(">> ")
                if return_or_continue in ["A" , "a"]:
                    print ("you decide to go back to the main room")
                    clear
                    first_chambers()     
                    clear()
                elif return_or_continue in ["B" , "b"]:
                    clear()
                    third_chamber() 
        return
    
    
def third_chamber(): 
    print ("you see another closed door in the back of the prison what do you do \n(A) check it out \n(B) dont check it" )
    closed_door = input(">> ")
    if closed_door in ["A" , "a"]:
        print("you decide to open the door and find a ancient lunchroom that looks like it has been abandond for a very long time you hear some weird type of growling noice behind a door what do you do \n(A) check it out \n(B) you dont and keep serching" )
        weird_noice = input(">> ")
        if weird_noice in ["A" , "a"]:
            print ("you go check it out but find a big growling wolf monster which kills you instantly")
            clear()
            dead()
            third_chamber()
            
        elif weird_noice in ["B" ,"b"]:
            print("you did not look closer and decided to walk away and look further until you stepped on a stone like button that generates a clicking sound two hidden doors open which one do you choose? \n(A) left \n(B) right \n(C) keep looking")
            hidden_door = input(">> ")
            if hidden_door in ["A" , "a"]:
                
                print("you wander into the left room that has a 2 big monsters inside of it you tried to sneak out of the room but you trip and fall which wakes up the monsters but you bearly got to escape you will need to check the other chambers (b)left chamber (C)keep looking for other secrets")
                escaped = input(">> ")
                if escaped in ["B" ," b "]:
                    print("you wander into the right room thats filled with traps you try to back off but the door closes and you are traped there's no way out")
                    dead()
                    third_chamber()
                    
                elif escaped in ["C","c"]:
                    fourth_and_final_chamber()
                    
            elif hidden_door in ["B" ,"b"]:
                print ("you wander into the right room thats filled with traps you try to back off but the door closes and you are traped there's no way out")
                dead()                
            elif hidden_door in ["C" , "c"]:
                fourth_and_final_chamber()
    elif closed_door in ["B" , "b"]:
        print ("you did not go trough the closed door and decide to go back to the first chamber")
        clear()
        first_chambers()
    return
    
def fourth_and_final_chamber():
    print("you look around the room and see that another door opend behind you do you decide to check it out (A)check it out (B) dont check it out")
    the_final_room = input(">> ")
    if the_final_room in["A" , "a"]:
        print(" you decide to check it out and at first it didnt look like much until you looked a little closer and you find out that its a room filled with gold , diamonds , gems , and a lot of other kind of tressure you only have limited time tho you you have to decide what to take so what do you do \n(A)take gold and some gems \n(B) take a few diamonds and 2 other tressures")
        tressure = input(">> ")
        if tressure in ["A" , "a"]:
            print("you took to much gold wich weighted you down as the tressure room started to collaps you didn't have enough time to escape")
            dead()
            fourth_and_final_chamber()
        elif tressure in ["B" ,"b"]: 
            print("you grabbed some middle sized diamonds and some gold goblets then you say that the tressure chamber started to collaps so you made a run for it and barely made it out alive.")
    return          
            
def the_Escape():
    print ("after you barley made it out of the tressure room you decide to try and head to the exit so you started on your way back but you heard footsteps you looked behind you and noticed the wolf from earlier broke free out of the lunchroom and started running after you what do you do (A) hide (B)make a run for it")
    hide_or_run = input(">> ")
    if hide_or_run in ["A" , "a"]:
        print ("you hide and you succefully lose the big wolf you decide to check once more before you continue on your way out the coast was clear so you decide to continue on the find to the exit which you reach a copple of minutes later")
        print ("you succefully reach the exit and your free from the dungeon what do you do now (A) head home (B)head into the city")
        escaped = input(">> ") 
        if escaped in ["A" , "a"]:
            print ("you head home and take a well deserved rest.") 
            the_end()
        elif escaped in ["B" , "b"]:
            print ("you head into the city to sell some of your tressure and decide to grab a gold pint of beer after that you head home and get a well deserved rest")
            the_end()
    if hide_or_run in ["B" , "b "]:
        print ("the wolf caught up to you and he ripped you appart")
        dead()
        the_Escape()
        
        return
    


def the_end():
        print("*******************************************************************************")
        print(                 '''                              made by michel kroon
                                       23a2''')
        print('''
                             
                       _____ _   _ _____   _____ _   _ ____   
                      |_   _| | | | ____| | ____| \ | |  _ \  
                        | | | |_| |  _|   |  _| |  \| | | | | 
                        | | |  _  | |___  | |___| |\  | |_| | 
                        |_| |_| |_|_____| |_____|_| \_|____/  
                                                            

''')    
        print("********************************************************************************")
    
    
    
    
# # # main script
start()

story()

choice()

breakfast()

bathroom()

going_on_a_adventure ()

heading_out()

arrival_at_dungeon()

first_chambers()

second_chamber()

third_chamber()

fourth_and_final_chamber()

the_Escape()

the_end()
