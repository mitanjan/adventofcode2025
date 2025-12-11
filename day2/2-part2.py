with open('input', 'r') as f:
    data = [item for line in f if line.strip() for item in line.strip().split(',')]

invalid_ids = []
for item in data:
    start, end = map(int, item.split('-'))
    for num in range(start, end + 1):
        num_str = str(num)
        # check equal-length partitions: yield partitions where every part has same length
        def equal_partitions(s):
            n = len(s)
            if n == 0:
                yield []
                return
            for k in range(1, n+1):
                if n % k == 0:
                    part_len = n // k
                    yield [s[i:i+part_len] for i in range(0, n, part_len)]

        # if any equal-length partition has all identical blocks (and more than 1 block), mark it
        for parts in equal_partitions(num_str):
            if len(parts) > 1 and len(set(parts)) == 1:
                invalid_ids.append(num)
                break


print(invalid_ids)
print(sum(invalid_ids))