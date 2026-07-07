# Check Armstrong Number
# A number is Armstrong if the sum of its digits raised to the power of the number of digits equals the number itself.
def is_armstrong(numbers):
    armstrong=[]
    for number in range(1,numbers+1):
        string_number=str(number)
        power=len(string_number)
        result=sum(int(d)**power for d in string_number)
        if result==number:
            armstrong.append(number)
    return armstrong
while True:
    numbers=int(input("Enter a number that you want check armstrong number"))
    if numbers==0:
        break
    print("The armstrong numbers are",is_armstrong(numbers))