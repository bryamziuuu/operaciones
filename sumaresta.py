input("Hola, bienvenido a la calculadora de Bryam")

print("Esta es la operacion summa")
n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))



def suma(n1, n2):
    return n1 + n2

print("La suma es: ", suma(n1, n2))


print("Esta es la operacion resta")

n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))

def resta(n1, n2):
    return n1 - n2  

print("La resta es: ", resta(n1, n2))