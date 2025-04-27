amt= int (input("please enter the amount you want to withdraw : "))
note_100 =amt // 100 #floor division
note_50 = (amt % 100) // 50
note_10 = ((amt % 100) %50)//10
print (f"the number of 100 notes are : {note_100}")
print (f"the number of 50 notes are : {note_50}")
print (f"the number of 10 notes are : {note_10}")