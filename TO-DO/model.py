from dao import *

class ToDo():
    def __init__(self, tarefa=str):
        self.tarefa = tarefa

    def AdicionarTarefa(self, tarefa, idtarefa, status):
        daoAdicionar = DaoAdicionarTarefa()
        return daoAdicionar.adicionar_tarefa(tarefa, idtarefa, status)
        
    def ListarTarefas(self):
        return DaoListarTarefa.listar()

    def RemoverTarefa(self, idexcluir):
        return DaoExcluirTarefa.excluir(idexcluir)
    
    def StatusTarefa(self, status):
        return DaoStatusTarefa.concluir(status)

TODO = ToDo()