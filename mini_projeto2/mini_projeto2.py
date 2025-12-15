from operacoes.banco import Banco
from utilitarios.exceptions import SaldoInsuficienteError, ContaInexistenteError

def menu_principal():
    print("\n--- Mini-Projeto 2 - Sistema Bancário Digital ---\n")
    print("1. Adicionar Cliente")
    print("2. Criar Conta")
    print("3. Acessar Conta")
    print("4. Sair\n")

    #Retornar a opção digitada pelo usuário
    return input("Escolha uma opação: ")

#função que exibe o menu de operações deuma conta específica
def menu_conta(banco):
    try:
        #solicita ao usuário o número da conta
        num_conta = int(input("Digite o número da conta: "))

        #busca a conta no banco; pode gerar a exceção se não existir
        conta = banco.buscar_conta(num_conta)

        #loop de operações dentro da conta
        while True:
            print(f"\n--- Operações para Conta No {conta._numero} ---")
            print(f"Cliente: {conta._cliente.nome} | Saldo: R${conta.saldo:.2f}")
            print(f"1. Depositar")
            print(f"2. Sacar")
            print(f"3. Ver Extrato")
            print(f"4. Voltar ao Menu Principal")

            opcao = input("Escolha uma opção: ")

            if opcao == '1':

                #deposita valor na conta
                valor = float(input("Digite o valor para depósito: "))
                conta.depositar(valor)

            elif opcao == '2':

                #tenta realizar um saque
                try:

                    valor = float(input("Digite o valor para saque: "))
                    conta.sacar(valor) #polimorfismo: depende do tipo de conta

                except SaldoInsuficienteError as e:
                    print(f"Erro na operação: {e}")

            elif opcao == '3':

                #exibe o extrato da conta  
                conta.extrato()

            elif opcao == '4':
                
                #sai do menu da conta e retorna para o menu principal
                break

            else:
                print("Opção inválida. Tente novamente.")

    #exceção cas o a conta não exista
    except ContaInexistenteError as e:
        print(f"Erro: {e}")

    #exceção para entradas inválidas (Não numeros)
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um número.")

#função principal que controla o fluxo do sistema
def main():

    #cria o objeto Banco
    banco = Banco("Banco Digital DSA")

    #loop principal do sistema
    while True:

        opcao = menu_principal()

        if opcao == '1':

            #adiciona um novo cliente
            nome = input("Digite o nome do cliente: ")
            cpf = input("Digite o CPF do cliente: ")
            banco.adicionar_cliente(nome, cpf)

        elif opcao == '2':

            #cria uma nova conta vinculada a um cliente existente
            cpf = input("Digite o CPF do cliente para vincular a conta: ")
            cliente = banco._clientes.get(cpf)

            if cliente:
                tipo = input("Digite o tipo da conta (corrente/poupança): ")
                banco.criar_conta(cliente, tipo)

            else:
                print("Cliente não encontrado. Cadastre o cliente primeiro")
        
        elif opcao == '3':

            #abre o menu de operações de uma conta
            menu_conta(banco)
        
        elif opcao == '4':

            #encerra o programa
            print(f"\nObrigado por usar o nosso sistema. Até logo!")
            break
            
        else:
            print("\nOpção inválida. Por favor, tente novamente. \n")

if __name__ == "__main__":
    main()