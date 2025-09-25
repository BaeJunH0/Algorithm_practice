import sys

input = sys.stdin.readline

# 조건 : min heap을 구현하되, 대소 비교를 절대값으로 수행해라 (만약 절대값이 같으면, 부호를 포함한 값이 더 작은 쪽이 더 작다)
class Heap:
    def __init__(self):
        self.values = []

    def _less(self, a, b):
        if abs(a) != abs(b):
            return abs(a) < abs(b)
        return a < b

    def _swap(self, a, b):
        self.values[a], self.values[b] = self.values[b], self.values[a]

    def _up(self):
        idx = len(self.values) - 1
        while idx > 0:
            parent = (idx - 1) // 2
            if self._less(self.values[idx], self.values[parent]):
                self._swap(idx, parent)
                idx = parent
            else:
                break

    def _down(self):
        idx = 0
        n = len(self.values)
        while True:
            left = idx * 2 + 1
            right = idx * 2 + 2
            smallest = idx
            if left < n and self._less(self.values[left], self.values[smallest]):
                smallest = left
            if right < n and self._less(self.values[right], self.values[smallest]):
                smallest = right
            if smallest == idx:
                break
            self._swap(idx, smallest)
            idx = smallest

    def _is_empty(self):
        return len(self.values) == 0

    def push(self, value):
        self.values.append(value)
        self._up()

    def pop(self):
        if self._is_empty():
            return 0
        last_idx = len(self.values) - 1
        self._swap(0, last_idx)
        response = self.values.pop()
        if not self._is_empty():
            self._down()
        return response

    def __iter__(self):
        for i in self.values:
            yield i

    def __str__(self):
        return "heap's elements : [" + ", ".join(map(str, self)) + "]"

if __name__ == '__main__':
    heap = Heap()

    for i in range(int(input())):
        command = int(input())

        if command != 0:
            heap.push(command)
        else:
            print(heap.pop())