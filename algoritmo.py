from classes import *
import os

def Main():
    contIndice = 0
    toDo = ToDoList()
    x = False
    while x == False:
        try:
            os.system("pause")
            os.system("cls")
            print("Esse é um software de lista de tarefas (TO-DO)")
            print("[1] CRIAR TAREFA\n[2] EXCLUIR TAREFA\n[3] LISTAR TAREFA")
            menu = int(input("> "))

            match menu:
                case 1:
                    os.system("cls")
                    print("CRIAR UMA TAREFA")
                    descrição = input("Forneça uma descrição para sua nova tarefa: ")
                    contIndice += 1
                    indice = contIndice
                    toDo.adicionar_tarefa(indice, descrição)

                case 2:
                    os.system("cls")
                    print("EXCLUIR TAREFAS")
                    print("Qual é o índice da tarefa que deseja excluir?")
                    indiceTarefa = int(input("> "))
                    toDo.excluir_tarefa(indiceTarefa)
                
                case 3:
                    os.system("cls")
                    print("LISTAR TAREFAS")
                    toDo.listar_tarefas()

                case _:
                    print("Opção não existe")

        except Exception as erro:
            print("Inválido")
            print(erro.__class__.__name__)