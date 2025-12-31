with open('input', 'r') as f:
    lines = [line.rstrip('\n') for line in f if line.rstrip('\n') != '']

grid = [list(line) for line in lines]
print(grid)

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

adj = adjacent_papers(grid, 2, 2)
adj_coords_items = adj
adj_items = [ch for (_, _, ch) in adj]

print(f'adjacent coords+items {adj_coords_items}')
print(f'adjacent items {adj_items}')

