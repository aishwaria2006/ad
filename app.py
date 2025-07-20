import pandas as pd
import os

# Load the CSV
df = pd.read_csv("data.csv")

# Check the content
print("First 5 rows:")
print(df.head())

# Check if files exist
print("\nFile existence check:")
df['file_exists'] = df['filepath'].apply(lambda x: os.path.exists(x))
print(df[['filepath', 'file_exists']])

# Check for missing labels
print("\nMissing values:")
print(df.isnull().sum())

print("\nUnique labels:", df['label'].unique())
