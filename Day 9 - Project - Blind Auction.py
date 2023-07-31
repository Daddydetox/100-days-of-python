def validateFloat(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Incorrect numbers format.")

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(f"{logo}\nWelcome to the secret auction program.")

bidders = {}
while True:
    name = input("What is your name?: ")
    bid = validateFloat("What is your bid?: $")
    bidders[name] = bid

    answer = input("Are there any other bidders? Type [no] to end the auction: ").lower()
    if answer == "no":
        break

print(f"The auction is finished! {max(bidders).title()} won the auction with a bid of ${max(bidders.values())}!")
