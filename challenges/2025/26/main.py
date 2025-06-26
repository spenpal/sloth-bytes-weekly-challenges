def spiral_order(matrix: list[list[int]]) -> list[int]:
    if not matrix or not matrix[0]:
        return []

    res = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Traverse from left to right along the top row
        res.extend(matrix[top][col] for col in range(left, right + 1))
        top += 1

        # Traverse from top to bottom along the right column
        res.extend(matrix[row][right] for row in range(top, bottom + 1))
        right -= 1

        if top <= bottom:
            # Traverse from right to left along the bottom row
            res.extend(matrix[bottom][col] for col in range(right, left - 1, -1))
            bottom -= 1

        if left <= right:
            # Traverse from bottom to top along the left column
            res.extend(matrix[row][left] for row in range(bottom, top - 1, -1))
            left += 1

    return res
