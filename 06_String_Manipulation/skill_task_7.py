pw = input("Please enter a password between 6-12 characters long: ")
lenPW = len(pw)
if lenPW < 6 :
    print("Your password is too short.")
elif lenPW > 12 :
    print("Your password is too long.")
else :
    print("Password accepted.")
