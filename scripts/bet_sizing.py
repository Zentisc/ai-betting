def kelly(probability, odds, bankroll):

    edge = (probability * odds) - 1

    fraction = edge / (odds - 1)

    stake = bankroll * fraction

    if stake < 0:
        return 0

    return round(stake,2)