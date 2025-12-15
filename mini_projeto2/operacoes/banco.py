from entidades.cliente import Cliente
from entidades.conta import Conta, ContaCorrente, ContaPoupanca
from utilitarios.exceptions import ContaInexistenteError

class Banco:

    """
    Classe que gerencia asa operações do banco
    Demosntra Composição, pois "tem" clientes e contas
    """

    #construtos da classe Banco
    def __init__(self, nome: str):
        self.nome = nome
        self._clientes = {}     #dicionário de clientes (chave:CPF, valor: obj Cliente)
        self._contas = {}       #dicionario de contas (chave: num da conta, valor: obj Conta)

    """metodo para adicionar um novo cliente ao banco"""
    def adicionar_cliente(self, nome: str, cpf: str) -> Cliente:

        """cria e adiona um novo cliente ao banco"""
        #verifica se já existe cliente com o mesmo cpf
        if cpf in self._clientes:
            print("Erro: Cliente com CPF já cadastrado.")
            return self._clientes[cpf]
        
        #cria obj Cliente e adiciona ao dicionario
        novo_cliente = Cliente(nome, cpf)
        self._clientes[cpf] = novo_cliente

        print(f"Cliente {nome} adicionado com sucesso!")
        return novo_cliente
    
    """"metodo para criar uma conta para um cliente"""
    def criar_conta(self, cliente: Cliente, tipo: str) -> Conta:

        """cria uma nova conta para um cliente existente"""
        #numero da nova conta sera vaseado no total de contas + 1
        numero_conta = Conta.get_total_contas() + 1
        
        #cria conta corrente se o tipo informado for "corrente"
        if tipo.lower() == 'corrente':
            nova_conta = ContaCorrente(numero_conta, cliente)
        
        #cria conta poupança se o tipo informado for "poupanca"
        elif tipo.lower() == 'poupanca':
            nova_conta = ContaPoupanca(numero_conta, cliente)

        #caso o tipo nào seja válido
        else:
            print(f"Tipo de conta inválido. Escolhaa 'corrente' ou 'poucpanca'.")
            return None
        
        #adiciona a conta ao dicionario de contas
        self._contas[numero_conta] = nova_conta

        #associa a conta ao cliente
        cliente.adicionar_conta(nova_conta)
        print(f"Conta {tipo} No {numero_conta} criada para o cliente {cliente.nome}.")
        return nova_conta
    
    def buscar_conta(self, numero_conta: int) -> Conta:

        """Busca uma conta pelo seu numero"""
        #tenta recuperar a conta do dicionario
        conta = self._contas.get(numero_conta)

        #se não encontrar, lança exceção personalizada
        if not conta:
            raise ContaInexistenteError(numero_conta)
        return conta