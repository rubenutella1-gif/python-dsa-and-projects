""" lst=[1,2,3,4,5,7,6,7,7,1,2,4]
lst3=[2,3,5,1,42,5]
#1append
lst.append("hello")
print(lst)
#2pop
lst.pop()
print(lst)
#3 remove
lst.remove(1)
print(lst)
#4 insert
lst.insert(2,"apple")
print(lst)
#5 extend
lst.extend([23,43,"berry"])
print(lst)
#6 count
lst.count(7)
print(lst)
#7 sort
lst3.sort()
print(lst3)
#8 copy 
lst1=lst.copy()
print(lst1)
#9 index
print(lst.index(2))
#10 reverse
lst.reverse()
print(lst)
#11 clear
lst.clear()
print(lst) """
# Accessing First and Last elements in a list
lst1=[1,2,3,4,5,6,7,8,9,10]
first_last=lst1[0],lst1[-1]
print("First and last element of the list",first_last)