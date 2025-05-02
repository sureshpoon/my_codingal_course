medical_cause= input("Do you have any medical cause? (Y/N): ")
attendance = int (input ("What is your attendance? "))
if medical_cause =="Y":
    print ("You are allowed")

else:
    if attendance>= 75:
        print ("you are allowed")
    else :
        print ("you are not allowed")        


