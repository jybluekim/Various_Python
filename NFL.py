import pandas


df = pandas.read_csv("NFL_Players.csv")

#print (df)
#df2 = df.set_index("name")

#print (df2.iloc[0:3, 0:3])

df2 = df.loc[:, ["name", "birth_state", "college", "height", "weight", "year_start"]]

#print(df2)

df2.to_csv("NFL.csv")
