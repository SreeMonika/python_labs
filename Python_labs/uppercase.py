apples = input("No of apples")
weight = input("enter whether weight is in kg or lbs")
applewgt = 1/5
if(unit == "kg"):
    totalweight = applewgt * float(apples)
    print(totalweight)
elif(unit == "lb"):
    totalweight = (applewgt * 2.2)  * float(apples)
    print("calculate the pound:")
else:
    print("please specify kg or lb")
