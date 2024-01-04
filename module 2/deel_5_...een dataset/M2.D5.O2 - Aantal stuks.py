from fruitmand import *

count = 0
for x in fruitmand["name"]:
    if x in fruitmand:
        count+=1
        print(count)