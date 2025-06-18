test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class MinHeap:
    def __init__(self):
        self.heap = []
    def is_empty(self):
        return len(self.heap) == 0
    def size(self):
        return len(self.heap)

    def peek(self):
        if self.is_empty():
            return None
        return min(self.heap)

# test
def test_1_1():
    heap = MinHeap()
    record_test("1.1.1 Empty heap initialization", heap.is_empty() == True)
    heap.heap = [1, 3, 2] 
    record_test("1.1.2 Size tracking", heap.size() == 3)
    record_test("1.1.3 Peek functionality", heap.peek() == 1)
    empty_heap = MinHeap()
    record_test("1.1.4 Empty heap edge case", empty_heap.peek() is None)
    record_test("1.1.5 Type validation", isinstance(heap.is_empty(), bool))
# 🚀 Run tests
test_1_1()

# 📋 Summary
for r in test_results:
    print(r)
