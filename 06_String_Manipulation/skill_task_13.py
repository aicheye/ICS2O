name = input("What is your first name? ")
lower = name.lower()
count1 = name.count("a")
count2 = name.count("e")
count3 = name.count("i")
count4 = name.count("o")
count5 = name.count("u")
total = count1 + count2 + count3 + count4 + count5
print("Your name contains the following vowels: " +
      f"a: " + str(count1) +
      ", e: " + str(count2) +
      ", i: " + str(count3) +
      ", o: " + str(count4) +
      ", u: " + str(count5))
print("In total your name contains " + str(total) + " vowels")
