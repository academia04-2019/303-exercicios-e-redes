qtd_notas = int(input("Digite o número de notas"))

soma = 0

for i in range(qtd_notas):
    soma += int(input("Digite a nota"))

print(soma/qtd_notas)

lista = []

for index in range(qtd_notas):
    lista.append(int(input("digite o valor")))
for i in range(qtd_notas):
    soma += lista[i]

print(soma/qtd_notas)