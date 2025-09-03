
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error, división por cero"
    return a / b

print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

op = int(input("Elige una opción (1-4): "))
a = float(input("Número 1: "))
b = float(input("Número 2: "))

if op == 1:
    print("Resultado:", suma(a, b))
elif op == 2:
    print("Resultado:", resta(a, b))
elif op == 3:
    print("Resultado:", multiplicacion(a, b))
elif op == 4:
    print("Resultado:", division(a, b))
else:   
    print("Opción no válida")