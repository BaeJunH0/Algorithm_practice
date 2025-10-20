import sys

input = sys.stdin.readline

def inorder(now):
    if now == '.':
        return
    
    left, right = tree[now]

    inorder(left)
    print(now, end = '')
    inorder(right)

def preorder(now):
    if now == '.':
        return
    
    left, right = tree[now]

    print(now, end = '')
    preorder(left)
    preorder(right)

def postorder(now):
    if now == '.':
        return
    
    left, right = tree[now]

    
    postorder(left)
    postorder(right)
    print(now, end = '')

T = int(input())
tree = {}

for i in range(T):
    a, b, c = input().rstrip().split()

    tree[a] = [b, c]

preorder('A')
print()
inorder('A')
print()
postorder('A')