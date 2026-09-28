import pandas as pd

#The json file created in task1
filepath="data/trends_280926.json"

#Load json into panda dataframe
df=pd.read_json(filepath)
print("stories", len(df))

#Removing duplicate story
df=df.drop_duplicates(subset="post_id")
print(f"after removing duplicates",len(df))

#Convert into integers and removes  row with missing values
df["score"]=pd.to_numeric(df["score"],errors="coerce")
df["num_comments"]=pd.to_numeric(df["num_comments"],errors="coerce")
df=df.dropna(subset=["score","num_comments"])
df["score"]=df["score"].astype(int)
df["num_comments"]=df["num_comments"].astype(int)

#Convert title to string removes space
df["title"]=df["title"].astype(str)
df["title"]=df["title"].str.strip()

#cleaned data save as csv
outputfile="data/trendpulse_cleandata.csv"
df.to_csv(outputfile, index=False)

#print stories 
print(f"Number of stories: {len(df)}")
print(f"Csv file: {outputfile}")
print(df["category"].value_counts())

