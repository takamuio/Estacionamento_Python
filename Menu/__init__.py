from Menu import Entrada
from Menu import Saida
from Menu import Consulta_Vaga
from Menu import Consulta_Geral
from time import sleep
import Interface


def principal():
    while True:
        Interface.cabecalho('MENU PRINCIPAL')
        resposta = Interface.menu(['Entrada', 'Saida', 'Consulta de vaga', 'Consulta geral', 'Sair'])
        if resposta == 1:
            Entrada.menu_principal()
        elif resposta == 2:
            Saida.menu_principal()
        elif resposta == 3:
            Consulta_Vaga.pesquisa()
        elif resposta == 4:
            Consulta_Geral.consulta()
        elif resposta == 5:
            break
        else:
            print(f'\033[0;31mErro ! Opção invalida.\033[m')
        sleep(1)
