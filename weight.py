weight=int(input("weight: "))
unit=input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted= weight/0.45
    print("Weight in terms of Lbs: "+str(converted))
else:
    converted=weight*0.45
    print("Weight in kgs:"+str(converted))

