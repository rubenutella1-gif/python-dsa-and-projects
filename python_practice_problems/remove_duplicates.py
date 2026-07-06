# Remove Duplicates from a List
# Remove duplicates while maintaining order.
lst=[1,1,23,3,23,4,33,3,2,45,65]
# unique=[]
# for i in lst:
#     if i not in unique:
#         unique.append(i)
# print(unique)
unique = list(dict.fromkeys(lst))
print(unique)