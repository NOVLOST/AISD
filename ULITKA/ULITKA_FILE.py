num=11
a=0
b=0
N=int(input("Введите число для формирования квадратной матрицы "))
print(num,'\n')
while  N-b != 1:
    for i in range(b+0,N-1-a):
        num += 1
        print(num,'\n')
    if a!=0:
        b += 1
    for i in range(b+0,N-1-a):
        num += 10
        print(num, '\n')
    for i in range(b+0,N-1-a):
        num -= 1
        print(num, '\n')
    a += 1
    for i in range(b+0,N-1-a):
        num -=10
        print(num, '\n')
