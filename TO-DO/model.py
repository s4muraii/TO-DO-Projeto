from dao import *

class ToDo():
    def __init__(self, tarefa=str):
        self.tarefa = tarefa

    def AdicionarTarefa(self, tarefa, idtarefa, status):
        daoAdicionar = DaoAdicionarTarefa()
        return daoAdicionar.adicionar_tarefa(tarefa, idtarefa, status)
        
    def ListarTarefas(self):
        with open("tarefas.txt", "r") as arquivo:
            linhas = arquivo.readlines()
        return linhas
    
    def AtualizarTarefas(self, tarefas_lista):
        with open("tarefas.txt", "w") as arquivo:
            arquivo.writelines(tarefas_lista)

    def RemoverTarefa(self, idexcluir):
        return DaoExcluirTarefa.excluir(idexcluir)
    
    def StatusTarefa(self, status):
        return DaoStatusTarefa.concluir(status)

TODO = ToDo()