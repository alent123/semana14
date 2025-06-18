test_results = []  # Creamos una lista vacía para guardar los resultados de las pruebas

def record_test(test_name, condition):  # Definimos una función para registrar si una prueba pasó o falló
    emoji = "✅" if condition else "❌"  # Si la condición es verdadera, usamos un check verde; si no, una cruz roja
    test_results.append(f"{emoji} {test_name}")  # Guardamos el nombre de la prueba con el emoji en la lista

class MinHeap:  # Definimos la clase MinHeap (montículo mínimo)
    def __init__(self):  # Constructor: se ejecuta cuando se crea un objeto de esta clase
        self.heap = []  # Inicializamos el montículo como una lista vacía

    def insert(self, value):  # Método para insertar un valor en el montículo
        self.heap.append(value)  # Añadimos el nuevo valor al final de la lista
        self._heapify_up(len(self.heap) - 1)  # Llamamos a _heapify_up con el índice del nuevo elemento (último)

    def _heapify_up(self, index):  # Método privado que sube el valor para mantener el orden del montículo
        while index > 0:  # Mientras no estemos en la raíz (posición 0)
            parent = self._parent_index(index)  # Obtenemos el índice del padre del nodo actual
            if self.heap[index] < self.heap[parent]:  # Si el valor actual es menor que el de su padre
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]  # Intercambiamos los valores
                index = parent  # Actualizamos el índice al del padre (seguimos subiendo)
            else:  # Si ya está en la posición correcta
                break  # Salimos del bucle

    def _parent_index(self, index):  # Método privado para obtener el índice del padre de un nodo
        if index == 0:  # Si el índice es 0, no tiene padre (es la raíz)
            return -1  # Retornamos -1 como señal
        return (index - 1) // 2  # Fórmula para obtener el índice del padre en un arreglo de heap

    def size(self):  # Método que devuelve el tamaño del montículo
        return len(self.heap)  # Devolvemos la longitud de la lista

    def peek(self):  # Método que devuelve el valor mínimo (raíz), sin eliminarlo
        if not self.heap:  # Si el montículo está vacío
            return None  # Retornamos None (nulo)
        return self.heap[0]  # Si no está vacío, retornamos el primer valor (mínimo)

def test_1_3():  # Función para ejecutar las pruebas del challenge 3
    heap = MinHeap()  # Creamos un nuevo montículo mínimo

    heap.insert(5)  # Insertamos el número 5
    record_test("1.3.1 Single element insertion", heap.heap == [5])  # Verificamos que el heap tenga solo [5]

    heap.insert(3)  # Insertamos el número 3
    heap.insert(8)  # Insertamos el número 8
    heap.insert(1)  # Insertamos el número 1
    record_test("1.3.2 Multiple insertions", len(heap.heap) == 4)  # Verificamos que haya 4 elementos en total

    record_test("1.3.3 Minimum tracking", heap.peek() == 1)  # Verificamos que el mínimo sea 1 (la raíz)

    valid_heap = True  # Inicializamos una variable como verdadera
    for i in range(len(heap.heap) // 2):  # Recorremos solo los padres
        left = 2 * i + 1  # Calculamos el índice del hijo izquierdo
        right = 2 * i + 2  # Calculamos el índice del hijo derecho
        if left < len(heap.heap) and heap.heap[i] > heap.heap[left]:  # Si el hijo izquierdo existe y es menor
            valid_heap = False  # Entonces la propiedad del heap está rota
        if right < len(heap.heap) and heap.heap[i] > heap.heap[right]:  # Si el hijo derecho existe y es menor
            valid_heap = False  # También rompe la propiedad
    record_test("1.3.4 Heap property validation", valid_heap)  # Verificamos si se mantuvo la propiedad del heap

    record_test("1.3.5 Size consistency", heap.size() == 4)  # Verificamos que el tamaño sea exactamente 4

test_1_3()  # Ejecutamos la función de prueba

for r in test_results:  # Recorremos cada resultado de prueba
    print(r)  # Imprimimos el resultado
