test_results = []  # Creamos una lista vacía para guardar los resultados de las pruebas

def record_test(test_name, condition):  # Función para registrar si una prueba pasó o falló
    emoji = "✅" if condition else "❌"  # Usamos un emoji según el resultado (verdadero o falso)
    test_results.append(f"{emoji} {test_name}")  # Guardamos el nombre de la prueba con el emoji

class MinHeap:  # Definimos la clase del montículo mínimo
    def __init__(self):  # Constructor que se ejecuta al crear un nuevo objeto MinHeap
        self.heap = []  # Inicializamos el heap como una lista vacía

    def delete_min(self):  # Método para eliminar y devolver el valor mínimo (raíz)
        if not self.heap:  # Si el montículo está vacío
            return None  # Retornamos None (no hay nada que eliminar)

        if len(self.heap) == 1:  # Si hay solo un elemento
            return self.heap.pop()  # Lo quitamos y lo retornamos directamente

        min_value = self.heap[0]  # Guardamos el valor mínimo actual (raíz)
        self.heap[0] = self.heap.pop()  # Reemplazamos la raíz con el último elemento y lo eliminamos
        self._heapify_down(0)  # Restauramos la propiedad del heap desde la raíz
        return min_value  # Retornamos el valor mínimo eliminado

    def _heapify_down(self, index):  # Método privado para empujar hacia abajo un valor que rompió la propiedad del heap
        while self._has_left_child(index):  # Mientras tenga hijo izquierdo (si no tiene, ya es hoja)
            smaller_child_index = self._left_child_index(index)  # Suponemos que el hijo izquierdo es el menor

            if self._has_right_child(index):  # Si también hay hijo derecho
                right_index = self._right_child_index(index)  # Obtenemos su índice
                if self.heap[right_index] < self.heap[smaller_child_index]:  # Comparamos ambos hijos
                    smaller_child_index = right_index  # Si el derecho es menor, usamos ese en su lugar

            if self.heap[index] > self.heap[smaller_child_index]:  # Si el valor actual es mayor que su hijo menor
                self.heap[index], self.heap[smaller_child_index] = self.heap[smaller_child_index], self.heap[index]  # Hacemos el intercambio
                index = smaller_child_index  # Bajamos al nuevo índice
            else:
                break  # Si ya cumple la propiedad, salimos del bucle

    def _left_child_index(self, index):  # Devuelve el índice del hijo izquierdo de un nodo
        return 2 * index + 1  # Fórmula estándar del heap para hijo izquierdo

    def _right_child_index(self, index):  # Devuelve el índice del hijo derecho de un nodo
        return 2 * index + 2  # Fórmula estándar del heap para hijo derecho

    def _has_left_child(self, index):  # Verifica si el nodo tiene hijo izquierdo
        return self._left_child_index(index) < len(self.heap)  # Debe estar dentro del tamaño del heap

    def _has_right_child(self, index):  # Verifica si el nodo tiene hijo derecho
        return self._right_child_index(index) < len(self.heap)  # También debe estar dentro del rango

    def size(self):  # Devuelve el número de elementos en el heap
        return len(self.heap)  # Simplemente retorna la longitud de la lista

def test_1_4():  # Función para ejecutar las pruebas del challenge 4
    heap = MinHeap()  # Creamos un nuevo heap

    result = heap.delete_min()  # Intentamos eliminar el mínimo de un heap vacío
    record_test("1.4.1 Empty heap deletion", result is None)  # Esperamos que retorne None

    heap.heap = [5]  # Colocamos un solo valor manualmente en el heap
    result = heap.delete_min()  # Lo eliminamos
    record_test("1.4.2 Single element deletion", result == 5 and heap.size() == 0)  # Debe retornar 5 y dejar el heap vacío

    heap.heap = [1, 3, 2, 7, 4]  # Insertamos valores directamente
    first = heap.delete_min()  # Eliminamos el primer mínimo (1)
    second = heap.delete_min()  # Eliminamos el siguiente mínimo (2)
    record_test("1.4.3 Multiple deletions", first == 1 and second == 2)  # Verificamos que los valores sean correctos

    heap.heap = [1, 3, 2, 7, 4, 5]  # Creamos un heap válido manualmente
    heap.delete_min()  # Eliminamos el mínimo (1), lo que puede afectar la estructura
    valid_heap = True  # Suponemos que el heap es válido
    for i in range(len(heap.heap) // 2):  # Verificamos la propiedad del heap para cada padre
        left = 2 * i + 1  # Índice del hijo izquierdo
        right = 2 * i + 2  # Índice del hijo derecho
        if left < len(heap.heap) and heap.heap[i] > heap.heap[left]:  # Si el hijo izquierdo es menor que el padre
            valid_heap = False  # Se rompe la propiedad
        if right < len(heap.heap) and heap.heap[i] > heap.heap[right]:  # Igual con el hijo derecho
            valid_heap = False
    record_test("1.4.4 Heap property maintenance", valid_heap)  # Registramos si la estructura sigue siendo válida

    initial_size = heap.size()  # Guardamos el tamaño actual
    heap.delete_min()  # Eliminamos otro valor
    record_test("1.4.5 Size tracking", heap.size() == initial_size - 1)  # Verificamos que el tamaño haya bajado en 1

test_1_4()  # Ejecutamos todas las pruebas

for r in test_results:  # Recorremos los resultados
    print(r)  # Mostramos cada uno en consola
