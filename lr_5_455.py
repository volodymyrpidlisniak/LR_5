seq1 = list(map(int, input().split(',')))
seq2 = list(map(int, input().split(',')))

common_elements = sorted(list(set(seq1) & set(seq2)))

print(*common_elements)