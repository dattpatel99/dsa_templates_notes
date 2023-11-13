





# building a prefix sum
def prefixSum(arr):
    prefix = [arr[0]]
    for i in range(1, len(arr)):
        prefix.append(prefix[-1] + arr[i])
    
    return prefix


# efficient string building
def stringBuilding(arr):
    # arr is a list of characters
    ans = []
    for c in arr:
        ans.append(c)
    
    return "".join(ans)



# reverse linked list
def reverseLL(head):
    curr = head
    prev = None
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node 
        
    return prev

# Find number of subarrays that fit an exact criteria
from collections import defaultdict
def subarrayByCondition(arr, k):
    counts = defaultdict(int)
    counts[0] = 1
    ans = curr = 0

    for num in arr:
        # do logic to change curr
        ans += counts[curr - k]
        counts[curr] += 1
    
    return ans

# monotonic increasing stack
def increasingStack(arr):
    stack = []
    ans = 0

    for num in arr:
        # for monotonic decreasing, just flip the > to <
        while stack and stack[-1] > num:
            # do logic
            stack.pop()
        stack.append(num)
    
    return ans



# find top k elements
import heapq
def fn(arr, k):
    heap = []
    for num in arr:
        # do some logic to push onto heap according to problem's criteria
        heapq.heappush(heap, ("CRITERIA", num))
        if len(heap) > k:
            heapq.heappop(heap)
    
    return [num for num in heap]


# build a trie
# note: using a class is only necessary if you want to store data at each node.
# otherwise, you can implement a trie using only hash maps.
class TrieNode:
    def __init__(self):
        # you can store data at nodes if you wish
        self.data = None
        self.children = {}

def buildTrie(words):
    root = TrieNode()
    for word in words:
        curr = root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        # at this point, you have a full word at curr
        # you can perform more logic here to give curr an attribute if you want
    
    return root

# in order traversal of binary tree
def inOrderTraversal(root):
    if root:
        inOrderTraversal(root.left)
        print(root.val, end=" ")
        inOrderTraversal(root.right)

# pre order traversal of binary tree
def preOrderTraversal(root):
    if root:
        print(root.val, end=" ")
        preOrderTraversal(root.left)
        preOrderTraversal(root.right)

# post order traversal of binary tree
def postOrderTraversal(root):
    if root:
        postOrderTraversal(root.left)
        postOrderTraversal(root.right)
        print(root.val, end=" ")