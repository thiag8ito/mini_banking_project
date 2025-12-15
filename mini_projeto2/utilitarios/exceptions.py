class SaldoInsuficienteError(Exception):

    """"Exceção levantada quando uma operação de saque excede o saldo disponível"""
    #construtor da exceção
    def __init__(self, saldo_atual, valor_saque, mensagem="Saldo insuficiente para realizar o saque."):
        
        self.saldo_atual = saldo_atual  #saldo atual da conta no momento do erro
        self.valor_saque = valor_saque  #valor solicitado para o saque
        self.mensagem = f"{mensagem} Saldo atual: R${saldo_atual:.2f}, tentativa de saque: R${valor_saque:.2f}"     #mensagem detalhada de erro com saldo atual e valor do saque

        #Chama o construtor da classe Exception com a mensagem
        super().__init__(self.mensagem)

#define a exceção para operações em contas inexistentes
class ContaInexistenteError(Exception):

    """Exceção levantada ao tentar operar em uma conta que não existe"""

    #construtor da exceção
    def __init__(self, numero_conta, mensagem="A conta especificada não foi encontrada."):

        self.numero_conta = numero_conta    #numero da conta que não foi encontrada
        self.mensagem = f"{mensagem} Número da conta: {numero_conta}"   #mensagem detalhada de erro com o numero da conta
        super().__init__(self.mensagem)     #chama construtor da classe Exception com a msg