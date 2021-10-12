def find_fibo(n):
    if n <= 2:
        return 1
    fibo_x, fibo_next = 1,1

    i = 3
    while i <= n:
        i = i + 1
