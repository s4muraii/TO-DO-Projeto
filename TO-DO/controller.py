from model import *
from dao import *

class ControllerAdicionarTarefa():
    def __init__(self, tarefa):
        try:
            if tarefa == "":
                print("Digite uma tarefa válida.")
            else:
                try:
                    self.tarefa = tarefa
                    if DAO.AdicionarTarefa(self.tarefa) == True:
                        print("Tarefa adicionada.")
                    else:
                        print("Algum problema foi encontrado, tente novamente.")

                except Exception as erro:
                    print(f"Erro ao adicionar a tarefa: {erro}")

        except Exception as erro:
                print(f"Erro ao adicionar a tarefa: {erro}")

class ControllerExcluirTarefa():
    def __init__(self, excluir):
        self.excluir = excluir
        
        try:
            self.excluir_convert = self.excluir
            self.excluir_convert = int(self.excluir)
            self.excluir_convert -= 1
            
            DAO.RemoverTarefa(self.excluir) == True
            print("Tarefa removida.")
            
        except Exception as erro:
                print("Digite um número válido. Esta tarefa não existe.")
                

class ControllerListarTarefa():
    
    def __init__(self):
        ControllerLista = DAO.ListarTarefa()
        cont = 0

        for tarefas in range(len(ControllerLista)):
            cont += 1
            print(f"{cont}. {ControllerLista[tarefas]}")