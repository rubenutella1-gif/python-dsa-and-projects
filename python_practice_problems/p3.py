n=int(input().strip())
arr=list(map(int,input().split()))
zeros=0
positives=0
negetives=0
for i in arr:
    if i==0:
        zeros+=1
    elif i<0:
        negetives+=1
    else:
        positives+=1
print(f"positive:{positives},Negetives:{negetives},Zeros:{zeros}")