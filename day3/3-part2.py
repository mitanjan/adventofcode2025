"""Select the largest possible k-digit number from each input line
while preserving the order of digits. Results are stored in `jolts`.

Algorithm: greedy stack-based selection. For each line (string of digits)
we build the largest possible subsequence of length `k` by popping
smaller digits from the stack while we still have enough remaining
characters to fill `k` slots.
"""

def max_subsequence(s: str, k: int) -> str:
    """Return lexicographically largest subsequence of length k from s preserving order."""
    n = len(s)
    if k >= n:
        return s
    stack = []
    # number of characters we are allowed to remove (drop)
    to_remove = n - k
    for ch in s:
        while stack and to_remove > 0 and stack[-1] < ch:
            stack.pop()
            to_remove -= 1
        stack.append(ch)
    # stack may be longer than k if we never removed enough; take first k
    return ''.join(stack[:k])


def read_banks(path: str = 'input'):
    with open(path, 'r') as f:
        return [line.strip() for line in f if line.strip()]


if __name__ == '__main__':
    banks = read_banks('input')
    k = 12
    jolts = []
    for bank in banks:
        best = max_subsequence(bank, k)
        # convert to int; if leading zeros are possible they will be dropped by int()
        jolts.append(int(best))

    print('jolts =', jolts)
    print(sum(jolts))

