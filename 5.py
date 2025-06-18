#santiaogo
test_results = []  # Crea una lista vacía para guardar los resultados de las pruebas

def record_test(test_name, condition):  # Define una función para registrar el resultado de una prueba
    emoji = "✅" if condition else "❌"  # Usa un emoji según si la condición es verdadera o falsa
    test_results.append(f"{emoji} {test_name}")  # Agrega el resultado formateado a la lista de resultados

class MaxHeap:  # Define la clase MaxHeap
    def __init__(self):  # Método constructor de la clase
        self.heap = []  # Inicializa el heap como una lista vacía
    
    def insert(self, value):  # Método para insertar un valor en el heap
        self.heap.append(value)  # Agrega el valor al final de la lista
        self._heapify_up(len(self.heap) - 1)  # Restaura la propiedad de heap subiendo el valor
    
    def delete_max(self):  # Método para eliminar el valor máximo del heap
        if not self.heap:  # Si el heap está vacío
            return None  # Retorna None
        max_val = self.heap[0]  # Guarda el valor máximo (raíz)
        last = self.heap.pop()  # Elimina el último elemento del heap
        if self.heap:  # Si el heap no está vacío después de eliminar
            self.heap[0] = last  # Coloca el último elemento en la raíz
            self._heapify_down(0)  # Restaura la propiedad de heap bajando el valor
        return max_val  # Retorna el valor máximo eliminado
    
    def build_heap(self, array):  # Método para construir un heap desde un arreglo
        self.heap = array[:]  # Copia el arreglo recibido a self.heap
        n = len(self.heap)  # Obtiene el tamaño del heap
        for i in range(n // 2 - 1, -1, -1):  # Recorre desde la mitad hacia el inicio
            self._heapify_down(i)  # Aplica heapify_down en cada nodo
    
    def _heapify_up(self, index):  # Método privado para subir un elemento
        while index > 0:  # Mientras no sea la raíz
            parent = (index - 1) // 2  # Calcula el índice del padre
            if self.heap[index] > self.heap[parent]:  # Si el hijo es mayor que el padre
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]  # Intercambia
                index = parent  # Actualiza el índice al del padre
            else:  # Si no es mayor
                break  # Sale del ciclo
    
    def _heapify_down(self, index):  # Método privado para bajar un elemento
        n = len(self.heap)  # Obtiene el tamaño del heap
        while True:  # Ciclo infinito hasta que se rompa
            largest = index  # Asume que el mayor es el actual
            left = 2 * index + 1  # Índice del hijo izquierdo
            right = 2 * index + 2  # Índice del hijo derecho
            if left < n and self.heap[left] > self.heap[largest]:  # Si el hijo izquierdo es mayor
                largest = left  # Actualiza el mayor
            if right < n and self.heap[right] > self.heap[largest]:  # Si el hijo derecho es mayor
                largest = right  # Actualiza el mayor
            if largest != index:  # Si el mayor no es el actual
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]  # Intercambia
                index = largest  # Actualiza el índice
            else:  # Si ya está en orden
                break  # Sale del ciclo

def test_1_5():  # Define la función de pruebas
    heap = MaxHeap()  # Crea una instancia de MaxHeap
    
    heap.insert(3)  # Inserta el valor 3 en el heap
    heap.insert(1)  # Inserta el valor 1 en el heap
    heap.insert(5)  # Inserta el valor 5 en el heap
    record_test("1.5.1 MaxHeap insertion", heap.heap[0] == 5)  # Verifica que la raíz sea 5
    
    max_val = heap.delete_max()  # Elimina el valor máximo del heap
    record_test("1.5.2 MaxHeap deletion", max_val == 5)  # Verifica que el valor eliminado sea 5
    
    heap.build_heap([3, 1, 4, 1, 5, 9, 2])  # Construye un heap desde el arreglo dado
    record_test("1.5.3 Build heap from array", heap.heap[0] == max(heap.heap))  # Verifica que la raíz sea el máximo
    
    valid_max_heap = all(  # Verifica la propiedad de heap para todos los nodos
        heap.heap[i] >= heap.heap[2*i+1] if 2*i+1 < len(heap.heap) else True
        for i in range(len(heap.heap)//2)
    )
    record_test("1.5.4 Heap property verification", valid_max_heap)  # Registra el resultado
    
    heap.build_heap([])  # Construye un heap desde un arreglo vacío
    record_test("1.5.5 Empty array handling", len(heap.heap) == 0)  # Verifica que el heap esté vacío

test_1_5()  # Ejecuta la función de pruebas

for r in test_results:  # Recorre los resultados de las pruebas
    print(r)  # Imprime cada resultado
