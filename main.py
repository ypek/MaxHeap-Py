import os 
from implementMaxHeap import *

qtd_pessoas = []
tempo_preparo = []
nome_reserva = []
#(quantidade de pessoas [int], tempo de preparo [int], nome da reserva [str])

while True:
    os.system('color 6')
    print('''
    
    
      █▀▄▀█ █▀▀ █▀▀▄ █  █ 
      █ ▀ █ █▀▀ █  █ █  █ 
      ▀   ▀ ▀▀▀ ▀  ▀  ▀▀

    (1) Definir tamanho da fila com prioridades
    
    (2) Adicionar novo grupo na fila com prioridades

    (3) Mostrar próximo grupo aguardando

    ''')

    opcao = int(input('Digite a opção desejada: '))
    if opcao == 1:
        tamanho = input('Digite o tamanho da fila com prioridades: ')
        print('O tamanho da fila com prioridades foi definido para: ', tamanho)
        fila = MaxHeap(tamanho)
    elif opcao == 2:
        qtd_pessoas.append(input('Digite a quantidade de pessoas: '))
        tempo_preparo.append(input('Digite o tempo de preparo em hrs: '))
        nome_reserva.append(input('Digite o nome da reserva: '))
        try:
            fila.put(qtd_pessoas, tempo_preparo, nome_reserva)
        except:
            print('Fila lotada!')
        print('Grupo adicionado com sucesso!')
        print('Fila atual: ', fila)

    elif opcao == 3:
        fila.get()
        print('Próximo grupo aguardando: ', fila.peek())

        
    else:
        print('Opção inválida!')


    
