import pandas as pd

#read the csv file
df = pd.read_csv("ml(pandas)/pokemon_data.csv")
#print(df.tail(4)) the tail and head show the a specific part of the data

#this section you can specify which data you want to show 
"""
print(df[{'Name','HP'}])
print(df.iloc[0:3])
print(df.iloc[1,2])
"""

#note it can also read other files not just csv
#when the data is seperated using \ or others you need to specify using delimeter
#df_xLsx = pd.read_csv("ml(pandas)/pokemon_data.txt", delimiter="\t")
#print(df_xLsx)

#for index of rows iterrate the rows of column of the name
#for index, row in df.iterrows():
#    print(index, row['Name'])

#the loc attribute is to specify which data you want to show
"""
print(df.loc[df['HP'] == 45])
print(df.describe())
print(df.sort_values(['Name', 'HP', 'Defense'], ascending = [1,0]))
"""

#this is for adding a new column name
"""
df['Total XP'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
print(df.head(3))
"""
#this is to drop the column(cancel it)
#print(df.drop(columns=['HP']))

#df['Total XP'] = df.iloc[:, 4:10].sum(axis=1)
"""
cols = list(df.columns)#this is the list of the column
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]#this is the specific column
print(df.head(3))

#this is to save file as csv file
df.to_csv("ml(pandas)/modified.csv", index=False)

df.to_excel("ml(pandas)/modified.xlsx", index=False)
#note there is no dilemiter when theres two csv file instead it's seperator

df.to_csv("ml(pandas)/modified.txt", index=False, sep="\t")
"""

"""
#this is for filtering ou the data
df_new = df.loc[(df['Type 1'] == "Grass") & (df['Type 2'] == "Poison") & (df['Sp. Atk'] < 100)]
#arrange the index in order
df_new.reset_index(drop=True, inplace=True)
"""
#the ~ means not
#find the string that contains mega and cancel it out
#new_df = df.loc[~df['Name'].str.contains("Mega")]

#import re
#the re is a regular module which lets us type the date in lowercase
#df.loc[df['Type 1'].str.contains('grass|fire', flags=re.I, regex=True)]
#you can filter specific alphabets of the str in the data. the * means zero or more
# the ^ means only start with the specific string 
#df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)]
#this line of code is to change the data
#g = df.loc[df['Type 1'] == 'Grass', 'Lagendary'] = True

df = pd.read_csv("ml(pandas)/pokemon_data.csv")
#this is to set it as a condition same as an if statement
#g = df.loc[df['HP'] < 50, ['Ganeration']] = "bitch"
#c = df.groupby(df['Type 1']).mean().sort_values('Attack', ascending=False)
#this section is for grouping the data sets 
"""
#this is to label in numbers of index
df['count'] = 1
c = df.groupby(df['Type 1']).count()['count']
"""

#this is to make a new dataframe but with the original column headings   
new_df = pd.DataFrame(columns=df.columns)
#this is to print the data 3 columns at a time 
for df in pd.read_csv("ml(pandas)/pokemon_data.csv", chunksize=3):
   results = df.groupby(['Type 1']).count()
   #take the new dataframe as a chunks and combined them with the results and store them back into the new dataframe
   new_df = pd.concat([new_df, results])
   