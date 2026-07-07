def secondlargest(l):
    num=list(set(l))
    num.sort()
    print(num)
    return num[-2] if len(num)>=2 else None
l=list(map(int,input("enter list").split()))
print(secondlargest(l))