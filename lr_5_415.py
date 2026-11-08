numbers = list(map(int, input().split(',')))

result = numbers[::2]

print(','.join(map(str, result)))