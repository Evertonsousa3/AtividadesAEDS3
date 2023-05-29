class FilaPrioridade:
    def __init__(self):
        self.fila_prioridade = []

    def esta_vazia(self):
        return len(self.fila_prioridade) == 0

    def inserir(self, item, prioridade):
        elemento = (item, prioridade)
        if self.esta_vazia():
            self.fila_prioridade.append(elemento)
        else:
            inserido = False
            for i in range(len(self.fila_prioridade)):
                if self.fila_prioridade[i][1] > prioridade:
                    self.fila_prioridade.insert(i, elemento)
                    inserido = True
                    break
            if not inserido:
                self.fila_prioridade.append(elemento)

    def remover(self):
        if len(self.fila_prioridade) == 0:
            print("Fila vazia!")
            return None
        else:
            elemento = self.fila_prioridade[0]
            self.fila_prioridade.pop(0)
            return elemento

    def ler_inicio(self):
        return self.fila_prioridade[0]

    def ler_final(self):
        return self.fila_prioridade[len(self.fila_prioridade)-1]

    def __str__(self):
        return ' '.join([str(i) for i in self.fila_prioridade])

    def __len__(self):
        return len(self.fila_prioridade)


if __name__ == '__main__':
    filaprioriade = FilaPrioridade()
    filaprioriade.inserir("Pedro", 10)
    filaprioriade.inserir("João", 12)
    filaprioriade.inserir("Camila", 8)
    filaprioriade.inserir("Isabela", 15)
    print(filaprioriade)
    print(f'tamanho: {len(filaprioriade)}')
    filaprioriade.remover()
    print(filaprioriade)
    print(f'tamanho: {len(filaprioriade)}')
    filaprioriade.remover()
    print(filaprioriade)
    print(f'tamanho: {len(filaprioriade)}')
    filaprioriade.remover()
    filaprioriade.remover()
    filaprioriade.remover()
    print(f'tamanho: {len(filaprioriade)}')

