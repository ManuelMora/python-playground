import math


def getDecimalsFromNumber(value: float) -> float:
    decimalVal = round(value, 2)
    return float((abs(decimalVal) % 1))


def getRoundedValue(value: float, amount: float) -> float:
    if amount < 5:
        decimals = getDecimalsFromNumber(value)
        return math.floor(value) + decimals

    decimals = getDecimalsFromNumber(value)

    print(f"decimals = {decimals}")
    dec = 0 if decimals <= 0.39 else (0.5 if decimals <= 0.79 else 1)

    roundedValue = math.floor(value) + dec

    if roundedValue == amount:
        return amount + 1

    return roundedValue


print(getRoundedValue((23 * 3.6), 23))
print(getRoundedValue((12.79), 23))