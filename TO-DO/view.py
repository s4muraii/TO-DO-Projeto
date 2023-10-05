from controller import *
import os

sair = 0
while sair == 0:
    print("SOFTWARE TO-DO")
    print("01 -> ADICIONAR TAREFA")
    print("02 -> EXCLUIR TAREFA")
    print("03 -> LISTAR TAREFA")
    print("04 -> SAIR")

    menu = input("> ")
    os.system("cls")

    match menu:
        case "1":
            tarefa = input("Adicione uma tarefa: ")
            adicionarTarefa = ControllerAdicionarTarefa(tarefa)
            os.system("pause")
            os.system("cls")

        case "2":
            listarTarefa = ControllerListarTarefa()
            excluir = int(input("Qual o índice da tarefa deseja excluir? "))
            excluirTarefa = ControllerExcluirTarefa(excluir)
            os.system("pause")
            os.system("cls")

        case "3":
            print("Lista de Tarefas:")
            listarTarefa = ControllerListarTarefa()
            os.system("pause")
            os.system("cls")

        case "4":
            sair = 1

        case _:
            print("Opção inválida")