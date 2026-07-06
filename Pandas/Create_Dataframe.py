# A DataFrame is a two-dimensional, labeled data structure in Pandas that consists of rows and columns
# A DataFrame is like a table 
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
print(s.info())
print(s.describe())