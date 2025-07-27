import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset from URL
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Drop rows with missing age
df = df.dropna(subset=['Age'])

# Create age groups
bins = [0, 20, 40, 60, 80]
labels = ['0–20', '21–40', '41–60', '61–80']
df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels)

# Count values
age_group_counts = df['Age Group'].value_counts().sort_index()
gender_counts = df['Sex'].value_counts()

# Plot Age Group Distribution
plt.figure(figsize=(8, 5))
sns.barplot(x=age_group_counts.index, y=age_group_counts.values, palette="Blues")
plt.title("Titanic Age Group Distribution")
plt.xlabel("Age Group")
plt.ylabel("Number of Passengers")
for i, count in enumerate(age_group_counts.values):
    plt.text(i, count + 5, str(int(count)), ha='center')
plt.tight_layout()
plt.show()

# Plot Gender Distribution
plt.figure(figsize=(6, 4))
sns.barplot(x=gender_counts.index, y=gender_counts.values, palette="Set2")
plt.title("Titanic Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
for i, count in enumerate(gender_counts.values):
    plt.text(i, count + 5, str(int(count)), ha='center')
plt.tight_layout()
plt.show()
