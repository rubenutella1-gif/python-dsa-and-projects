P,R,T=map(int,input("Enter P,R,T  : ").split())
Simple_Interest=(P*R*T)/100
amount=P*(1+R/100)**T
compound_Interest=amount-P
print("Simple Interest is : ",Simple_Interest)
print("Compound  Interest is : ",compound_Interest)