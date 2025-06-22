import math


def fact_of_fact(n: int) -> int:
    return math.prod(math.factorial(i) for i in range(1, n + 1))
