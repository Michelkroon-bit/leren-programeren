from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

# Jouw python instructies zet je vanaf hier:
blokjes = 7
while blokjes < 7:
    robotArm.moveRight()
    robotArm.grab()
    blokjes -=1

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()


#