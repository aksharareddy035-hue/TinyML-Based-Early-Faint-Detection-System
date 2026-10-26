
import pandas as pd
from pathlib import Path

file_path = Path("data/s1_sit.csv")

df = pd.read_csv(file_path)

print("\n--- DATASET OVERVIEW ---")
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])

print("\n--- COLUMN NAMES ---")
print(df.columns.tolist())

print("\n--- FIRST 5 ROWS ---")
print(df.head())

print("\n--- DATA TYPES ---")
print(df.dtypes)

print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

print("\n--- BASIC STATISTICS ---")
print(df.describe())


# Plot the physiological and motion signals

import matplotlib.pyplot as plt

signals = [
    "pleth_2",
    "a_x",
    "a_y",
    "a_z",
    "g_x",
    "g_y",
    "g_z"
]

# Remove rows with missing values in the selected signals
plot_df = df.dropna(subset=signals).copy()

# Plot the first 500 samples
fig, axes = plt.subplots(len(signals), 1, figsize=(12, 14))

for ax, signal in zip(axes, signals):
    ax.plot(plot_df[signal].iloc[:500])
    ax.set_title(signal)
    ax.set_xlabel("Sample number")
    ax.set_ylabel("Value")
    ax.grid(True)

plt.tight_layout()
plt.show()


# Check the sampling rate

df["time"] = pd.to_datetime(df["time"])

time_diff = df["time"].diff().dt.total_seconds()

print("Average time between samples:", time_diff.median(), "seconds")
print("Estimated sampling rate:", 1 / time_diff.median(), "Hz")
print("Recording duration:", (df["time"].iloc[-1] - df["time"].iloc[0]).total_seconds(), "seconds")

