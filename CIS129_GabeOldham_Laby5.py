# Module 5 Lab-5
# Gabe Oldham
# 10/16/2024
# This program gets the weekly bottle count from the user day by day
# and calculates the total payout.

def calcPayout(bottleCount):
    PAYOUT_PER_BOTTLE = .10 
    payout = bottleCount * PAYOUT_PER_BOTTLE

    return payout

def printInfo(bottles, payout):
    print(f"\nThe total number of bottles collected is {bottles}")
    print(f"The total paid out is $ {payout:.1f}")

def getBottles():
    NBR_OF_DAYS = 7
    totalBottles = 0
    todayBottles = 0
    totalPayout = 0
    counter = 1 
    prompt = ""
    
    while counter <= NBR_OF_DAYS:
        prompt = f"Enter number of bottles returned for day #{counter}: "
        todayBottles = int(input(prompt))
        totalBottles += todayBottles
        counter += 1 

    totalPayout = calcPayout(totalBottles)
    printInfo(totalBottles, totalPayout)

# Declare the local vairables
keepGoing = "y"
prompt = "\nDo you want to enter another week's worth of data? Enter y or n: "

while keepGoing == "y":
    getBottles()
    keepGoing = input(prompt)
    print("")
