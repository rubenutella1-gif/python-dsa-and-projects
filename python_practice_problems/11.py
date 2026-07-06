""" def CountHouses(arr,foodrequired):
    if arr is None:
        return -1
    totalfood=0
    count=0
    for food in arr:
        totalfood+=food
        count+=1
        if totalfood>=foodrequired:
            return count
    return 0
print(CountHouses([3,5,2,8,4],10)) """
""" def reverseSring(s):
    words=s.split()
    l1=[]
    for word in words:
        l1.append(word[::-1])
    return " ".join(l1)
print(reverseSring("Accenture Coding Round")) """
""" num=int(input())
def is_prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
total=0
for n in range(1,num+1):
    if is_prime(n):
        total+=n
print(total) """
""" def is_prime(num):
    if num<2:
        return False
    count=0
    for i in range(2,int(num**0.5+1)):
        if num%i==0:
            return False
    return True
num=int(input("Enter num:"))
count=0
for n in range(1,num+1):
    if is_prime(n):
        count+=1
print(count) """
def rotate_array(arr, k, dir):
    if arr is None:
        return -1

    n = len(arr)
    k = k % n

    if dir == 'L':
        return arr[k:] + arr[:k]
    elif dir == 'R':
        return arr[-k:] + arr[:-k]
    else:
        return -1

print(rotate_array([1,2,3,4,5], 2, 'L'))