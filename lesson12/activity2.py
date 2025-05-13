lowest = int (input("Enter the lowest rage : "))
highest = int (input ("enter the higest range : "))
print ("prime numbers between ", lowest, "and", highest, "are :")
for n in range (lowest , highest + 1) :
    if n > 1:
        for i in range (2,n):
            if n % i == 0 :
                break 
        else :
            print (n)
                
           
                
