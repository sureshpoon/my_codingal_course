#swap
#without using temporary variable
# a = int (input("Enter any number : "))
# b = int (input ("Enter another number : "))
# c = int (input ("Enter another number : "))
# print ("Before swapping, a =",a, "b =",b, "c=", c)
# a = a + b + c
# b = a - (b+c) 
# c= a - (b+c)
# a= a - (b+c)
# print ("after swapping, a =",a, "b=",b ,"c=",c)

#with using temp variable 
a= int (input("Enter any number : "))
b = int (input ("Enter another number : "))
c = int (input ("enter another number : "))
print ("Before swapping, a=", a, "b=",b, "c=",c)
temp = a
a =b
b = c
c= temp
print ("After swapping, a=", a, "b=",b, "c=",c)