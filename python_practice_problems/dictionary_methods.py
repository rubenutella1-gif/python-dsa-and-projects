""" dict1={"name":"Rubenu","age":22}
print(dict1)
print(dict1.get("name"))
print(dict1.keys())
print(dict1.values())
print(dict1.items())
dict1["number"]=8639591117
print(dict1)
dict1.pop("name")
print(dict1)
dict1.update({"Study":"Btech"})
print(dict1)
dict1.setdefault("course","default")
print(dict1)
dict2=dict1.copy()
print(dict2)
dict1.clear()
print(dict1)
print(dict2) """
# method 1 to declare dictionary
""" dict1={
    "name":"Rubenu",
    "age":22,
    "skill":"Python Developer"
}
print(dict1) """
# method 2 to declare dictionary 
""" dict1=dict(name="Rubenu",age=22,skill="Python Developer")
print(dict1) """
# method 3 to declare dictionary
keys=["name","age","skill"]
values=["Rubenu",22,"Python developer"]
dict1=dict(zip(keys,values))
print(dict1)
"""print(dict1["name"])
print(dict1.get("name"))
print(dict1.get("height","NOT in the dictionary"))
dict1["number"]=8639591117
print(dict1)
del dict1["number"]
print(dict1)
dict1.pop("age")
print(dict1) """
print(dict1.keys())
print(dict1.values())
print(dict1.items())