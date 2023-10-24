from model import *
import os
import random

class ControllerAdicionarTarefa():
    def __init__(self, tarefa):

        try:
            if tarefa == "":
                print("Digite uma tarefa válida.")
            else:
                try:
                    self.tarefa = tarefa
                    if TODO.AdicionarTarefa(self.tarefa) == True:
                        print("Tarefa adicionada.")
                    else:
                        print("Algum problema foi encontrado.")

                except Exception as erro:
                    print("Erro ao adicionar a tarefa: {erro}")

        except Exception as erro:
                print("Erro ao adicionar a tarefa: {erro}")

class ControllerExcluirTarefa():
    def __init__(self, excluir):
        self.excluir = excluir
        try:
            if TODO.RemoverTarefa(self.excluir) == True and self.excluir >= "0":
                print("Tarefa removida.")
            else:
                print("Algum problema foi encontrado.")

        except Exception as erro:
                print("Digite um número válido. Esta tarefa não existe.")

class ControllerListarTarefa():
    def __init__(self):
        ControllerLista = TODO.ListarTarefas()
        
        cont = -1

        for tarefas in ControllerLista:
            cont += 1
            print(f"{cont}. {tarefas}")