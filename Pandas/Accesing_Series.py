import pandas as pd
s=pd.Series((1,2,3,4,5,6),index=("a","b","c","d","e","f"))
print(s)
data={1:"Ruben",2:"Ramesh",3:"Kiran",4:"Prabhas",5:"Sudhansh"}
s1=pd.Series(data)
print(s1)
#we can access the data in the Series by slicing same as the lists
print(s["a":"d"])
# Here we are accessing the elements by using the lables so the last item also printed
#We can call this as loc() labled based indexing last index is included
print(s.loc["a":"c"])
print(s.loc[["a","b","d"]])#If we want to access multiple labels in pandas using loc, we must pass them inside a single list. 
s.index=[1,2,3,4,5,6]
print(s.loc[1:4])#here it prints from the lable based which is given , not positioned ,end is included
print(s.iloc[1:4])#Here it prints from the position based always treats as from 0 position and end is excluded


#Note:we can perform conditional and logical operations on series like <,>,&,|,etc.
# condition in open braces () and for printing we have to put it in square brackets [].