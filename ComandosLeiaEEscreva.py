# 1. Fazer um algoritmo para ler o valor do lado de um quadrado e mostrar sua área
#( lado2) e seu perímetro ( 4 x lado ).

lervalordoquadrado = input('Qual o valor? ')
lervalorfloat = float(lervalordoquadrado)

area = (lervalorfloat) ** 2 
perimetro = (lervalorfloat) * 4

print ('A área é {} e o perímetro é {}'.format(area, perimetro))

#2. Elaborar um algoritmo para ler o nome e a quantidade de filhos de uma pessoa.
#Mostrar a mensagem: “Fulano tem 5 filhos.”

nome = input('Qual o seu nome? ')
quantidadefilhos = input('Quantos filhos você tem? ')
print ('{} tem {} filhos'.format(nome, quantidadefilhos))

#3. Fazer um algoritmo para ler os valores da base e altura de um retângulo e mostrar
#seu perímetro ( 2 x ( base + altura ) ) e sua área ( base x altura ).

valorbase = input('Digite o valor da base: ')
valorbasefloat = float(valorbase)

valoraltura = input('Digite o valor da altura: ')
valoralturafloat = float(valoraltura)

perimetro = (valorbasefloat + valoralturafloat) * 2
area = valorbasefloat * valoralturafloat

print ('O retângulo tem {} de perímetro e {} de área'.format(perimetro, area))

#4. Fazer um algoritmo para ler o valor do lado de um cubo e
#mostrar sua área ( 6 x lado**2) e seu volume ( lado**3).

valorladocubo = input('Digite o lado do cubo: ')
valorladocubofloat = float(valorladocubo)

area = (valorladocubofloat ** 2) * 6
volume = valorladocubofloat ** 3

print('A área do cubo é de {}, e seu volume é de {}'.format(area, volume))

#5. Elaborar um algoritmo para ler dois números e mostrar o quociente e o resto da
#divisão inteira do primeiro pelo segundo número.

n1 = input('Digite um número: ')
n2 = input('Digite outro número: ')

n1float = float(n1)
n2float = float(n2)

print (n1float % n2float)

#6. Criar um algoritmo para ler a base e a altura de um triângulo e
#mostrar a sua área ( ( base x altura ) / 2 ).

basetriangulo = input('Digite a base do triângulo: ')
alturatriangulo = input('Digite a altura do triângulo: ')

basetriangulofloat = float(basetriangulo)
alturatriangulofloat = float(alturatriangulo)

area = (basetriangulofloat * alturatriangulofloat) / 2

print ('O valor da área do triângulo é de {}'.format(area))

#7. Construir um algoritmo para ler o raio de uma circunferência e mostrar o perímetro ( 2 x π x raio ) e a área ( π x raio2). Utilize o π como constante.

import math

valorraio = input('Digite o valor do raio: ')
valorraiofloat = float(valorraio)

perimetro = (math.pi * valorraiofloat) * 2
area = (math.pi * valorraiofloat**2)

print ('O perímetro é {} e a área é {}'.format(perimetro, area))


