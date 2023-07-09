welcome="Welcome to the tip calculator."
bill=float(input("What Was the total bill?$"))  #$124.56
tip=int(input("What percentage tip would you like to give? 10,12,or 15? 12"))
people=int(input("How many people to split the bill?  7"))
#"Each person should pay:     $19.93

tip_as_persent=tip/100
total_tip_amount=bill * tip_as_persent
total_bill=bill+total_tip_amount
bill_per_person=total_bill/people
final_amount=round(bill_per_person,2)
final_amount="{:.2f}".format(bill_per_person)
print(f"Each person should pay ${final_amount}")

