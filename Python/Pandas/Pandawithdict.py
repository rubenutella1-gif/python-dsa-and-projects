import pandas as pd
player_score={
    "Dhoni":99,
    "Virat":99,
    "Rohit":99,
    'Hardik':90,
    'dube':90,
    'abhishek':85,
    'ishan':95
}
d=pd.Series(player_score,name="Indian cricket team" )
print(d)
print(d["Dhoni"])
print(d[["Dhoni","Rohit"]])
print(d.loc["Dhoni":"Rohit"])
#Conditional selections
print(d[d>90])
#Logical operations
print(d[(d>95) and (d<100)])