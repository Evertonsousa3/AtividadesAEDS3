class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class FilaPrioridade:
    def __init__(self):
        self.inicio = None
        self.final = None
        self._tamanho = 0

    def inserir(self, valor):

        '''
        Método de inserção regular na fila.
        :param valor:
        :return:
        '''

        novo_nodo = Node(valor)
        if self.inicio is None:
            self.inicio = novo_nodo
        else:
            self.final.proximo = novo_nodo
        self.final = novo_nodo
        self._tamanho += 1
        pass

    def inserir_prioridade(self):
        '''
        Método de inserção na fila com prioridade
        :return:
        '''

        pass

    def ler_inicio(self):
        nodo_inicio = self.inicio
        return nodo_inicio.valor

    def ler_final(self):
        nodo_final = self.final
        return nodo_final.valor

    def remover(self):
        if self.inicio is None:
            print("Não há nenhum elemento na fila, nenhuma operação foi realizada!")
            return

        nodo_inicio = self.inicio
        valor = nodo_inicio.valor
        self.inicio = nodo_inicio.proximo
        self._tamanho -= 1
        return valor
        pass

    def __iter__(self):
        nodo_inicio = self.inicio
        while nodo_inicio:
            yield nodo_inicio
            nodo_inicio = nodo_inicio.proximo
        pass

    def __len__(self):
        return self._tamanho
