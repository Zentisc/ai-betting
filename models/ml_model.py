
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

FEATURE_FILE = "data/features.csv"
MODEL_FILE = "models/trained_model.pkl"
FEATURE_LIST = "models/feature_list.pkl"

def train_model():

    print("Loading features dataset...")

    df = pd.read_csv(FEATURE_FILE)

    X = df.drop(columns=["target"])
    y = df["target"]

    feature_names = list(X.columns)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    print("Training model...")

    model = RandomForestClassifier(
        n_estimators=300,
        max_depth=10,
        random_state=42
    )

    model.fit(X_train, y_train)

    preds = model.predict(X_test)

    acc = accuracy_score(y_test, preds)

    print("Model accuracy:", acc)

    joblib.dump(model, MODEL_FILE)
    joblib.dump(feature_names, FEATURE_LIST)

    print("Model saved:", MODEL_FILE)
    print("Feature list saved:", FEATURE_LIST)


if __name__ == "__main__":
    train_model()