"""15.Формируется матрица F следующим образом: если в Е количество чисел, больших К в четных столбцах в области 1 больше,
чем сумма чисел в нечетных строках в области 3, то поменять в Е симметрично области 1 и 3 местами, иначе В и С поменять местами несимметрично.
При этом матрица А не меняется. После чего вычисляется выражение: A*F– K*AT . Выводятся по мере формирования А, F и все матричные операции последовательно."""
import random
sumE=0
sumB=0
K=int(input("Введите К="))
N=int(input("Введите N="))

"""формируем матрици размеров N/2 с случайными значением от -10 до 10"""
D =  [[random.randint(-10,10 ) for j in range(N//2)] for i in range(N//2)]
E =  [[random.randint(-10,10 ) for j in range(N//2)] for i in range(N//2)]
C =  [[random.randint(-10,10 ) for j in range(N//2)] for i in range(N//2)]
B =  [[random.randint(-10,10 ) for j in range(N//2)] for i in range(N//2)]
G = [ [0]*((N//2)*2) for i in range((N//2)*2) ]
H = [ [0]*((N//2)*2) for i in range((N//2)*2) ]
A = [D[i] + E[i]  for i in range(N//2)]
A += [C[i] + B[i] for i in range(N//2)]
print("матрица A\n",A,"\n\n")

"""ищем количество чисел больших к в четных столбцах 1 области матрицы Е"""
for i in range(1,len(E),2):
    for j in range(1,len(E[i]),1):
        if E[j][i] > K and j < i and j > (N//2) - 1 - i:  sumE += 1

    """сумма чисел в нечетных строках в области 3 матрицы E"""
for i in range(0,len(E),2):
    for j in range(0,len(E[i]),1):
        if j > i and j > (N//2) - 1 - i:   sumB += E[i][j]

"""Если количество чисел больших к в четных столбцах 1 области матрицы Е 
больше чем сумма чисел в нечетных строках в области 3 матрицы E
меняем в Е симметрично области 1 и 3 местами, иначе В и С поменять местами несимметрично."""
if sumE > sumB:
    g = -1
    m = -1
    for i in range(0,(N//4),1):
        g += 2
        m += 1
        for j in range(1+m , N//2-m-1 , 1 ):
            cont = E[j][i]
            E[j][i]=E[j][i-g]
            E[j][i-g]= cont
    print("подматрица E с симетрично перенесенными областями 1 и 3\n",E,"\n")
    F = [D[i] + E[i] for i in range(N // 2)]
    F += [C[i] + B[i] for i in range(N // 2)]
else:
    F = [D[i] + E[i]  for i in range(N//2)]
    F += [B[i] + C[i] for i in range(N//2)]
print("матрица F\n",F,"\n")
for g in range(len(A)):
    for i in range(len(F[0])):
        for k in range(len(F)):G[g][i] += A[g][k] * F[k][i]
print("Результат выражения A*F\n",G,"\n")

for g in range(len(A)):
    for i in range(len(A[0])):H[i][g]=A[g][i]
print("Транспонированная матрица А\n",H,"\n")

for g in range(len(A)):
    for i in range(len(A[0])): H[g][i] = H[g][i] * K
print("Транспонированная матрица А умноженная на K\n",H,"\n")

for g in range(len(A)):
    for i in range(len(A[0])): G[g][i]=G[g][i]-H[g][i]
print("Конечный результат\n",G,"\n")























