#Tarefa: Escrava um programa que leia um número n inteiro qualquer
# e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.

termo = int(input('Quantos termos você gostaria de ver: '))
sequencia = [0,1]
indice = 0

if termo > 1:
    while len(sequencia) < termo:
        fibonacci = sequencia[-1] + sequencia[-2]

        sequencia.append(fibonacci)

    print(f'-'.join(map(str, sequencia)))
elif termo == 1:
    print(sequencia[0])

else:
    print('Opção invalida, digite um número inteiro maior que 0')
