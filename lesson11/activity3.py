num = int (input("Enter a number : "))
sum = 0
temp = num 
while temp > 0 :
    digit = temp % 10
    sum = sum + digit**3
    temp = temp // 10

if num == sum : 
    print (f"{num} is an armstrong number" )

else :
    print (f"{num} is not an armstrong number" )         