import Validacoes

vagas = []
detalhes_veiculos = {}
quantidade_maxima = 10


def adicionar_veiculo():
    detalhes_veiculos['modelo'] = Validacoes.leia_str('Modelo do veiculo: ')
    detalhes_veiculos['cor'] = Validacoes.leia_str('Cor do veiculo: ')
    detalhes_veiculos['placa'] = Validacoes.leia_str('Placa do veiculo: ')
    vagas.append(detalhes_veiculos)
    detalhes_veiculos.clear()
    print('Entrada concluida')
