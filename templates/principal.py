from modelo.arquivo_entrada import ArquivoEntrada 
from jinja2 import Template
import statistics
import logging
import traceback



objeto_arquivo_entrada = ArquivoEntrada()
objeto_arquivo_entrada.preencher_arquivo_entrada()

try:

    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s [%(levelname)s] %(message)s',
                        handlers=[
                            logging.FileHandler('processo.log'),
                            logging.StreamHandler()
                        ])

    logging.info('Lendo o arquivo .csv e preenchendo os objetos')
    # Abrir o template
    with open('templates/template.html', 'r') as arquivo_template:
        arquivo_texto = arquivo_template.read()


    logging.info('Renderizando template... ')
    # Passar as variáveis necessárias para o template
    template = Template(arquivo_texto)

    # Calcular a média de preços por marca
    dicionario_media_preco_por_marca = {}
    marcas = set(produto.marca for produto in objeto_arquivo_entrada.produtos)
    for marca in marcas:
        precos = [
            float(produto.preco.replace('.', '').replace(',', '.'))
            for produto in objeto_arquivo_entrada.produtos
            if produto.marca == marca
        ]
        media = statistics.mean(precos)
        dicionario_media_preco_por_marca[marca] = f"R$ {media:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

    # Contexto para o template
    contexto = {
        'cabecalho': objeto_arquivo_entrada.cabecalho,
        'produtos': objeto_arquivo_entrada.produtos,
        'total_produtos': len(objeto_arquivo_entrada.produtos),
        'produto_mais_barato': min(objeto_arquivo_entrada.produtos, key=lambda x: float(x.preco.replace('.', '').replace(',', '.'))).preco,
        'produto_mais_caro': max(objeto_arquivo_entrada.produtos, key=lambda x: float(x.preco.replace('.', '').replace(',', '.'))).preco,
        'dicionario_media_preco_por_marca': dicionario_media_preco_por_marca
    }

    # Renderizando o template com o contexto
    renderizado = template.render(contexto)

    logging.info('Iniciando escrita do retatorio .html...')
    # Escrever o resultado no arquivo de saída
    with open('templates/relatorio_gerado.html', 'w') as arquivo_saida:
        arquivo_saida.write(renderizado)
    logging.info('Relatorio gerado com sucesso.')

except Exception as erro:
    logging.error(f'Ocorreu o seguinte erro: {erro}')
    logging.error(traceback.format_exc())