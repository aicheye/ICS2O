# user input: first name
first = input("What is your first name? ")
# user input: last name
last = input("What is your last name? ")
# concatenates the first and last name and applies title case
full = (first + " " + last).title()
# stores the length of the name
lenName = len(first) + len(last)
# outputs the data
print(f"Hello {full}. Your name contains {lenName} letters.")
