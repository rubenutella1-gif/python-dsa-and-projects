# # s={1,2,33}
# # print(type(s))
# # print(s)
# # s={1,2,33}
# # s.add(22)
# # print(s)
# s={1,2,33}
# s.update({1,2,3,4,55,67,46})  
# print(s)
# s.pop()
# print(s)
# s={1,2,33}
# s.remove(2)
# print(s)

s={1,2,33}
k={1,3,5,6,78}
print(s.union(k))
print(s.intersection(k))
print(s.issubset(k))
print(s.issuperset(k))