numbers = list(map(int, input().split()))
n = int(input())

result = [i for i in numbers if i < n]
print(*result)