import random
pol = 0
s=0
i=0
k=1
aar = []
N=int(input('Ввод: '))
A=[[random.randrange(10) for i in range(N)] for j in range(N)]
for row in range(N):
    for col in range(row + 1, N):
         s+=A[row][col]

for row in range(N):
    aar.append(input())
    if N > 0:
        pol += 1
print('Сумма:', s)
print('Число:', pol)