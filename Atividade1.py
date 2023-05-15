class FilaDePrioridade(object):
    def __init__(self):
        self.filaPrioridade = []

    def __str__(self):
        return ' '.join([str(i) for i in self.filaPrioridade])

    # Função para checar se a fila está vazia
    def estaVazia(self):
        return len(self.filaPrioridade) == 0

    # Função para inserir na fila
    def inserir(self, data):
        self.filaPrioridade.append(data)

    # Função para exibir valor baseado na prioridade
    def deletar(self):
        try:
            valorMaximo = 0
            for i in range(len(self.filaPrioridade)):
                if self.filaPrioridade[i] > self.filaPrioridade[valorMaximo]:
                    valorMaximo = i
            item = self.filaPrioridade[valorMaximo]
            del self.filaPrioridade[valorMaximo]
            return item
        except IndexError:
            print("A fila está vazia.")
            exit()

    # Testes


if __name__ == '__main__':
    minhaFila = FilaDePrioridade()
    minhaFila.inserir(12)
    minhaFila.inserir(1)
    minhaFila.inserir(14)
    minhaFila.inserir(17)
    print(minhaFila)
    while not minhaFila.estaVazia():
        print(minhaFila.deletar())