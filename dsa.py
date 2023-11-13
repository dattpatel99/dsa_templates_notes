class Node:
    def __init__(self, val=-1, next: 'Node' = None, prev: 'Node' = None):
        self._val = val
        self._next = next
        self._prev = prev
    
    def setNext(self, node: 'Node'):
        self._next = node

    def setPrev(self, node: 'Node'):
        self._prev = node
    
    def getNext(self)->'Node':
        return self._next

    def getPrev(self) -> 'Node':
        return self._prev

class DoubleLinkedList:
    def __init__(self, head: Node, tail: Node = None):
        self.head = head
        self.tail = tail

    def append(self, node: Node):
        self.tail.setNext(node)
        node.setPrev(self.tail)
        self.tail = node
        while self.tail.getNext():
            self.tail = self.tail.getNext()

    def insert(self, location_node: Node, add_node: Node):
        add_node.setNext(location_node.getNext())
        add_node.setPrev(location_node)
        location_node.getNext().setPrev(add_node)
        location_node.setNext(add_node)
        
    def delete(self, node: Node):
        if node == self.head:
            self.head = self.head.getNext()
        elif node == self.tail:
            self.tail = self.tail.getPrev()
        else:
            node.getPrev().setNext(node.getNext())
            node.getNext().setPrev(node.getPrev())
    
    def pop(self):
        if self.tail:
            ans = self.tail
            new_tail = self.tail.getPrev()
            new_tail.setNext(None)
            self.tail = new_tail
            return ans
        return None
    
    def peek(self):
        if self.tail:
            return self.tail
        return None            

'''
Push, Pop, Peek, Size: O(1)
Search: O(n)
FILO
'''
class Stack:
    def __init__(self):
        self._s = []

    def search(self, k):
        if self._s:
            for _ in self._s:
                if _ == k:
                    return _
            return None

    def pop(self):
        if len(self._s) != 0:
            e = self._s[-1]
            self._s = self._s[:-1]
            return e
        return None

    def push(self, k)->None:
        self._s.append(k)

    def peek(self):
        if len(self._s) != 0:
            return self._s[-1]
        return None

class PriorityQueue:
    def __init__(self):
        pass
