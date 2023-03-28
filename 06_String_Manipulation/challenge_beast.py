# user input: first name
first = input("What is your first name? ")
# user input: last name
last = input("What is your last name? ")
# concatenates the first and last name and applies title case
full = (first + " " + last).title()
# stores the length of the name
lenName = len(first) + len(last)
# stores the initials of the name
initials = (first[0] + last[0]).upper()
# counts all values in the full name
countA = full.upper().count("A")
countE = full.upper().count("E")
countI = full.upper().count("I")
countO = full.upper().count("O")
countU = full.upper().count("U")
# counts the total number of values
totalVowels = countA + countE + countI + countO + countU
# outputs the data
print(f"Hello {full}. "
      f"Your name contains {lenName} letters. "
      f"Your initials are {initials}.")
# outputs the vowel data
print(f"Your name has {totalVowels} vowels, in the following counts: "
      f"a: {countA}, "
      f"e: {countE}, "
      f"i: {countI}, "
      f"o: {countO}, "
      f"u: {countU}.")
