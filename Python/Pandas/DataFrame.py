import pandas as pd
import numpy as np
Data={
    "Name":["Rubenu","Ramesh","Prabhas","Kiran","Sudhansh"],
    "Age":[22,23,25,23,np.nan],
    "Role":["SD","HR","Manager","Recruiter","Student"],
    "Income":[24000,30000,22000,34000,np.nan]
}
data=pd.DataFrame(Data)
data.index=range(1,len(data)+1)

""" print(data)
print(data.head(2))
print(data.tail(2)) """
print(data.iloc[1:3])
print(data.iloc[1:3,[0,3]])
print(data.loc[0:3,["Name","Income"]])
print(data[["Age"]])
print(data[["Age","Income"]])
print(data.drop("Age",axis=1))
print(data)
data["Age"]+=5  # Here we assign 5 to each row in t he column of Age
print(data)
print(data["Age"]+5)   #Here we just add 5 to the age column not assign the 5 to the column 
print(data)
#We can rename the column by using therename function
data.rename(columns={"Income":"Salary","Name":"Names"},inplace=True) 
print(data)
#We can add column into the dataframe
data["Promoted Salary"]=data["Salary"]+5000
print(data)
#Data Cleaning 
#if any of the column is null or Nan it simply remove the row and completely deleted when we use the inplace
# data.dropna(how="any",inplace=True)
# If all the columns are null then only it removes the row
# data.dropna(how="all",inplace=True)
# print(data)
# print(data.info())
data["Age"]=data["Age"].mean()
print(data)