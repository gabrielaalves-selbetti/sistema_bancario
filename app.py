from operacoes.banco import Banco
from utils.exceptions import SaldoInsuficienteError, ContaInexistente

def menu_principal():
    print('-- Mini Sistema Bancário ---\n\n1. Adicionar Cliente\n2. Criar Conta\n3. Acessar Conta\n4.Sair\n')

    return input('Escolha uma opção: ')

def menu_conta(banco):
    try:
        num_conta = int(input("Digite o número da conta: "))

        conta = banco.buscar_conta(num_conta)

        while True: 
            print(f"\n--- Operações para Conta Nº {conta._numero} ---")
            print(f"Cliente: {conta._cliente.nome} | Saldo: R${conta.saldo:.2f}")
            print("1. Depositar")
            print("2. Sacar")
            print("3. Ver Extrato")
            print("4. Voltar ao Menu Principal")

            opcao = input('Escolha uma opção: ')

            if opcao == '1': 
                valor = float(input('Digite o valor para o depósito: '))
                conta.depositar(valor)
            elif opcao == '2':
                try:
                    valor = float(input('Digite o valor para saque: '))
                except SaldoInsuficienteError as e: 
                    print(f'Erro na operação: {e}')
            elif opcao == '3': 
                conta.extrato()
            elif opcao == '4':
                break
            else:
                print('Opção inválida, tente novamente.')

    except ContaInexistente as e:
        print(f'Erro: {e}')
     
    except ValueError: 
        print(f'Entrada inválida. Digite um número.')
    
def main(): 
    banco = Banco('MeuBanco.com')
    while True:
        opcao = menu_principal()

        if opcao == '1':
            
            # Adiciona um novo cliente
            nome = input("Digite o nome do cliente: ")
            cpf = input("Digite o CPF do cliente: ")
            banco.adicionar_cliente(nome, cpf)
        
        elif opcao == '2':
            
            # Cria uma nova conta vinculada a um cliente existente
            cpf = input("Digite o CPF do cliente para vincular a conta: ")
            cliente = banco._clientes.get(cpf)
            
            if cliente:

                tipo = input("Digite o tipo da conta (corrente/poupanca): ")
                banco.criar_conta(cliente, tipo)
            
            else:
                print("Cliente não encontrado. Cadastre o cliente primeiro.")

        elif opcao == '3':

            # Abre o menu de operações de uma conta
            menu_conta(banco)
            
        elif opcao == '4':

            # Encerra o programa
            print("\nObrigado por usar o nosso sistema. Até logo!\n")
            break
        
        else:

            print("\nOpção inválida. Por favor, tente novamente.\n")

# Ponto de entrada da aplicação
if __name__ == "__main__":
    main()

