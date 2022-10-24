from random import *
nameList = []
for x in range(5):
    nameList.append(input("enter a name: "))
    
    
print("rand name is:", nameList[randint(0,4)])