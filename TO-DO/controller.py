from model import *
from dao import *
import random 

class ControllerAdicionarTarefa():
    def __init__(self, tarefa):
        self.tarefa = tarefa
        idtarefa = str(random.randint(1000, 9999))
        status = "A"

        try:
            if tarefa == "":
                print("Digite uma tarefa válida.")

            else:

                try:
                    if idtarefa not in TODO.ListarTarefas():
                        TODO.AdicionarTarefa(tarefa, idtarefa, status)
                        print("Tarefa adicionada.")

                    else:
                        print("Algum problema foi encontrado.")

                except Exception as erro:
                    print(f"Erro ao adicionar a tarefa: {erro}")

        except Exception as erro:
                print(f"Erro ao adicionar a tarefa: {erro}")

class ControllerExcluirTarefa():
    def __init__(self, idexcluir):
        self.idexcluir = idexcluir

        try:
            if idexcluir in TODO.ListarTarefas():
                TODO.RemoverTarefa(idexcluir)
                print("Tarefa removida.")
            else:
                print("Algum problema foi encontrado.")
                
        except Exception as erro:
            print(f"Erro ao excluir a tarefa: {erro}")
            print("Digite um número válido. Esta tarefa não existe.")

class ControllerListarTarefa():
    def __init__(self):
        ControllerLista = TODO.ListarTarefas()
        cont = 0
        for tarefas in ControllerLista:
            cont += 1
            tarefasCorrigidas = tarefas.split("\t", 2)
            tarefasFormatadas = tarefasCorrigidas[2][:-1]
            if cont >= 1:
                print(f"{cont}. {tarefasFormatadas}")

class ControllerStatusTarefa():
    def __init__(self):
        pass

class ControllerAlterarTarefa():
    def __init__(self):
        pass