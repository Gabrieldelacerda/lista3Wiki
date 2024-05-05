numero = int(input("Fatorial de: "))

fatorial = 1

fatorial_str = ""

for i in range(numero, 0, -1):
    fatorial *= i
    fatorial_str += str(i)
    if i != 1:
        fatorial_str += " . "

print(f"{numero}! = {fatorial_str} = {fatorial}")