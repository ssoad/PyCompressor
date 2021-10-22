class PriorityQueue: 
    __heap = None
    __relation = None
    __size = None

    def __init__(self, predicate):
        self.__heap = []
        self.__relation = predicate #lambda parent, child: True if self.__heap[parent] <= self.__heap[child] else False
        self.__size = 0

    def length(self):
        return self.__size
        
    def put(self, element):
        self.__heap.append(element)
        self.__size = self.__size + 1
        self.heap_up(self.__size - 1)

    def delete(self):
        try:
            if self.__size == 0:
                raise EmptyHeap
            self.swap(0, self.__size - 1)

            element = self.__heap[self.__size - 1]
            
            self.__size = self.__size - 1
            del self.__heap[self.__size]
            self.heap_down()

            return element
        except EmptyHeap as err:
            print(err.message)
            return None

    def swap(self, index1, index2):
        tmp = self.__heap[index1]
        self.__heap[index1] = self.__heap[index2]
        self.__heap[index2] = tmp

    def heap_up(self, index):
        index = int(index)
        parent = (index - 1) / 2
        while(index > 0):
            parent = int((index - 1) / 2)
            relation_result = self.__relation(self.__heap[parent], self.__heap[index])

            if relation_result:
                return
            else:
                self.swap(parent, index)
            index = int((index - 1) / 2)

    def heap_down(self):
        parent = 0
        child = 2 * parent + 1
        size = self.__size

        while child < size:
            if child + 1 < size and self.__heap[child + 1] < self.__heap[child]:
                child = child + 1
            if self.__relation(self.__heap[parent], self.__heap[child]):
                return
            else:
                self.swap(parent, child)
                parent = child
                child = 2 * child + 1
    
    #@deprecated
    def show_queue(self):
        for element in self.__heap:
            print("(" + element.sign + ", " + str(element.frequency) + ")")

class EmptyHeap(Exception):
    message = "No element in PriorityQueue"