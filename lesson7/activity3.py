Maths = int (input ("enter the marks obtaained in maths : "))
science = int (input("enter the marks obtained in science : "))
english = int (input ("enter the marks obtained in english : "))
social = int (input ("enter the marks obtained in social : "))
computer = int (input ("enter the marks obtained in computer : "))
sum = Maths + science+ english + social + computer 
avg =  sum / 5
if avg >=91 and avg <= 100 :
    print ("Grade is A1")

elif avg>= 81 and avg <= 91:
    print ("Grade is A2")

elif avg >=71 and avg <= 81 :
    print ("Grade is B1")

elif avg >= 61 and avg <= 71 :
    print ("Grade is B2")

else :
    print ("Grade is C" )              
