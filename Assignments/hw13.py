def decimal_to_binary(n) :
    if n == 0 :
        return "0"
    binary_string = ""
    while n >0 :
        rem = n % 2
        binary_string = str(rem) + binary_string
        n = n // 2
    return binary_string

num = int (input("Enter a decimal number : "))
binary_num = decimal_to_binary (num)
print ("the binary conversion of ", num, "is", binary_num)    
