#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 14:56:33 2025

@author: lucky
"""

import os
import pandas as pd
from shutil import copy2
from sklearn.model_selection import train_test_split

# Set paths
source_dir = "/home/lucky/Documents/research/CREMA-D/AudioWAV"
dest_dir = "/home/lucky/Documents/research/split_audio"

# Load metadata
df = pd.read_csv("cremad_metadata.csv")

# Stratified splitting
train_df, temp_df = train_test_split(df, test_size=0.3, stratify=df["emotion"], random_state=42)
val_df, test_df = train_test_split(temp_df, test_size=0.5, stratify=temp_df["emotion"], random_state=42)

# Helper function to copy audio files
def copy_audio(split_df, split_name):
    audio_path = os.path.join(dest_dir, split_name)
    for filename in split_df["filename"]:
        src = os.path.join(source_dir, filename)
        dst = os.path.join(audio_path, filename)
        copy2(src, dst)

# Copy the files
copy_audio(train_df, "train")
copy_audio(val_df, "val")
copy_audio(test_df, "test")

# Save CSVs
train_df.to_csv("train.csv", index=False)
val_df.to_csv("val.csv", index=False)
test_df.to_csv("test.csv", index=False)

print("✅ Files copied and CSVs saved.")
