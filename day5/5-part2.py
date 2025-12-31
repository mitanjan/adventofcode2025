with open('input', 'r') as f:
    lines = [line.rstrip('\n') for line in f if line.rstrip('\n') != '']

fresh_ids = [l for l in lines if "-" in l]
ingredient_ids = [l for l in lines if "-" not in l]

#print(fresh_ids)
#print(ingredient_ids)

intervals = []

for fresh_id in fresh_ids:
    start, end = map(int, fresh_id.split("-"))
    intervals.append((start, end))

# Merge overlapping intervals
intervals.sort()
merged = []
for s, e in intervals:
    if not merged or s > merged[-1][1] + 1:
        merged.append([s, e])
    else:
        merged[-1][1] = max(merged[-1][1], e)

# Count numbers without expanding
count = sum(e - s + 1 for s, e in merged)
print(count)


