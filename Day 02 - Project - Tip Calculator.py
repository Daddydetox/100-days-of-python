def isFloat(input):
    try:
        input = float(input)
        return True
    except ValueError:
        return False


total = ""
percent = ""
people = ""

print('Welcome to the tip calculator!')

while not isFloat(total):
    total = input('Enter amount of the total bill: ')
total = float(total)
while not isFloat(percent):
    percent = input('Enter percentage tip would you like to give: ')
percent = float(percent)
while not people.isnumeric():
    people = input('Enter how many people to split the bill with: ')
people = int(people)

print(f'Amount: {total} $    Tip: {percent} %    Persons: {people}')
calc = total * ((percent / 100) + 1) / people
print(f'Total amount to pay each: {calc} $')
