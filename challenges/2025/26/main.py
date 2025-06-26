DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))


def out_of_bounds(
    visited: set[tuple[int, int]], row_len: int, col_len: int, pos: tuple[int, int]
) -> bool:
    return pos in visited or not (0 <= pos[0] < row_len) or not (0 <= pos[1] < col_len)


def spiral_order(matrix: list[list[int]]) -> list[int]:
    if not matrix:
        return []
    res = []
    visited = set()
    row_len = len(matrix)
    col_len = len(matrix[0])
    num_of_elements = row_len * col_len
    pos = (0, 0)
    direction_index = 0
    while len(visited) < num_of_elements:
        row, col = pos
        visited.add(pos)
        res.append(matrix[row][col])

        next_pos = (
            row + DIRECTIONS[direction_index % len(DIRECTIONS)][0],
            col + DIRECTIONS[direction_index % len(DIRECTIONS)][1],
        )
        if out_of_bounds(visited, row_len, col_len, next_pos):
            direction_index += 1
            next_pos = (
                row + DIRECTIONS[direction_index % len(DIRECTIONS)][0],
                col + DIRECTIONS[direction_index % len(DIRECTIONS)][1],
            )
        pos = next_pos
    return res
