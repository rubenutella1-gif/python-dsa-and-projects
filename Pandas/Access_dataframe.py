import pandas as pd
import numpy as np
data={
    "Name":["Rubenu","Ramesh","Prabhas","Kiran","Sudhansh","Rohan"],
    "Age":[22,23,25,23,np.nan,30],
    "Role":["SD","HR","Manager","Recruiter","HR","SD"],
    "Income":[24000,30000,np.nan,34000,np.nan,25000]
}
s=pd.DataFrame(data)
print(s)
print(s.head())#By default it returns the first 5 elements of the dataframe
print(s.tail())#By default it returns the last 5 elements of the dataframe
print(s.head(2))#Returns first 2 occurences of the data
#We can use the loc and the iloc functions to access the elements
print(s.iloc[1:4]) #indexes based accessing stop point is not included
print(s.loc[1:4]) #label based accessing stop point is included
#If we want specified columns in the dataframes we can use another brace inside the brace and pass the columns in it
print(s.loc[0::,["Name","Role"]])