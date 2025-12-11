with open('input', 'r') as f:
    data = [item for line in f if line.strip() for item in line.strip().split(',')]

invalid_ids = []
for item in data:
    start, end = map(int, item.split('-'))
    for num in range(start, end + 1):
        num_str = str(num)
        mid = len(num_str) // 2
        left_half = num_str[:mid]
        right_half = num_str[mid:]
        if left_half == right_half:
            invalid_ids.append(num)

print(invalid_ids)
print(sum(invalid_ids))