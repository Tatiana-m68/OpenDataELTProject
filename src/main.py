import requests
import pandas as pd
from pathlib import Path

# Constants
ITUNES_API = "https://itunes.apple.com/search?term=beatles&limit=50"

# Paths
BASE_DIR = Path(__file__).resolve().parents[1]
RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"

RAW_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

# --------------------
# Extract
# --------------------
response = requests.get(ITUNES_API)

if response.status_code != 200:
    raise RuntimeError(f"API request failed with status {response.status_code}")

data = response.json()

# Normalize nested json to DataFrame
df = pd.json_normalize(data.get("results", []))

# Save raw
df.to_csv(RAW_DIR / "raw.csv", index=False)

# --------------------
# Transform
# --------------------
# Ensure releaseDate is datetime
if "releaseDate" in df.columns:
    df["releaseDate"] = pd.to_datetime(df["releaseDate"], errors="coerce")

# Filter by artist
df_filtered = df[df["artistName"].str.contains("John Lennon", case=False, na=False)]

# Sort by release date
df_sorted = df_filtered.sort_values("releaseDate")

# Remove empty columns and clean NaNs
df_clean = (
    df_sorted.replace("", pd.NA)
             .dropna(axis=1, how="all")
)

# --------------------
# Load (save processed)
# --------------------
df_clean.to_csv(PROCESSED_DIR / "output.csv", index=False)