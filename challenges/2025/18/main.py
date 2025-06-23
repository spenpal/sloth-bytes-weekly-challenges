from itertools import pairwise


def is_shuffled_well(nums: list[int]) -> bool:
    streak = 1
    for a, b in pairwise(nums):
        if abs(a - b) == 1:
            streak += 1
            if streak >= 3:
                return False
        else:
            streak = 1
    return True
