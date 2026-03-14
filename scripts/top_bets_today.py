import pandas as pd

print("Finding best bets for next 48 hours...")

df = pd.read_csv("data/upcoming_predictions.csv")

bets = []

for _, row in df.iterrows():

    home = row["HomeTeam"]
    away = row["AwayTeam"]

    prob_home = row["prob_home"]
    prob_draw = row["prob_draw"]
    prob_away = row["prob_away"]

    # --- 1X2 prediction ---
    probs_1x2 = {
        "HOME": prob_home,
        "DRAW": prob_draw,
        "AWAY": prob_away
    }

    best_1x2 = max(probs_1x2, key=probs_1x2.get)
    best_1x2_prob = probs_1x2[best_1x2]

    # --- BTTS ---
    prob_btts = min(prob_home + prob_away, 0.95)
    prob_no_btts = 1 - prob_btts

    if prob_btts > prob_no_btts:
        btts_pick = "BTTS YES"
        btts_prob = prob_btts
    else:
        btts_pick = "BTTS NO"
        btts_prob = prob_no_btts

    # --- OVER UNDER ---
    prob_over25 = min(prob_home + prob_away + prob_draw/2, 0.95)
    prob_under25 = 1 - prob_over25

    if prob_over25 > prob_under25:
        ou_pick = "OVER 2.5"
        ou_prob = prob_over25
    else:
        ou_pick = "UNDER 2.5"
        ou_prob = prob_under25

    # --- BEST MARKET ---
    markets = {
        best_1x2: best_1x2_prob,
        btts_pick: btts_prob,
        ou_pick: ou_prob
    }

    best_market = max(markets, key=markets.get)
    best_prob = markets[best_market]

    bets.append({
        "match": f"{home} vs {away}",
        "bet": best_market,
        "prob": round(best_prob, 2)
    })

bets_df = pd.DataFrame(bets)

# sort by probability
bets_df = bets_df.sort_values("prob", ascending=False)

# FREE bet = best
free_bets = bets_df.head(1)

# VIP bets = next best
premium_bets = bets_df.head(4)

free_bets.to_csv("data/free_bets.csv", index=False)
premium_bets.to_csv("data/premium_bets.csv", index=False)

print("Saved:")
print("data/free_bets.csv")
print("data/premium_bets.csv")