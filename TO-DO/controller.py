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
            tarefas_lista = TODO.ListarTarefas()
            
            cont = 0
            for tarefa in tarefas_lista:
                cont += 1
                tarefas_corrigidas = tarefa.split("\t", 2)
                
                if len(tarefas_corrigidas) > 2:
                    tarefas_formatadas = tarefas_corrigidas[2][:-1]
                    
                    if cont >= 1:
                        print(f"{cont}. {tarefas_formatadas}")

class ControllerAlterarTarefa(ControllerListarTarefa):
    def __init__(self):
        super().__init__()  # chama a: ControllerListarTarefa.__init__(self)
        self.dao_alterar_tarefa = DaoAlterarTarefa()
        self.controller_todo = ToDo()

    def alterar_tarefa(self, indice, nova_descricao):
        tarefas_lista = self.ListarTarefas()

        if 1 <= indice <= len(tarefas_lista):
            tarefa = tarefas_lista[indice - 1]

            tarefas_corrigidas = tarefa.split("\t", 2)

            tarefas_corrigidas[2] = nova_descricao + "\n"

            tarefa_alterada = "\t".join(tarefas_corrigidas)

            tarefas_lista[indice - 1] = tarefa_alterada

            self.AtualizarTarefas(tarefas_lista)

            print(f"Tarefa {indice} alterada com sucesso.")

class ControllerStatusTarefa():
    def __init__(self):
        pass

class ControllerConcluirTarefa():
    def __init__(self):
        pass