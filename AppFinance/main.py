from transaction import Transacao
from gerenciador import GerenciadorFinanceiro

def menu():
    print("\n=== APLICAÇÃO DE FINANÇAS PESSOAIS ===")
    print("1. Adicionar Receita")
    print("2. Adicionar Despesa")
    print("3. Listar Transações")
    print("4. Ver Saldo Atual")
    print("5. Listar Apenas Receitas")
    print("6. Listar Apenas Despesas")
    print("0. Sair")

def main():
    gerente = GerenciadorFinanceiro()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            valor = float(input("Valor da receita (Kz): "))
            desc = input("Descrição: ")
            gerente.adicionar_transacao(Transacao('receita', valor, desc))
            print("✅ Receita adicionada com sucesso.")
        
        elif opcao == '2':
            valor = float(input("Valor da despesa (Kz): "))
            desc = input("Descrição: ")
            gerente.adicionar_transacao(Transacao('despesa', valor, desc))
            print("✅ Despesa adicionada com sucesso.")

        elif opcao == '3':
            print("\n📋 LISTA DE TRANSAÇÕES:")
            gerente.listar_transacoes()

        elif opcao == '4':
            saldo = gerente.calcular_saldo()
            print(f"\n💰 Saldo atual: {saldo:.2f} Kz")

        elif opcao == '5':
            receitas = gerente.filtrar_por_tipo('receita')
            for r in receitas:
                print(f"{r.data} - {r.valor:.2f} Kz - {r.descricao}")

        elif opcao == '6':
            despesas = gerente.filtrar_por_tipo('despesa')
            for d in despesas:
                print(f"{d.data} - {d.valor:.2f} Kz - {d.descricao}")

        elif opcao == '0':
            print("👋 Até logo!")
            break

        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == '__main__':
    main()
