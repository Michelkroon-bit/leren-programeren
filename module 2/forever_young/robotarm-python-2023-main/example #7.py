from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')
count = 0 
# Jouw python instructies zet je vanaf hier:
while count < 7:
    robotArm.moveRight
    count+=1

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()


#