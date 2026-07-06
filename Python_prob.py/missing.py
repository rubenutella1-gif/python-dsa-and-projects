def missing_num(num):
    n=len(num)+1
    total=n*(n+1)//2
    return total-sum(num)
print(missing_num([1,2,3,4,6,7]))