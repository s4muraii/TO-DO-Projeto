class ToDo():

    def __init__(self):
        self.lista = []

    def AdicionarTarefa(self, tarefa):
        self.lista.append(tarefa)
        return True
    
    def RemoverTarefa(self, excluir):
        self.lista.pop(excluir)

    def ListarTarefas(self):
        return self.lista

TODO = ToDo()