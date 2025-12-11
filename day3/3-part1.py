with open('input', 'r') as f:
    banks = [line.strip() for line in f if line.strip() ]

jolts = []
for bank in banks:
    print(f'bank {bank}')
    bank = list(bank)
    #bank.sort(reverse=True)
    #print(f'bank {bank}')
    jolt = 0
    for i in range(len(bank)-1):
        currentjolt = bank[i] + bank[i+1]
        currentjolt = int(currentjolt)
        if currentjolt > jolt:
            jolt = currentjolt
        for j in range(i+1, len(bank)):
            currentjolt = int(bank[i] + bank[j])
            if currentjolt > jolt:
                jolt = currentjolt
        print(f'currentjolt {currentjolt}')
        print(f'jolt {jolt}')
    jolts.append(jolt)

print(f'banks length: {len(banks)}')
print(f'jolts length: {len(jolts)}')
print(jolts)
print(sum(jolts))
