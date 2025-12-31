with open('input', 'r') as f:
    lines = [line.rstrip('\n') for line in f if line.rstrip('\n') != '']

grid = [list(line) for line in lines]

def adjacent_papers(grid, r, c):
    """
    Return a list of (row, col, char) for all adjacent cells around (r,c),
    and also provide a convenience list of just the adjacent characters.
    """
    dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    R = len(grid)
    C = len(grid[0]) if R else 0
    res = []
    for dr, dc in dirs:
        rr, cc = r + dr, c + dc
        if 0 <= rr < R and 0 <= cc < C:
            res.append((rr, cc, grid[rr][cc]))
    return res

def count_adjacent_rolls(grid, r, c):
    """Return the number of rolls ('@') adjacent to (r,c)."""
    adj = adjacent_papers(grid, r, c)
    return sum(1 for (_, _, ch) in adj if ch == '@')


def forklift_can_access(grid, r, c):
    """Return True if cell (r,c) is a roll and has fewer than 4 adjacent rolls."""
    if not grid:
        return False
    R = len(grid)
    C = len(grid[0]) if R else 0
    if not (0 <= r < R and 0 <= c < C):
        return False
    if grid[r][c] != '@':
        return False
    return count_adjacent_rolls(grid, r, c) < 4


# example: check a single cell and compute total accessible rolls
adj = adjacent_papers(grid, 2, 2)
adj_coords_items = adj
adj_items = [ch for (_, _, ch) in adj]

def annotate_accessible(grid):
    """Return a new grid (list of lists) where accessible rolls ('@') are
    replaced with 'x', and also return the total count of accessible rolls.
    """
    R = len(grid)
    C = len(grid[0]) if R else 0
    annotated = [list(row) for row in grid]
    total = 0
    for r in range(R):
        for c in range(C):
            if forklift_can_access(grid, r, c):
                annotated[r][c] = 'x'
                total += 1
    return annotated, total


annotated_grid, accessible_total = annotate_accessible(grid)

for row in annotated_grid:
    print(''.join(row))

print(f"Accessible rolls: {accessible_total}")


def iterative_remove(grid):
    """Remove accessible rolls iteratively.

    Repeatedly find all rolls that a forklift can access (fewer than 4
    adjacent '@') and replace them with '.' until no more can be removed.
    Returns the final grid, total removed, and number of iterations.
    """
    # work on a copy
    G = [list(row) for row in grid]
    total_removed = 0
    iterations = 0
    while True:
        to_remove = []
        R = len(G)
        C = len(G[0]) if R else 0
        for r in range(R):
            for c in range(C):
                if forklift_can_access(G, r, c):
                    to_remove.append((r, c))
        if not to_remove:
            break
        iterations += 1
        for (r, c) in to_remove:
            G[r][c] = '.'
            total_removed += 1
    return G, total_removed, iterations


final_grid, removed, rounds = iterative_remove(grid)
print(f"Removed total: {removed} in {rounds} rounds")
for row in final_grid:
    print(''.join(row))

