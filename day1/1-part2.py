start = 50

with open('input.txt', 'r') as f:
    data = [line.strip() for line in f if line.strip()]

print(f"The dial starts by pointing at {start}.")

results = []
counter = 0
M = 100
for item in data:
    dirc = item[0]
    number = int(item[1:])

    if dirc == 'R':
        result = (start + number) % M
        first_k = (M - start) % M
        if first_k == 0:
            first_k = M
    else:  # 'L'
        result = (start - number) % M
        first_k = start % M
        if first_k == 0:
            first_k = M

    zeros = 0 if number < first_k else 1 + (number - first_k) // M
    counter += zeros

    print(f"start {start}\nrotation {item}\nresult {result}\ncounter {counter}\n")
    results.append(result)
    start = result
print(f"\nCounter: {counter}")

