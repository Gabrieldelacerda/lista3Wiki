def fibonnaci():
    fib_series = [0, 1]
    next_term = 1

    while next_term <= 500:
        fib_series.append(next_term)
        next_term = fib_series[-1] + fib_series[-2]

    return fib_series

fib_series = fibonnaci()
print("Série de Fibonnaci até que o valor seja maior que 500:")
print(fib_series)