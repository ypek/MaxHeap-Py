# Classe modificada para permitir a indicação de quantidade de itens permitidos
# na Heap

# Foram definidos metodos e variaveis privadas (private)

class MaxHeap:
    def __init__(self, max_size=None):
        self.__heap = [0]
        self.__max_size = None
        if max_size is not None and isinstance(max_size, int):
            if max_size <= 0:
                raise ValueError("max_size precisa ser maior que zero.")
            self.__max_size = max_size

    def is_empty(self): ## retorna True se estrutura esta vazia
        if len(self.__heap) - 1 == 0:
            return True
        return False

    def is_full(self):
        if self.__max_size is not None:
            if len(self.__heap) - 1 == self.__max_size:
                return True
        return False

    def put(self, item):
        if not self.is_full():
            self.__heap.append(item)
            self.__floatUp(len(self.__heap) - 1)
        else:
            raise Exception("Heap Lotada!")

    def get(self):
        if len(self.__heap) > 2:
            self.__swap(1, len(self.__heap) - 1)
            max = self.__heap.pop()
            self.__bubbleDown(1)
        elif len(self.__heap) == 2:
            max = self.__heap.pop()
        else:
            max = False
        return max

    def peek(self):
        if self.__heap[1]:
            return self.__heap[1]
        return False

    def __swap(self, i, j):
        self.__heap[i], self.__heap[j] = self.__heap[j], self.__heap[i]

    def __floatUp(self, index):
        parent = index//2
        if index <= 1: # nao faz nada se for raiz
            return
        elif self.__heap[index] > self.__heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)

    def __bubbleDown(self, index):
        left = index * 2
        right = index * 2 + 1
        maior = index
        if len(self.__heap) > left and self.__heap[maior] < self.__heap[left]:
            maior = left
        if len(self.__heap) > right and self.__heap[maior] < self.__heap[right]:
            maior = right

        if maior != index:
            self.__swap(index, maior)
            self.__bubbleDown(maior)

## TESTES ##
if __name__ == '__main__':     ## teste para que ao importar esse arquivo nao considere esse trecho                   
    h = MaxHeap(4)
    h.put(45)
    h.put(55)
    h.put(33)

    print(h.get())
    print(h.get())
    print(h.get())
