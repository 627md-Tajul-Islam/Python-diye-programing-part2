def find_fibo(n):
    if n <= 2:
        return 1
    fibo_x, fibo_next = 1,1

    i = 3
    while i <= n:
        i = i + 1
        fibo_x, fibo_next = fibo_next, fibo_x + fibo_next

        return fibo_next

def list_fibo(n):
    fibo_list = [1,1]
    if n <= 2:
        return fibo_list[:n]

    fibo_x, fibo_next = fibo_next, fibo_x + fibo_next
    fibo_list.append(fibo_next)

    return fibo_list

for x in range(1,11):
    print(find_fibo(x))