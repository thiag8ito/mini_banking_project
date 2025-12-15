class Cliente:

    # Método construtor que inicializa os atributos da classe
    def __init__(self, nome: str, cpf: str):
        self.nome = nome    #Atributo para armazernar o nome do cliente
        self.cpf = cpf      #Atributo para armazanar o CPF do cliente
        self.contas = []    #Lista vazia para armazenar as contas assosciadas ao cliente
    
    #Método para adicionar uma conta à lista de contas do cliente
    def adicionar_conta(self, conta):
        self.contas.append(conta)

    #Método especial que define a representação em string do objeto
    def __str__(self):
        return f"Cliente: {self.nome} (CPF: {self.cpf})"