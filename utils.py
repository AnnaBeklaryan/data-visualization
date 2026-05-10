import pandas as pd

def load_data():
    apps = pd.read_csv("data/raw/googleplaystore.csv")

    relevant_cols = [
        "App", "Category", "Rating", "Reviews",
        "Installs", "Type", "Price", "Content Rating"
    ]

    apps = apps[relevant_cols].copy()

    apps = apps[apps["Rating"] <= 5]

    apps["Reviews"] = pd.to_numeric(apps["Reviews"], errors="coerce")

    apps["Installs"] = apps["Installs"].astype(str).str.replace(",", "", regex=False)
    apps["Installs"] = apps["Installs"].str.replace("+", "", regex=False)
    apps["Installs"] = pd.to_numeric(apps["Installs"], errors="coerce")

    apps["Price"] = apps["Price"].astype(str).str.replace("$", "", regex=False)
    apps["Price"] = pd.to_numeric(apps["Price"], errors="coerce")

    apps = apps.dropna(subset=["Category", "Rating", "Reviews", "Installs", "Type", "Price"])
    apps = apps.reset_index(drop=True)

    return apps