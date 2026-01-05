# Tarefa: Cria um programa que laia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor ۹۹۹۰ que é a condição de parada.
# No final, mostra quantos números foram digitados a qual foi a soma entra alas (desconsiderando o flag).
soma = digitados = 0
numero = int(input('Digite um numero inteiro: [999 para parar]  '))

while numero != 999:
    numero = int(input('Digite um numero inteiro: [999 para parar]  '))
    soma += numero
    digitados += 1

print(f'Você digitou {digitados} números validos e a soma deles foram {soma}')
