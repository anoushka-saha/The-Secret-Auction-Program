#Anoushka Saha
#The Secret Auction Program
#May 8th, 2024

#Importing module that will allow terminal to clear so program can be anonymous
import os

#Empty dictionary that will hold user names and bids
bids = {}

#While loop to allow multiple bidders to use the program anonymously 
while True:

    #Ask user for name
    user_name = input("What is your name: ")

    #Ask user for bid
    user_bid = int(input("How much would you like to bid?: $"))

    #Adding user info to bid dictionary
    bids[user_name] = user_bid

    #Ask about other bidders
    yes_no = input("Are there any more bidders (yes/no)?: ")

    #Exiting while loop if there are no more bidders
    if yes_no != "yes":
        os.system('cls')
        break
    else:
        os.system('cls')

#For loop to go throught bids dictionary to determine highest bid
max_bid = 0
for key in bids:
    if bids[key] > max_bid:
        max_bid = bids[key]
        winner = key

#Anouncing the succesful bidder
print("The succesful bidder is " + winner + " with a bid of $" + str(max_bid))
    
