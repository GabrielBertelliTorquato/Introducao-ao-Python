#1. Faça um Programa que mostre a mensagem "Alo mundo" na tela.

print ('Alo mundo')

#2. Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

PedirNumero = input ('Digite um número: ')
print ('O número informado foi {}'.format(PedirNumero))

#3. Faça um Programa que peça dois números e imprima a soma.

n1 = input ('Digite um número: ')
n2 = input ('Digite outro número: ')
soma = int(n1) + int(n2)
print ('O resultado é {}'.format(soma))

#4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.

n1 = input('Digite a sua nota em português: ')
n2 = input('Digite a sua nota em matemática: ')
n3 = input('Digite a sua nota em filosofia: ')
n4 = input('Digite a sua nota em sociologia: ')

n1float = float(n1)
n2float = float(n2)
n3float = float(n3)
n4float = float(n4)

CalculoMedia = (n1float + n2float + n3float + n4float) / 4

print ('A sua média é: {}'.format(CalculoMedia))

#5. Faça um Programa que converta metros para centímetros.

Metros = input('Digite a quantidade de metros: ')
MetrosInt = int(Metros)
Calculo = MetrosInt * 100

print ('{} centímetros'.format(Calculo))

#6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math

raio = float(input('Digite o valor do raio do círculo: '))

area = math.pi * raio ** 2

print(f'A área do círculo é {area:.2f}')

#7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado = input('Digite o lado do quadrado: ')
ladofloat = float(lado)
area = ladofloat ** 2
dobro_area = area * 2
print ('A área do quadrado é {} e o dobr0 desta área é {}'.format(area, dobro_area))

#8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#   calcule e mostre o total do seu salário no referido mês.

ganho_por_horas = input('Digite quantos você ganha por hora: ')
horas_trabalhadas = input('Digite quantas horas você trabalhou no mês: ')

ganho_por_horasfloat = float(ganho_por_horas)
horas_trabalhadasfloat = float(horas_trabalhadas)

calculo = (ganho_por_horasfloat) * horas_trabalhadasfloat

print ('Você recebeu {} reais neste mês'.format(calculo))

#9. Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus
#   Celsius.

Farenheit = input('Digite a temperatura em graus Farenheit: ')
FarenheitInt = int(Farenheit)
Calculo = round(5 * (FarenheitInt - 32) / 9)
print ('A temperatura em graus Celsius é: {}'.format(Calculo)) 

#10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.

celsius = input('Digite a temperatura em graus Celsius: ')
celsiusfloat = float(celsius)
converterfarenheit = round(celsiusfloat * 9/5 + 32)
print ('A temperatura em graus Farenheit é: {}'.format(converterfarenheit))

#11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#     a. o produto do dobro do primeiro com metade do segundo .
#     b. a soma do triplo do primeiro com o terceiro.
#     c. o terceiro elevado ao cubo.

n1 = input('Digite um número inteiro: ')
n2 = input('Digite outro número inteiro: ')
nreal = input('Digite um número real: ')

n1int = int(n1)
n2int = int(n2)
nreal = float(nreal)

produto = (n1int * 2) * (n2int / 2)
soma = (n1int * 3) + nreal
cubo = nreal ** 3

print ('O produto do dobro do primeiro com metade do segundo é: {}'.format(round(produto)))
print ('A soma do triplo do primeiro com o terceiro é: {}'.format(soma))
print ('O terceiro elevado ao cubo é: {}'.format(cubo))

#12. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
#    usando a seguinte fórmula: (72.7*altura) - 58

altura = input('Digite a sua altura: ')
alturafloat = float(altura)
pesoideal = (72.7 * alturafloat) - 58
print ('O seu peso ideal é: {:.5}'.format(pesoideal))

#15.  Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#     Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto
#     de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#     a. salário bruto.
#     b. quanto pagou ao INSS.
#     c. quanto pagou ao sindicato.
#     d. o salário líquido.
#     calcule os descontos e o salário líquido, conforme a tabela abaixo:

valor_hora = float(input("Digite o valor da hora trabalhada: "))
horas_mes = float(input("Digite o número de horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas_mes

ir = 0.11 * salario_bruto
inss = 0.08 * salario_bruto
sindicato = 0.05 * salario_bruto
descontos = ir + inss + sindicato

salario_liquido = salario_bruto - descontos

print("Salário Bruto: R$ {:.2f}".format(salario_bruto))
print("Descontos:")
print("  - IR (11%): R$ {:.2f}".format(ir))
print("  - INSS (8%): R$ {:.2f}".format(inss))
print("  - Sindicato (5%): R$ {:.2f}".format(sindicato))
print("Total de descontos: R$ {:.2f}".format(descontos))
print("Salário Líquido: R$ {:.2f}".format(salario_liquido))

#16.   Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área
#      a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é
#      vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem
#      compradas e o preço total.

import math

area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))
litros_necessarios = math.ceil(area / 3) 
latas_necessarias = math.ceil(litros_necessarios / 18)
preco_total = latas_necessarias * 80

print("Você precisará comprar", latas_necessarias, "latas de tinta")
print("O preço total é de R$ {:.2f}".format(preco_total))

#17

import math

area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

litros_necessarios = area / 6  
litros_necessarios_com_folga = litros_necessarios * 1.1  

latas_necessarias = math.ceil(litros_necessarios_com_folga / 18)

preco_latas = latas_necessarias * 80

galoes_necessarios = math.ceil(litros_necessarios_com_folga / 3.6)

preco_galoes = galoes_necessarios * 25

latas_necessarias_mix = int(litros_necessarios_com_folga / 18) 
litros_sobrando = litros_necessarios_com_folga % 18  
galoes_necessarios_mix = math.ceil(litros_sobrando / 3.6)  
preco_mix = (latas_necessarias_mix * 80) + (galoes_necessarios_mix * 25)  


print("Quantidade de tinta a ser comprada:")
print("- Apenas latas de 18 litros: {} latas, totalizando R$ {:.2f}".format(latas_necessarias, preco_latas))
print("- Apenas galões de 3,6 litros: {} galões, totalizando R$ {:.2f}".format(galoes_necessarios, preco_galoes))
print("- Mistura de latas e galões: {} latas e {} galões, totalizando R$ {:.2f}".format(latas_necessarias_mix, galoes_necessarios_mix, preco_mix))

#18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de
#    Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em
#    minutos).

tamanho_arquivo = float(input("Digite o tamanho do arquivo em MB: "))
velocidade_internet = float(input("Digite a velocidade do link de Internet em Mbps: "))

tamanho_arquivo_mb = tamanho_arquivo * 8

tempo_download_min = (tamanho_arquivo_mb / velocidade_internet) / 60

print("O tempo aproximado de download do arquivo é de {:.2f} minutos.".format(tempo_download_min))









