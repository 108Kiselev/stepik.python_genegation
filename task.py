n = int(input())

pas = [[1], [1, 1], [1, 2, 1]]

for i in range(3, n+1):
    row = []
    row.append(1)
    for j in range(1, len(pas[i-1])):
        row.append(pas[-1][j-1] + pas[-1][j])
    row.append(1)
    pas.append(row)
print(pas[n])