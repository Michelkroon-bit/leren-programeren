from time import sleep

count = 31 
while True:
    count  = count - 1
    sleep(1)
    print (count)
    
    if count == 1:
        print("blastoff!!")
        break