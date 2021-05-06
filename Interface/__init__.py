import Validacoes


def linha(tamanho=30):
    return '-' * tamanho


def cabecalho(txt):
    print(linha())
    print(txt.center(30))
    print(linha())


def menu(lista):
    contador = 1
    for item in lista:
        print(f'[ {contador} ] - {item}')
        contador += 1
    print(linha())
    opcao = Validacoes.leia_int('Sua opção: ')
    return opcao
