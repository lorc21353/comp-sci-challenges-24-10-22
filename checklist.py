checklist = []
textfile = open("Desktop"+"To-Do-List.txt", "w")
where = input("Where are you going?: ")
checklist.append(where)

itemcount = 0
taskcount = 0

print("Enter 'exit' to finish entering items")
while True:
    temp = input("Enter an item you need to bring: ")
    if temp.lower() == "exit":
        break
    checklist.append(temp)
    itemcount += 1
    
print("Enter 'exit' to finish entering items")
while True:
    temp = input("Enter a task you need to do: ")
    if temp.lower() == "exit":
        break
    checklist.append(temp)
    taskcount += 1
    
    
# i had to check the syntax for this as im used to saving JSONObjects and JSONArrays in java rather than text files in python but its file = open("filename", "w") w is to open to file to write to file.write("stuff") is to write stuff to the file and file.close() is to finish with the file
# although from what i remember of JSON files this is fairly similar
count = 0
for x in checklist:
    if count == 0:
        textfile.write("The Destination is: "+ x + "\n")
    elif count > 0 and count <= itemcount:
        textfile.write("Item to bring: " + x + "\n")
    else:
        textfile.write("task to do: " + x + "\n")
    count += 1
textfile.close()