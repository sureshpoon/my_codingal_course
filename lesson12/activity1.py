text = str(input("enter a word : "))
chr = str (input("Enter the character that you want to check the frequency of : "))
i = 0
count = 0
while i < len (text):
    if text[i] == chr : #hello
        count += 1
    i = i + 1     
      
print ("the frequency of character is", count)  

