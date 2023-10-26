class Dao:
    def __init__(self):
        self.arquivo= "tarefas.txt"
        
class DaoAdicionarTarefa():
    
    def adicionar_tarefa(self, tarefa, idtarefa):
        with open("tarefas.txt", "a") as arquivo:
            arquivo.write(idtarefa)
            arquivo.write("\t")
            arquivo.write(tarefa)
            arquivo.write("\n")
        return True

class DaoExcluirTarefa():

    def excluir(excluir):
        with open("tarefas.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            linhas.pop(int(excluir) - 1)
            with open("tarefas.txt", "w") as arquivo:
                arquivo.writelines(linhas)
            return True
                    
class DaoListarTarefa():

    def listar():
        with open("tarefas.txt", "r") as arquivo:
            linhas = arquivo.readlines()
        return linhas