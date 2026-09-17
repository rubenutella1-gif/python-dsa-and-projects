""" l1=list(map(int,input("Enter a number: ").split())) """
pos=0
neg=0
zeros=0
for i in map(int, input().split()):
    if i>0:
        pos+=1
    elif i<0:
        neg+=1
    else:
        zeros+=1
print("positives= ",pos," negetives= ",neg," Zeros= ",zeros)