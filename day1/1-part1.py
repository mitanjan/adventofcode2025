start = 50

with open('input.txt', 'r') as f:
    data = [line.strip() for line in f if line.strip()]

print(f"The dial starts by pointing at {start}.")

results = []
counter = 0
for item in data:
    dirc = item[0]
    number = int(item[1:])
    if dirc == 'R':
        # rotate right (toward higher numbers)
        result = (start + number) % 100
    else:
        # rotate left (toward lower numbers)
        result = (start - number) % 100

    results.append(result)
    if result == 0:
        counter += 1
    print(f"The dial is rotated {item} to point at {result}.")
    start = result

print(f"\nCounter: {counter}")

