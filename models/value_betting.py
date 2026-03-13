def calculate_value(prob, odds):

    value = prob * odds

    if value > 1:
        return True
    else:
        return False