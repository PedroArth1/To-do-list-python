lista_tarefas = []
def add():
    tarefa = input("Digite nova tarefa: ")
    lista_tarefas.append(tarefa)
    print(f'Tafera "{tarefa}" adicionada com sucesso!')
    print("\n")

def mostrar():
    print("Tarefas:")
    for items in range(len(lista_tarefas)):
        print(f"{items+1}. {lista_tarefas[items]}")
    print("\n")

def remover():
    tarefa_rem = int(input("Digite o número da tarefa a ser removida: "))
    lista_tarefas.pop(tarefa_rem-1)


def main():
    while True:
        print("Escolha uma opção")
        print("1. Mostrar Tarefas")
        print("2. Adicionar Tarefa")
        print("3. Remover Tarefa")
        print("4. Sair")
        opcao = int(input("Digite o número da opção desejada: "))

        if opcao == 1:
            mostrar()
        elif opcao == 2:
            add()
        elif opcao == 3:
            remover()
        elif opcao == 4:
            print("Até logo chapa quente...")
            break

main()