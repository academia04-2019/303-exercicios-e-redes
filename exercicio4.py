num1 = int(input("digite o valor 1"))
num2 = int(input("digite o valor 2 "))

def somar(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    return num1 / num2

print('Soma:', somar(num1, num2))
print('Subtração:', subtrair(num1, num2))
print('Multiplicação:', multiplicar(num1, num2))
print('Divisão:', dividir(num1, num2))