# Load model
import whisper
import pandas as pd
import os
from tqdm import tqdm

model = whisper.load_model("tiny")  # "small" or "medium" for better accuracy

# Load your data
df = pd.read_csv("D:/projects/Big Projects/AD detection/data.csv")

# Transcribe and add 'transcript' column
transcripts = []

for path in tqdm(df["filepath"]):
    try:
        result = model.transcribe(path)
        transcripts.append(result["text"])
    except Exception as e:
        print(f"Error transcribing {path}: {e}")
        transcripts.append("")

df["transcript"] = transcripts

# Save updated dataset
df.to_csv("D:/projects/Big Projects/AD detection/data_with_transcripts.csv", index=False)
