""" С клавиатуры вводятся два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц,
B, C, D, E заполняется случайным образом целыми числами в интервале [-10,10]. Для тестирования использовать не случайное
заполнение, а целенаправленное.
Вид матрицы А:
D	Е
С	В
Для простоты все индексы в подматрицах относительные.
По сформированной матрице F (или ее частям) необходимо вывести не менее 3 разных графика.
Программа должна использовать функции библиотек numpy  и mathplotlib

15.Формируется матрица F следующим образом: скопировать в нее А и  если в Е количество чисел, больших К в четных столбцах
больше, чем сумма чисел в нечетных строках, то поменять местами С и Е симметрично, иначе В и С поменять местами несимметрично.
При этом матрица А не меняется. После чего если определитель матрицы А больше суммы диагональных элементов матрицы F,
то вычисляется выражение: A*AT – K * FТ, иначе вычисляется выражение (AТ +G-1-F-1)*K, где G-нижняя треугольная матрица, полученная из А.
Выводятся по мере формирования А, F и все матричные операции последовательно."""

import numpy as np
import matplotlib.pyplot as plt

sumE=0
sumB=0
K=int(input("Введите К="))
N=int(input("Введите N="))
"""формирем матрицы размером N/2xN/2 с случайным заполнением от -10 до 10 """
D = np.array(np.random.randint (-10, 10, ((N//2), (N//2))))
E = np.array(np.random.randint (-10, 10, ((N//2), (N//2))))
C = np.array(np.random.randint (-10, 10, ((N//2), (N//2))))
B = np.array(np.random.randint (-10, 10, ((N//2), (N//2))))
A = np.hstack((np.vstack((D,C)),np.vstack((E,B))))

print("матрица A\n",A,"\n\n")
"""#удаляем не четные столбцы и режем на отдельные элементы четный столбы"""
Ecut=E[:, 1::2].reshape(-1, 1)
"""#возвращает в виде [подходит][неподходит]"""
Ecut=np.where(Ecut < K )
"""#складывает каждый элемент из нечетной строки в несоколько эелементов затем в одно число"""
Bsum=np.sum(np.sum(B[0::2], axis=1))

if len(Ecut[0]) > Bsum:
   E = E.transpose()
   C = C.transpose()
   F = np.hstack((np.vstack((D,E)),np.vstack((C,B))))

else:
    F = np.hstack((np.vstack((D,B)),np.vstack((E,C))))

print("матрица F\n",F,"\n")

"""#если определитель матрицы А больше суммы диагональных элементов матрицы F, то вычисляется выражение: A*AT – K * FТ,"""
if all([np.linalg.det(A) > sum(np.fliplr(A).diagonal()+np.diagonal(A))]):
    G=np.dot(A,np.transpose(A))
    print("Результат выражения A*A^T\n",G,"\n")

    H=np.dot(K,np.transpose(F))
    print("Результат выражения K*H^T\n", H, "\n")

    Res=np.subtract(G, H)
    print("(Конец)Результат выражения (A*A^T)-(K*H^T)\n", Res, "\n")

else:
    print("Транспонированая матрица А \n",np.transpose(A),"\n\n")

    print(" матрица G^(-1) \n",np.tril(np.linalg.inv(A),0), "\n\n")

    print(" матрица F^(-1) \n",np.linalg.inv(F), "\n\n")

    G=np.add(np.transpose(A) ,   np.tril(np.linalg.inv(A),0).astype(int))
    H=np.linalg.inv(F)
    Res=np.dot(np.subtract(  G,   H),K)
    print("Конечный результат выражения (AT+G^(-1)-F^(-1))*K\n", Res, "\n\n")


plt.title("Зависимости: y =sin от элементов F, x = соs от элементов F")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.plot(np.cos(F),np.sin(F),linestyle="--",color="r")



plt.show()


plt.title("Высота столбца от числа элемента первой строки")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.bar(range(0,((N//2)*2)),F[0],color='r',alpha=0.9)

plt.show()

plt.title("соответсвие номера и квадрата элемента из первой строки ")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.plot(range(0,((N//2)*2)),F[0],linestyle="-",color="g")

plt.show()
