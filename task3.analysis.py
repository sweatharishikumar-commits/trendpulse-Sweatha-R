import pandas as pd
import numpy as np

# Load CSV file
filepath = "data/trendpulse_cleandata.csv"
df = pd.read_csv(filepath)
print("Loaded data:",df.shape)
print(df.head())

numeric_columns=df.select_dtypes(include=np.number).columns
print("\nMean:")
print(df[numeric_columns].mean())
print("\nMedian:")
print(df[numeric_columns].median())
print("\nMinimum:")
print(df[numeric_columns].min())
print("\nMaximum:")
print(df[numeric_columns].max())

# Standard deviation using NumPy
print("\nStandard deviation:")
for column in numeric_columns:
    print(column, ":", np.std(df[column]))
# number of stories per category
category_count = df["category"].value_counts()
print("\nStories per category:")
print(category_count)

# Average score by category
category_score = df.groupby("category")["score"].mean()
print("\nAverage score by category:")
print(category_score)

# Average comments by category
category_comments = df.groupby("category")["num_comments"].mean()
print("\nAverage comments by category:")
print(category_comments)

# Top 10 stories by score
top_stories = df.nlargest(10, "score")
print("\nTop 10 stories by score:")
print(top_stories[["title", "score", "category"]])

# Top 10 most commented stories
most_commented = df.nlargest(10, "num_comments")

print("\nTop 10 most commented stories:")
print(most_commented[["title", "num_comments", "category"]])

# Correlation between score and comments
correlation = df["score"].corr(df["num_comments"])

print("\nCorrelation between score and comments:")
print(correlation)

#Save analysed data task4
output_path="data/trends_analysed.csv"
df.to_csv(output_path,index=False)
print("\nSaved to",output_path)