# We should import pandas library 
# if we are  working with data
# which may be in the form of csv,excel or sql
import pandas as pd
#we can create 1D data with the Series keyword
s=pd.Series([1,2,3,4,5])
s.name="Numbers"
print(s)
print(s.dtype)
print(s[1])  #we can do slicing with data 
#iloc loaction based indexing
print(s.iloc[2])
print(s.iloc[[1,2,3]])
names=["Ramesh","Rubenu","Kiran","Prabhas","Sudhansh"]
s.index=names
print(s)
#when we assign a indexing we cant use iloc there is another one
# for slicinf for lable based indexing that is loc
print(s.loc["Ramesh"])
#In lable based indexing the both start and end value are included while slicing
print(s.loc["Ramesh":"Prabhas"])