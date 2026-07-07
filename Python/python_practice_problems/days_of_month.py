#write a python program to count number of notes for given amount
def count_number_of_notes(amount,note):
    if note==100:
        return amount/100
    elif note==500:
        return amount/500
    elif note==200:
        return amount/200
    elif note==50:
        return amount/50
    elif note==20:
        return amount/20
    elif note==10:
        return amount/10
    else:
        return False
while True:    
    amount=int(input("Enter amount That you want to count Number of notes:"))  
    note=int(input("Enter which type of notes that the amount is:"))  
    result=count_number_of_notes(amount,note)
    print(result)