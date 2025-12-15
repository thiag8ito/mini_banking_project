from abc import ABC, abstractmethod
from datetime import datetime
from utilitarios.exceptions import SaldoInsuficienteError

class Conta(ABC):
    """
    Classe base abstrata para contas bancárias.
    Demonstra Herança e Encapsulamento.
    """

    _total_contas = 0   #Atributo de classe que calcula quantas contas foram criadas

    def __init__(self, numero: int, cliente):
        self._numero = numero       #numero da conta
        self._saldo = 0.0           #saldo da conta, inicializado em 0
        self._cliente = cliente     #referencia ao cliente dono da conta
        self._historico = []        #lista para armazenar historico da conta
        Conta._total_contas += 1    #incrementa total de contas

    """propriedade para acessar o saldo de forma controlada"""
    @property
    def saldo(self):
        
        #getter para o saldo, permitindo acesso controlado
        return self._saldo
    
    """método de lcasse para consultar o numero total de contas"""
    @classmethod
    def get_total_contas(cls):

        #Metodo de classe para obter o numero total de contas criadas
        return cls._total_contas
    
    """metodo para realizar depósitos"""
    def depositar(self, valor: float):

        #adiciona um valor ao saldo da conta
        if valor > 0:

            #incrementa o saldo
            self._saldo += valor

            #registra a transação no histórico com data e hora
            self._historico.append((datetime.now(), f"Depósito de R${valor:.2f}"))
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")

        else:
            print("Valor de depósito inválido.")

    """método abstrato que deve ser implementado pelas subclasses"""
    @abstractmethod
    def sacar(self, valor: float):

        #método abstrato para sacar um valor

        pass

    """método para exibir o extra da conta"""
    def extrato(self):
        print(f"\n--- Extrato da Conta No. {self._numero} ---")
        print(f"Cliente: {self._cliente.nome}")
        print(f"Saldo atual: R${self._saldo:.2f}")
        print("Histórico de transações: ")
        
        #caso não haja histórico
        if not self._historico:
            print("Nenhuma transação registrada.")
        
        #percorre o histórico e exibe cada transação
        for data, trasacao in self._historico:
            print(f"- {data.strftime('%d/%m/%y %H:%M:%S')}: {trasacao}")
        print("--------------------------------------\n")

"""define a subclasse ContaCorrente"""
class ContaCorrente(Conta):

    #Subclasse que representa uma cc
    #demonstra Polimorfismo ao sobrescrever o método sacar

    #construtor com limite padrao de cheque especial
    def __init__(self, numero: int, cliente, limite: float = 500.0):
        
        #chama o construtor da classe base
        super().__init__(numero, cliente)

        #define o limite de cheque especial
        self.limite = limite

    """implementação do método sacar com o cheque especial"""
    def sacar(self, valor: float):

        #permite saque utilizando o saldo da conta mais o limite (cheque especial)
        if valor <= 0:
            print("Valor de saque inválido.")
            return

        #calcula o saldo disponível
        salvo_disponivel = self.saldo + self.limite

        #caso o valor do saque ultrapasse o saldo disponivel
        if valor > salvo_disponivel:
            raise SaldoInsuficienteError(salvo_disponivel, valor, "Saldo e limite insuficiente.")
        
        #deduz o valor do saque do saldo
        self._saldo -= valor

        #registra a transação no histórico
        self._historico.append((datetime.now(), f"Saque de R${valor:.2}"))
        print(f"Saque de R${valor:.2f} realizado com sucesso.")

"""define a subclasse ContaPoupança"""
class ContaPoupanca(Conta):

    #subclasse que representa uma conta poupança
    def __init__(self, numero: int, cliente):
        super().__init__(numero, cliente)

    #implementação do metodo sacar apenas com o saldo disponivel
    def sacar(self, valor: float):

        #permite saque apenas se houver saldo suficiente
        if valor <= 0:
            print("Valor de saque inválido.")
            return
        
        #verifica se há saldo suficiente
        if valor > self.saldo:
            raise SaldoInsuficienteError(self._saldo, valor)
        
        #deduz o valor do saldo
        self._saldo -= valor

        #regista a transação no histórico
        self._historico.append((datetime.now(), f"Saque de R${valor:.2f}"))
        print(f"Saque de R${valor:.2} realizado com sucesso.")