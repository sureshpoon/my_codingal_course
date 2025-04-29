num = int (input ("enter any number : "))
if num == 1 :
    print ("neither prime nor composite")

elif  num % 2 == 0 or num % (num ** 0.5) == 0 :
    print ("it is a composite number")

else :
    print ("it is a primme number")   
