num = int (input("Enter a number : "))
temp = num 
num_len = 0
while temp > 0 :
    num_len += 1
    temp = int (temp / 10)

if num_len >= 4 :
    num_len = int(num_len / 2)
    check = 0
    while num > 0 :
        rem = num % 10
        if check == num_len :
            middle = rem 

        elif check == (num_len - 1) :
            middle_1 = rem

        num = int (num / 10)
        check = check + 1
    multiply = middle * middle_1
    print ("the product of the middle digits are : ", multiply)

else :
    print ("the number is not 4 or more then 4 digits")        


