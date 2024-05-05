def fibonnaci(n):
    fibonacci_series = [1, 1]
    for i in range(2, n):
        next_term = fibonacci_series[-1]  + fibonacci_series[-2]
        fibonacci_series.append(next_term)
    return fibonacci_series

n = int(input("Digite o valor de n para gerar a série de Fibonnaci: "))
fib_series = fibonnaci(n)
print("Série de Fibonnaci até o {} termo:".format(n))
print(fib_series)