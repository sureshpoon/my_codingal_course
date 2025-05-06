num = int (input("enter a number : "))
digit = 0
while num > 0 :
    num = num // 10
    digit = digit + 1
    
print (f"number of digits in given number is {digit}")