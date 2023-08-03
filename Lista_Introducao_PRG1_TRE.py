#9.

from math import pi

raio = float(input("Digite o valor do raio da lata (em cm): "))

altura = float(input("Digite o valor da altura da lata (em cm): "))

volume = pi * raio ** 2 * altura

print(f"O volume da lata é de {volume:.2f} cm³")

#10. 

nota1 = float(input("Digite a primeira nota: "))

nota2 = float(input("Digite a segunda nota: "))

nota3 = float(input("Digite a terceira nota: "))

media = ((nota1 * 2) + (nota2 * 3) + (nota3 * 5)) / 10

print(f"A média final do aluno é {media:.2f}")

#11.

x1 = float(input("Digite a coordenada x do ponto P1: "))
y1 = float(input("Digite a coordenada y do ponto P1: "))

x2 = float(input("Digite a coordenada x do ponto P2: "))
y2 = float(input("Digite a coordenada y do ponto P2: "))

d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

print(f"A distância entre os pontos P1({x1},{y1}) e P2({x2},{y2}) é {d:.2f}")

#12. 

valora = input('Digite o valor de A: ')
valorb = input('Digite o valor de B: ')
valorc = input('Digite o valor de C: ')
valord = input('Digite o valor de D: ')
valore = input('Digite o valor de E: ')
valorf = input('Digite o valor de F: ')

valoraf = float(valora)
valorbf = float(valorb)
valorcf = float(valorc)
valordf = float(valord)
valoref = float(valore)
valorff = float(valorf)

x = (valorcf + valoref) - (valorbf + valorff) // (valoraf + valoref) - (valorbf + valordf)

y = (valoraf + valorff) - (valorcf + valordf) // (valoraf + valoref) - (valorbf + valordf)

print ('O valor de x é {} e o valor de y é {}'.format(x, y))

#13.

custo_fabrica = float(input("Digite o custo de fábrica do carro: "))

percentagem_distribuidor = 0.28
impostos = 0.45

custo_consumidor = custo_fabrica + (custo_fabrica * percentagem_distribuidor) + (custo_fabrica * impostos)

print(f"O custo ao consumidor do carro é de R$ {custo_consumidor:.2f}")


#14. 

idade_dias = int(input("Digite a idade em dias: "))

anos = idade_dias // 365
meses = (idade_dias % 365) // 30
dias_restantes = (idade_dias % 365) % 30

print(f"{anos} anos, {meses} meses e {dias_restantes} dias")

#15. 

segundos = int(input("Digite o tempo em segundos: "))

horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos_restantes = segundos % 60

print(f"{horas} horas, {minutos} minutos e {segundos_restantes} segundos")

#16.

salario_minimo = float(input("Digite o valor do salário mínimo: "))
valor_casa = 90 * salario_minimo
quantidade_casas = 1_000_000_000 // valor_casa
print("Com R$ 1.000.000.000,00 é possível construir", quantidade_casas, "casas populares.")




