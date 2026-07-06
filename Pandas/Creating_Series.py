# If we want to use pandas library first we should import the pandas library    
import pandas as pd

#we can create data in two ways one is series type and second one is in dataframe
#Series means we can create one dimensional data which means one dimensional labled data
#We can create 1D data by using the lists and Dictionaries
s=pd.Series((1,2,3,4,5,6),index=("a","b","c","d","e","f"),name="Rubenu")
print(s) #python always give index from zero (0) only the left side is index and the right side is value

#We can add index value to the data 
s.index=range(1,len(s)+1)
print(s)

#we can create series by using the dictiories here the key value is
#automatically assigned as the index value to the series data
data={1:"Ruben",2:"Ramesh",3:"Kiran",4:"Prabhas",5:"Sudhansh"}
s1=pd.Series(data)
print(s1)