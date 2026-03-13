import pandas as pd
import joblib

MODEL_FILE = "models/trained_model.pkl"
FEATURE_LIST_FILE = "models/feature_list.pkl"

UPCOMING_FILE = "data/upcoming_matches.csv"

OUTPUT_FILE = "data/upcoming_predictions.csv"


def predict():

    print("Predicting upcoming matches...")

    model = joblib.load(MODEL_FILE)
    features = joblib.load(FEATURE_LIST_FILE)

    df = pd.read_csv(UPCOMING_FILE)

    for f in features:
        if f not in df.columns:
            df[f] = 0

    X = df[features]

    probs = model.predict_proba(X)

    df["prob_home"] = probs[:, 0]
    df["prob_draw"] = probs[:, 1]
    df["prob_away"] = probs[:, 2]

    df.to_csv(OUTPUT_FILE, index=False)

    print("Predictions saved:", OUTPUT_FILE)


if __name__ == "__main__":
    predict()