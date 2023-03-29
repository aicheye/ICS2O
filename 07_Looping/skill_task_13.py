myList = ["A", "E", "I", "O", "U"]
name = input("Enter your name: ")
vowels = 0
for i in name:
    if i.upper() in myList:
        vowels += 1
print("Hello " + name + ", you have " + str(vowels) + " vowels in your name!")
