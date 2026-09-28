import pandas as pd
import matplotlib.pyplot as plt
import os

# Load analysed CSV
filepath = "data/trends_analysed.csv"
df = pd.read_csv(filepath)
print("Loaded data:",df.shape)
os.makedirs("Visualisations",exist_ok=True)


# Chart1 Number of Stories by Category
category_count = df["category"].value_counts()
plt.figure(figsize=(10, 6))
category_count.plot(kind="bar")
plt.title("Number of Hacker News Stories by Category")
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("visualisations/stories_by_category.png")
plt.show()

#Chart2 Average Score by Category
average_score = df.groupby("category")["score"].mean()
plt.figure(figsize=(10, 6))
average_score.plot(kind="bar")
plt.title("Average Hacker News Score by Category")
plt.xlabel("Category")
plt.ylabel("Average Score")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("visualisations/average_score.png")
plt.show()

#Chart3 Score vs Number of Comments
plt.figure(figsize=(10, 6))
for category in df["category"].unique():
    category_data = df[df["category"] == category]
    plt.scatter(
        category_data["score"],
        category_data["num_comments"],
        label=category
    )
plt.title("Hacker News Score vs Number of Comments")
plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.legend()
plt.tight_layout()
plt.savefig("visualisations/score_vs_comments.png")
plt.show()

print("\nVisualisations saved in:")
print("visualisations/")
print("\nFiles created:")
print("1. stories_by_category.png")
print("2. average_score.png")
print("3. average_comments.png")
print("4. score_vs_comments.png")