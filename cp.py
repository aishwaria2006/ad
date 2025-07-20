import os
import pandas as pd

# Base paths
base_path = r"D:\projects\Big Projects\AD detection"
dementia_path = os.path.join(base_path, "dementia")
nodementia_path = os.path.join(base_path, "nodementia")

# Collect data
data = []

# For dementia class
for person_folder in os.listdir(dementia_path):
    person_path = os.path.join(dementia_path, person_folder)
    for file in os.listdir(person_path):
        if file.endswith(".wav"):
            full_path = os.path.join(person_path, file)
            data.append([full_path, "dementia"])

# For nodementia class
for person_folder in os.listdir(nodementia_path):
    person_path = os.path.join(nodementia_path, person_folder)
    for file in os.listdir(person_path):
        if file.endswith(".wav"):
            full_path = os.path.join(person_path, file)
            data.append([full_path, "nodementia"])

# Create CSV
df = pd.DataFrame(data, columns=["filepath", "label"])
df.to_csv("data.csv", index=False)
print("CSV generated with", len(df), "samples.")
