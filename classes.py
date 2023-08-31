class ToDoList:
    def __init__(self):
        self.tarefas = {}

    def adicionar_tarefa(self, descrição, indice):
        self.descrição = descrição
        self.tarefas[indice] = self.descrição
        print("Você adicionou uma nova tarefa!")

    def excluir_tarefa(self, indiceTarefa):
        self.indiceTarefa = indiceTarefa
        if indiceTarefa == self.tarefas.keys():
            for chave in self.tarefas.keys():
                self.tarefas[chave].pop()
                print("Tarefa excluída.")
            else:
                print("Tarefa não existe")

    def listar_tarefas(self):
        for x, y in self.tarefas.items():
            print(f"{y} - {x}")