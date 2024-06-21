# Define a classe Nodo que representa um elemento da lista
class Nodo:
    def __init__(self, cor, numero):
        self.cor = cor   # Armazena a cor do cartão ('A' ou 'V')
        self.numero = numero  # Armazena o número do cartão
        self.proximo = None   # Ponteiro que inicialmente aponta para nenhum próximo nodo

# Define a classe ListaEncadeada que gerencia a lista de nodos
class ListaEncadeada:
    def __init__(self):
        self.head = None  # Ponteiro para o primeiro nodo da lista, inicialmente None

    # Função para inserir um nodo no final da lista (sem prioridade)
    def inserirSemPrioridade(self, nodo):
        if self.head is None:
            self.head = nodo  # O novo nodo se torna o primeiro nodo (head)
        else:
            atual = self.head  # Começa a partir do primeiro nodo
            while atual.proximo:  # Percorre a lista até o último nodo
                atual = atual.proximo
            atual.proximo = nodo  # Adiciona o novo nodo ao final da lista
    
    # Função para inserir um nodo com prioridade (ordem especial)
    def inserirComPrioridade(self, nodo):
        if self.head is None or self.head.cor == 'V':  # Se a lista estiver vazia ou o primeiro nodo for 'V'
            nodo.proximo = self.head   # O novo nodo aponta para o atual head
            self.head = nodo  # E se torna o novo head
            return
        
        atual = self.head  # Começa a partir do primeiro nodo
        anterior = None   # Inicializa o nodo anterior como None

        while atual and atual.cor == 'A':
            anterior = atual
            atual = atual.proximo

        nodo.proximo = atual  # O novo nodo aponta para o nodo atual
        if anterior:
            anterior.proximo = nodo  # O nodo anterior aponta para o novo nodo
        else:
            self.head = nodo  # Se não houver nodo anterior, o novo nodo se torna o head
    
    # Função para inserir um nodo baseado na cor e no número fornecidos pelo usuário
    def inserir(self):
        cor = input('Informe a cor do cartão (A/V): ').upper()  
        numero = int(input('Informe o número do cartão: '))
        novo_nodo = Nodo(cor, numero)  # Cria um novo nodo com os valores fornecidos

        if self.head is None:
            self.head = novo_nodo  # O novo nodo se torna o head
        elif cor == 'V':
            self.inserirSemPrioridade(novo_nodo)
        elif cor == 'A':
            self.inserirComPrioridade(novo_nodo)
    
    # Função para imprimir todos os nodos da lista de espera
    def imprimirListaEspera(self):
        atual = self.head  # Começa a partir do primeiro nodo
        if not atual:
            print('A lista está vazia.')
            return
        
        lista_nodos = []  # Inicializa uma lista para armazenar os nodos
        while atual: # Percorre a lista
            lista_nodos.append(f'[{atual.cor}, {atual.numero}]')  # Adiciona a representação do nodo à lista
            atual = atual.proximo   # Vai para o próximo nodo

        print(f'Lista de espera ->', ' '.join(lista_nodos))
    
    # Função para atender o primeiro paciente da fila
    def atenderPaciente(self):
        if self.head is None:                    # Se a lista estiver vazia
            print('Não há pacientes na fila.')   
            return
        
        paciente_atendido = self.head   # Armazena o primeiro nodo
        self.head = self.head.proximo   # Atualiza o head para o próximo nodo
        print(f'Atendendo o paciente cartão cor {paciente_atendido.cor} e número {paciente_atendido.numero}.')
        # Informa que o paciente está sendo atendido

# Função para exibir um menu e realizar operações na lista
def menu():
    lista = ListaEncadeada()
    while True:
        opcao = input('\nEscolha uma das opções:'
                  '\n1 - Adicionar paciente'
                  '\n2 - Mostrar pacientes na fila'
                  '\n3 - Chamar paciente'
                  '\n4 - Sair'
                  '\n>> ')
        
        if opcao == '1':
            lista.inserir()
            continue
        elif opcao == '2':
            lista.imprimirListaEspera()
            continue
        elif opcao == '3':
            lista.atenderPaciente()
            continue
        elif opcao == '4':
            print('Encerrando programa.')
            break 
        else:
            print('Opção inválida. Tente novamente.')
            continue

# Chamando a função menu para iniciar o programa
menu()
