print("Welcome to the tip calculator!")
bill = float(input("what was the total bill? $"))
tip = int(input("what percentage tip would you like to give?10, 12 or 15?"))
people=int(input("how many people to split the bill?"))
tipAspercent=tip/100
totalTipamount=bill*tipAspercent
totalbill=bill+totalTipamount
billPerperson=totalbill/people
finalAmount=round(billPerperson,2)
print(f"Each person should pay: ${finalAmount}")