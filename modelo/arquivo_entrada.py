from modelo.cabecalho import Cabecalho
from modelo.produto import Produto

class ArquivoEntrada:
    def __init__(self):
        self.cabecalho = None
        self.produtos = []

    def __str__(self):
        texto = f"{self.cabecalho}\n"
        for produto in self.produtos:
            texto += f"{produto}\n"
        return texto

    @staticmethod
    def ler_arquivo_entrada():
        arquivo_entrada = open('templates/arquivo-entrada-produtos.csv', 'r')
        linhas_do_arquivo = arquivo_entrada.readlines()
        arquivo_entrada.close()
        return linhas_do_arquivo

    def preencher_arquivo_entrada(self):
        linhas_do_arquivo = self.ler_arquivo_entrada()

        for linha in linhas_do_arquivo:
            linhas_separadas = linha.split(';')

            if linhas_separadas[0] == 'H':
                cabecalho = Cabecalho()
                cabecalho.preencher_objeto_cabecalho(linhas_separadas)
                self.cabecalho = cabecalho

            elif linhas_separadas[0] == 'P':
                produto = Produto()
                produto.preencher_objeto_produto(linhas_separadas)
                self.produtos.append(produto)
