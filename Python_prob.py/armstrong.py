def is_armstrong(n):
    digit=str(n)
    power=len(digit)
    total=sum(int(d)**power for d in digit)
    return n==total
print(is_armstrong(153))
print(is_armstrong(9474))
print(is_armstrong(234))