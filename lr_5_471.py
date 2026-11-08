numbers = list(map(int, input().split()))

positives = sorted([i for i in numbers if i > 0], reverse = True)

negatives = sorted([i for i in numbers if i < 0], reverse = True)

result = positives + negatives

print(*result)