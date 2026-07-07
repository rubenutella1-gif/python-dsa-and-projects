# Data Cleaning is the process of detecting and correcting (or removing) errors,
# missing values, and inconsistencies in data to improve its quality.
import pandas as pd
import numpy as np
data={
    "Name":["Rubenu","Ramesh","Prabhas","Kiran","Sudhansh","Rohan","Rubenu"],
    "Age":[22,23,25,23,np.nan,30,22],
    "Role":["SD","HR","Manager","Recruiter","HR","SD","SD"],
    "Income":[24000,30000,np.nan,34000,np.nan,25000,24000]
}
s=pd.DataFrame(data)
print(s)

#To check how many null values in the data we use isnull()
print(s.isnull().sum())

#We 2 options to clean the data one is to remove null values and other one is to get correct it
#1
s.dropna()
print(s.dropna(how="any")) # If any is null it removes the row
print(s.dropna(how="all")) # If all are null then only it removes the row
# s=s.fillna(0) #Replacing null value with zero
print(s)
s[["Age","Income"]]=s[["Age","Income"]].fillna(s[["Age","Income"]].median())
print(s)
s=s.drop_duplicates() # For remove duplicates we should use drop_duplicates
print(s)