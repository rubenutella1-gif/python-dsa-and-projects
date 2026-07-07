import pandas as pd
import numpy as np
data={
    "Name":["Rubenu","Ramesh","Prabhas","Kiran","Sudhansh","Rohan"],
    "Age":[22,23,25,23,np.nan,30],
    "Role":["SD","HR","Manager","Manager","HR","SD"],
    "Income":[24000,30000,np.nan,34000,np.nan,25000]
}
s=pd.DataFrame(data)
print(s)
data1={
    "Role":["SD","HR","MANAGER"],
    "Location":["Hyderabad","Chennai","Delhi"]
    
}
s1=pd.DataFrame(data1)
print(s1)
print(s.drop("Age",axis=1)) #If we want to remove the particular column we can use axis=1
print(s.drop(1,axis=0))     #If we want to remove the row we should use the row number and axis=0

#BroadcastingBroadcasting is a technique where a smaller value (like a single number)
# is automatically expanded to match the size of a larger data structure during arithmetic operations.

s["Income"]=s["Income"]+5000  # Here it changes the entire column 
print(s)
s.loc[1,"Income"]=50000       # Here it changes the matching row value
print(s)
s.rename(columns={"Income":"Salary"},inplace=True)
print(s)
print(s["Role"].value_counts())
s=s.loc[[2,1,3,0,5,4]] #Changing the rows
print(s)
s=s.reindex(columns=["Salary","Age","Name","Role"]) #Changing The columns
print(s)
s=s.reindex([1,3,2,4,0,5])
print(s)