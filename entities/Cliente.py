class Cliente:
    # método construtor para inicializar os atributos da classe
    def __init__(self, nome: str, cpf: str):
        self.nome = nome
        self.cpf = cpf
        self.contas = []

    def adicionar_conta(self, conta): 
        self.contas.append(conta)

    # define a representação em string do objeto 
    def __str__(self):
        return f'Cliente: {self.nome} (CPF: {self.cpf})'