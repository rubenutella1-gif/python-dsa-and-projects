import pandas as pd
s=pd.Series((1,2,3,4,5,6),index=("a","b","c","d","e","f"))
print(s)
data={1:"Ruben",2:"Ramesh",3:"Kiran",4:"Prabhas",5:"Sudhansh"}
s1=pd.Series(data)
print(s1)
#we can modify the series same as list
s["a"]=10 #If the index is exist it modifies the value
print(s)
s["z"]=20 #If it does not exist it Adds to list at the end
print(s)
#We use drop to remove the item in the series it uses only lables by default
print(s.drop("a"))#Here we are removing the element not the original one
print(s)
s.drop("z",inplace=True)#if we use the inplace=True it is permenently removed
print(s)
print(s.drop(["a","b"]))
#If we want to remove by the indexing we should use the iloc method for location based
print(s.drop(s.index[[1,2,3]])) #Removing a list of elements
print(s.drop(s.index[0:5]))      # removing using the slicing

#We can modify the index also but we have to change the entire index again