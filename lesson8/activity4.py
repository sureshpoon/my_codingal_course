a = int (input ("Enter a nuber : "))
b = int (input("enter another number : "))
c = int (input ("enter another number :"))
avg = (a+b+c)/3
if avg >a and avg > b and avg > c :
    print("the average is greater than all three numbers")

elif avg > a and avg > b and avg < c :
    print ("the average is greater than a and b but less than c")

else :
    print ("invalid")        