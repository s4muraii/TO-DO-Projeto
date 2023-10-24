from controller import *
from dao import *
import os
import random

sair = 0
while sair == 0:

    os.system("cls")
    print("SOFTWARE DE TO-DO \n1 - Adicionar tarefa \n2 - Listar tarefas \n3 - Remover tarefa \n4 - Sair")
    opcao = input("Digite a opção desejada > ")

    match opcao:
        case "1":
            os.system("cls")
            tarefa = input("Digite a tarefa > ")
            adicionarTarefa = ControllerAdicionarTarefa(tarefa)
            adicionarTarefa = DaoAdicionarTarefa(tarefa, idtarefa = str(random.randint(1000, 9999)))
            os.system("pause")

        case "2":
            os.system("cls")
            print("Estes são os itens presentes na lista de tarefas: ")
            listarTarefa = ControllerListarTarefa()
            print("\n")
            print("Estes são os itens presentes no DAO: ")
            listarTarefa = DaoListarTarefa()
            os.system("pause")

        case "3":
            os.system("cls")
            listarTarefa = ControllerListarTarefa()
            excluir = input("Digite o número da tarefa que deseja excluir > ")
            excluirTarefa = ControllerExcluirTarefa(excluir)
            excluirTarefa = DaoExcluirTarefa(excluir)
            os.system("pause")

        case "4":
            os.system("cls")
            sair = 1

        case _:
            os.system("cls")
            print("Opção inválida")