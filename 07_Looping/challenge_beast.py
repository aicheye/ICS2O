hero = "MOMO HIRAI"
letters = "MOMOHIRAI"
answer = input("Who do you think is my hero? ")
similar = 0

if answer.upper() != hero:
    for i in enumerate(hero):
        if i[0] <= len(answer) - 1 and i[1] == answer[i[0]].upper() :
            similar += 1

print("Incorrect!")
print(f"Clue: Your guess had {similar} identical letter(s) to my hero's name.")

answer = input("Who do you think is my hero? ")
letter = 0

while answer.upper() != hero:
    if letter == 0:
        print("Incorrect!")
        print(f"Clue: The first letter in my hero's name is {letters[0]}")
        letter += 1
    elif letter <= len(letters) - 1:
        print("Incorrect!")
        print(f"Clue The next letter in my hero's name is {letters[letter]}")
        letter += 1
    else:
        print("Incorrect!")
    answer = input("Who do you think is my hero? ")

print("Correct! My hero is Momo Hirai.")

