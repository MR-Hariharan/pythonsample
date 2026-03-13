import pandas as pd
data = {
    "StudentID": [101,102,103,104,105,106,107,108,109,110],
    "Name": ["Alice","Bob","Charlie","Diana","Ethan","Fiona","George","Hannah","Ivan","Julia"],
    "Age": [20,21,19,22,20,21,23,19,22,20],
    "Marks": [88,75,92,65,78,85,70,95,60,80],
    "Grade": ["A","B","A","C","B","A","B","A","C","B"]
}

df = pd.DataFrame(data)

df
df.to_csv("students.csv", index=False)

print("CSV file saved successfully")
df2 = pd.read_csv("students.csv")

print(df2)
print(df2.head(3))
print(df2.describe())
print(df2.shape)
print(df2.dtypes)
print(df2.info())
print(df2["Marks"].mean())
print(df2["Grade"].value_counts())      
print(df2[df2["Marks"] > 80])
