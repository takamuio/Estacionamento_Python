from Veiculos import Carro
import Veiculos


def leia_int(msg):
    while True:
        try:
            numero = int(input(msg))
        except (TypeError, ValueError):
            print(f'\033[0;31mErro ! Digite um valor inteiro valido.\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[0;31mErro ! Entrada de dados interrompido pelo usuario.\033[m')
            return 0
        else:
            return numero


def leia_str(msg):
    while True:
        try:
            texto = str(input(msg))
        except (TypeError, ValueError):
            print(f'\033[0;31mErro ! Digite um texto valido.\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[0;31mErro ! Entrada de dados interrompido pelo usuario.\033[m')
            return 0
        else:
            return texto
