def tax(bill):
    #added 8% tax to the bill
    bill = bill * 1.08
    print "Bill with tax : %f" % bill
    return bill

def tip(bill):
    #added 15% tip to the bill with tax 
    bill = bill * 1.15
    print "With tip: %f" % bill
    return  bill


meal_cost = 100
meal_wih_tax = tax(meal_cost)
meal_with_tip = tip(meal_wih_tax)
