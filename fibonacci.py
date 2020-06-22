A = [0,1]
max_f = int(input("Введите максимальное количество чисел Фибоначчи:"))
i = 2
while i <= max_f:
    A.append(A[i-1]+A[i-2])
    
    print (A[i])
    i+=1
