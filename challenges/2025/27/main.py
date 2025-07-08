def digits(n: int) -> int:
    return sum(len(str(i)) for i in range(1, n))
