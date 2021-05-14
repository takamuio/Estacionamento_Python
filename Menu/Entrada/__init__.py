from time import sleep
import Veiculos
from Veiculos import Carro
from Veiculos import Moto
from Veiculos import Onibus
import Interface


def menu_principal():
    Interface.cabecalho('ENTRADA')
    resposta = Interface.menu(['Carro', 'Moto', 'Onibus', 'Sair'])
    if resposta == 1:
        if Carro.quantidade < Carro.quantidade_maxima:
            Interface.cabecalho('CARRO')
            Veiculos.adicionar_veiculo()
            Carro.quantidade = 1
        else:
            print(f'\033[0;31mNão há vagas para carro !\033[m')
    elif resposta == 2:
        if Moto.quantidade < Moto.quantidade_maxima:
            Interface.cabecalho('MOTO')
            Veiculos.adicionar_veiculo()
            Moto.quantidade = 1
        else:
            print(f'\033[0;31mNão há vagas para moto !\033[m')
    elif resposta == 3:
        if Onibus.quantidade < Onibus.quantidade_maxima:
            Interface.cabecalho('ONIBUS')
            Veiculos.adicionar_veiculo()
            Onibus.quantidade = 1
        else:
            print(f'\033[0;31mNão há vagas para onibus !\033[m')
    elif resposta == 4:
        print('Voltando para o menu')
    else:
        print(f'\033[0;31mErro ! Opção invalida.\033[m')
    sleep(0.5)
