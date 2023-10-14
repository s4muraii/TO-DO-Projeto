class Dao:
    def __init__(self) -> None:
        self.arquivo="arquivo.txt"
        
    def AdicionarTarefa(self, tarefa):
        with open(self.arquivo, "a") as arquivo:
            arquivo.write(f"{tarefa}\n")
            return True
    
    def ListarTarefa(self):
        with open(self.arquivo, "r") as arquivo:
            ControllerList = arquivo.readlines()
            return ControllerList
        
    def ExcluirTarefa(self):
        pass
                
DAO = Dao()