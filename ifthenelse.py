# arjan codes
# https://www.youtube.com/shorts/psu7LYIyQAo

# anstelle von if then else besser dict verwenden. 
# bsp.

def should_buy(prices: list[int], strategy: str) -> str:
    if strategy == "avg":
        return should_buy_avg(prices)
    elif strategy == "minmax":
        return should_buy_minmax(prices)
    elif strategy == "price_drop":
        return should_buy_price_drop(prices)
    else:
        raise ValueError


# Besser
BUY_STRATEGIES = {
    "avg": should_buy_avg,
    "minmax" : should_buy_minmax,
    "price_drop": should_buy_price_drop
}

def should_buy(prices: list[int], strategy: str) -> str:
    return BUY_STRATEGIES[strategy](prices)
