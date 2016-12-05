print(61)
def get_odds():
    for odd in range(10):
        if odd % 2 == 1:
            yield odd
