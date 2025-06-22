def birthday_cake_candles(candles: list[int]) -> int:
    return candles.count(max(candles)) if candles else 0
