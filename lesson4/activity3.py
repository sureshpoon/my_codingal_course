print("enter your marks of any 3 subjects : ")
maths = int (input("Enter your marks in maths :"))
english = int (input("Enter the marks obtained in english :"))
science = int (input("Enter the marks obtained in science : "))
sum = maths + english + science
print (f"The sum : {sum}")
avg = sum/3
print (f"The average marks : {avg} ")
percentage = (sum/300)*100
print (f"the percentage is: {percentage}%")

