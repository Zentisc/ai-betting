import pandas as pd

INPUT_FILE = "data/raw_matches.csv"
OUTPUT_FILE = "data/features.csv"


def clean_columns(df):

    df.columns = (
        df.columns.astype(str)
        .str.replace(">", "_over_", regex=False)
        .str.replace("<", "_under_", regex=False)
        .str.replace("[", "", regex=False)
        .str.replace("]", "", regex=False)
        .str.replace(" ", "_", regex=False)
    )

    return df


def build_features():

    df = pd.read_csv(INPUT_FILE, low_memory=False)

    print("Dataset loaded:", len(df), "matches")

    df = clean_columns(df)

    # Entferne alle In-Game Statistiken (Data Leakage)
    forbidden = [
        "HS","AS","HST","AST",
        "HC","AC",
        "HY","AY",
        "HR","AR"
    ]

    df = df.drop(columns=[c for c in forbidden if c in df.columns], errors="ignore")

    df.to_csv(OUTPUT_FILE, index=False)

    print("Features saved:", OUTPUT_FILE)


if __name__ == "__main__":
    build_features()