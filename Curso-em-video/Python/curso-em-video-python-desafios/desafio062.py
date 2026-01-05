# Tarefa: Melhora o DESAFIO 061. Perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar O termos.


print('Gerador de PA')
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
progressao = 1
total = 10
mais = 0

while True:
    print('==-' * 20)
    while progressao <= total:

            print(f'{termo}', end='-')
            termo += razao
            progressao += 1
    print('PAUSA')
    print('==-' * 20)
    print('\nSE não quiser mais termos, é só digitar 0(zero)')
    mais = int(input('Quer quantos mais termo? \n'))
    if mais == 0:
        break
    total += mais
print('==-'*20)
print(f'Progressão finalizada com {progressao - 1} termos exibidos.')
print('==-'*20)
