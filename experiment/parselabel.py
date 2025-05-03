import os
import pandas as pd

data_dir = "/home/lucky/Documents/research/CREMA-D/AudioWAV"
files = [f for f in os.listdir(data_dir) if f.endswith(".wav")]

data = []
for f in files:
    parts = f.split("_")
    if len(parts) == 4:
        actor = parts[0]
        sentence = parts[1]
        emotion = parts[2]
        level = parts[3].replace(".wav", "")
        data.append((f, actor, sentence, emotion, level))

df = pd.DataFrame(data, columns=["filename", "actor", "sentence", "emotion", "level"])
df.to_csv("cremad_metadata.csv", index=False)  # <-- save the CSV
print("Saved to cremad_metadata.csv")
