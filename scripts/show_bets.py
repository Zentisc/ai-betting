import pandas as pd

def show_bets():

    df = pd.read_csv("data/top_bets.csv")

    print("\n🔥 TOP AI BETS\n")

    for _, row in df.iterrows():

        print(row["match"])
        print("Bet:", row["bet"])
        print("Probability:", round(row["probability"]*100,1),"%")
        print("------------------------------")

if __name__ == "__main__":
    show_bets()