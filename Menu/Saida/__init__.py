from time import sleep
import Interface


def menu_principal():
    Interface.cabecalho('SAIDA')
    resposta = Interface.menu(['Carro', 'Moto', 'Onibus', 'Sair'])
    if resposta == 1:
        print()
    elif resposta == 2:
        print()
    elif resposta == 3:
        print()
    elif resposta == 4:
        print()
    else:
        print(f'\033[0;31mErro ! Opção invalida.\033[m')
    sleep(1)
