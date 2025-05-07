class Cabecalho:
    def __init__(self):
        self.titulo = ""
        self.data = ""

    def __str__(self):
        return f"Cabecalho(titulo={self.titulo}, data={self.data})"

    def preencher_objeto_cabecalho(self, linhas_separadas):
        self.titulo = linhas_separadas[1]
        self.data = linhas_separadas[2] 