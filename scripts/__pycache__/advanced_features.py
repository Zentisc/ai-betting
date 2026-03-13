def add_differences(df):

    if "HS" in df.columns and "AS" in df.columns:
        df["shots_diff"] = df["HS"] - df["AS"]

    if "HST" in df.columns and "AST" in df.columns:
        df["shots_target_diff"] = df["HST"] - df["AST"]

    if "home_elo" in df.columns and "away_elo" in df.columns:
        df["elo_diff"] = df["home_elo"] - df["away_elo"]

    if "home_xg" in df.columns and "away_xg" in df.columns:
        df["xg_diff"] = df["home_xg"] - df["away_xg"]

    if "home_strength" in df.columns and "away_strength" in df.columns:
        df["strength_diff"] = df["home_strength"] - df["away_strength"]

    return df