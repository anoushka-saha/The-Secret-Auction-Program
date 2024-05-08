#Anoushka Saha
#The Secret Auction Program
#May 8th, 2024


#While loop to allow multiple bidders to use the program anonymously 
while True:
    
    #Ask user for name
    user_name = input(print("What is your name"))

    #Ask user for bid
    user_bid = input(print("How much would you like to bid?: $"))

    #Ask about other bidders
    yes_no = input(print("Are there any more bidders (yes/no)?: "))

    #Exiting while loop if there are no more bidders
    if yes_no != "yes":
        break
