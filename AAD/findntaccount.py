import pandas as pd

# Preparation: 
# 1.Download the global user list, retain NT account and email 2 columns, file name "exportglobalusers.csv"
# 2.Download cn user list, retain user name column, file name "exportcnusers.csv"
# 3.Add column name for tables

df1 = pd.read_csv ("exportglobalusers.csv")
df2 = pd.read_csv ("exportcnusers.csv")

#remove the domain name after @ and lower
df1 ["email"] = df1 ["email"].str.split ("@").str [0] 
df1 ["email"] = df1 ["email"].str.lower()

# #vlookup the two table
df3 = pd.merge (df1, df2, how="right", on="email")

#remove the blank rows
df3.dropna(inplace=True)
df3.to_csv("ntaccounts.csv")

# #find the duplicated rows and manually fix it by updating the output of df3
dup = df3.duplicated(subset="email", keep=False)
dup_rows = df3[dup]
print(dup_rows)
