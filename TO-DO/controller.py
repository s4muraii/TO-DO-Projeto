from model import *

class ControllerAdicionarTarefa():
    def __init__(self, tarefa):
        self.tarefa = tarefa

        try:
            if self.tarefa == " ":
                print("Informe uma tarefa válida")
        
            else:

                try:
                    if TODO.AdicionarTarefa(self.tarefa) == True:
                        print("Tarefa adicionada.")

                    else:
                        print("Algum problema foi encontrado ao adicionar a tarefa.")

                except Exception as erro:
                    print(f"Erro ao adicionar tarefa: {erro}")

        except Exception as erro:
            print(f"Erro ao adicionar tarefa: {erro}")

class ControllerExcluirTarefa():
    def __init__(self, excluir):
        self.excluir = excluir - 1

        try:
            if self.excluir in self.lista:
                TODO.RemoverTarefa(self.excluir)
                print("Tarefa excluída.")
            
            if self.excluir not in self.lista:
                print("O índice da tarefa não existe.")

            else:
                print("Algum problema foi encontrado ao tentar excluir a tarefa.")
        
        except Exception as erro:
            print(f"Erro ao excluir tarefa: {erro}")



class ControllerListarTarefa():
    def __init__(self):

        try:
            ControllerLista = TODO.ListarTarefas()
            cont = 0

            for tarefas in ControllerLista:
                cont += 1
                print(f"{cont}. {tarefas}")
        
        except Exception as erro:
            print(f"Erro ao listar tarefas: {erro}")