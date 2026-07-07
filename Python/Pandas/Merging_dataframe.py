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
    "Role":["SD","HR","Manager"],
    "Location":["Hyderabad","Chennai","Delhi"]
    
}
s1=pd.DataFrame(data1)
print(s1)
#we can perform all the join operations in the data of two tables
s2=pd.merge(s,s1,on="Role",how="left")
print(s2)
s3=pd.merge(s,s1,on="Role")
print(s3)