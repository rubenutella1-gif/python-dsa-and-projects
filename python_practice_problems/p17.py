s=list(map(int,input("Enter a list : ").split()))
j=0
for i in s:
    if i!=0:
        s[j]=i
        j+=1
for i in range(j,len(s)):
    s[i]=0
print(s)