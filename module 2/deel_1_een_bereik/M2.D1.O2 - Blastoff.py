from time import sleep



for x in range(30 , -1 , -1):
    print(x)
    sleep(1)
    if x == 0:
        print("BLASTOFF!!!")