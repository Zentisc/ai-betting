import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier

FEATURE_FILE = "data/features.csv"

MODEL_FILE = "models/trained_model.pkl"
FEATURE_LIST_FILE = "models/feature_list.pkl"


def train_model():

    print("Loading features dataset...")

    df = pd.read_csv(FEATURE_FILE, low_memory=False)

    # Zielvariable
    df["target"] = df["FTR"].map({
        "H": 0,
        "D": 1,
        "A": 2
    })

    # ALLE Leak-Spalten entfernen
    forbidden = [
        "FTR","HTR",
        "FTHG","FTAG",
        "HTHG","HTAG",
        "HS","AS",
        "HST","AST",
        "HC","AC",
        "HY","AY",
        "HR","AR"
    ]

    df = df.drop(columns=[c for c in forbidden if c in df.columns], errors="ignore")

    # nur numerische Features
    numeric_df = df.select_dtypes(include=["int64","float64"])

    X = numeric_df.drop(columns=["target"], errors="ignore")
    y = numeric_df["target"]

    features = X.columns.tolist()

    print("Training with", len(features), "features")

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = XGBClassifier(
        n_estimators=300,
        max_depth=6,
        learning_rate=0.05,
        subsample=0.8,
        colsample_bytree=0.8,
        eval_metric="mlogloss"
    )

    print("Training model...")

    model.fit(X_train, y_train)

    preds = model.predict(X_test)

    acc = accuracy_score(y_test, preds)

    print("Model accuracy:", acc)

    joblib.dump(model, MODEL_FILE)
    joblib.dump(features, FEATURE_LIST_FILE)

    print("Model saved:", MODEL_FILE)
    print("Feature list saved:", FEATURE_LIST_FILE)


if __name__ == "__main__":
    train_model()