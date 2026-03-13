import pandas as pd
import joblib

MODEL_FILE = "models/trained_model.pkl"
FEATURE_FILE = "data/features.csv"
FEATURE_LIST = "models/feature_list.pkl"

OUTPUT_FILE = "data/predictions.csv"


def predict():

    print("Loading model...")

    model = joblib.load(MODEL_FILE)
    features = joblib.load(FEATURE_LIST)

    df = pd.read_csv(FEATURE_FILE, low_memory=False)

    numeric_df = df.select_dtypes(include=["int64", "float64"])

    # nur Features verwenden die wirklich existieren
    valid_features = [f for f in features if f in numeric_df.columns]

    X = numeric_df[valid_features]

    probs = model.predict_proba(X)

    if probs.shape[1] == 3:

        df["prob_home"] = probs[:, 0]
        df["prob_draw"] = probs[:, 1]
        df["prob_away"] = probs[:, 2]

    else:

        df["prob_home"] = probs[:, 0]
        df["prob_draw"] = 0
        df["prob_away"] = probs[:, 1]

    df.to_csv(OUTPUT_FILE, index=False)

    print("Predictions saved:", OUTPUT_FILE)


if __name__ == "__main__":
    predict()