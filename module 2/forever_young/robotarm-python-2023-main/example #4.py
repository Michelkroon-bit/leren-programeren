from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

# Jouw python instructies zet je vanaf hier:
for x in range(5):
    robotArm.grab()
    for x in range (5):
        robotArm.moveRight()
    robotArm.drop()
    for x in range (5):
        robotArm.moveLeft()

for x in range(5):
    for x in range(5):
        robotArm.moveRight()
    robotArm.grab()
    for x in range (4):
        robotArm.moveLeft()
    robotArm.drop()
    robotArm.moveLeft()



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()