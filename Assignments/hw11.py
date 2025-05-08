base = int (input ("enter a number : "))
power = int (input ("enter a power : "))
res = 1
while power != 0 :
    res = res * base 
    power -= 1 #power = power - 1 

print ("answer : ", res)    
