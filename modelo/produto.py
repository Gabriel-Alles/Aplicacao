class Produto:

    def __init__(self):
        self.identificador = None
        self.nome = None
        self.marca = None
        self.tamanho_tela = None
        self.cor = None
        self.processador = None
        self.memoria_ram = None
        self.memoria_interna = None
        self.preco = None
        self.data_lancamento = None
        self.url_imagem = None

    def __str__(self):
        return (
            f"Produto("
            f"id={self.identificador}, nome={self.nome}, marca={self.marca}, "
            f"tela={self.tamanho_tela}, cor={self.cor}, processador={self.processador}, "
            f"RAM={self.memoria_ram}, armazenamento={self.memoria_interna}, "
            f"preço={self.preco}, lançamento={self.data_lancamento}, imagem={self.url_imagem})"
        )


    def preencher_objeto_produto(self, linhas_separadas):
        self.nome = linhas_separadas[1]
        self.marca = linhas_separadas[2]
        self.tamanho_tela = linhas_separadas[3]
        self.cor = linhas_separadas[4]
        self.processador = linhas_separadas[5]
        self.memoria_ram = linhas_separadas[6]
        self.memoria_interna = linhas_separadas[7]
        self.preco = linhas_separadas[8]
        self.data_lancamento = linhas_separadas[9]
        self.url_imagem = linhas_separadas[10]