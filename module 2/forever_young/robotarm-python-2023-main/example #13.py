from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')
stappen = 8
herhalingen = 0
aantal_stappen = 0
# Jouw python instructies zet je vanaf hier:
while herhalingen <5:
    while aantal_stappen <stappen:
        robotArm.moveRight()   
        aantal_stappen +=1
    robotArm.grab()
    aantal_stappen = 0
    
  
    while aantal_stappen <stappen:
        robotArm.moveLeft()
        aantal_stappen +=1
    aantal_stappen=0
    robotArm.drop()  
    stappen -= 1
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()