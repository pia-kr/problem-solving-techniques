# 트리 만들기 기본 틀 - 노드
class node:
    def __init__(self, x):
        self.key = x
        self.left = None
        self.right = None
        self.parent = None

# 기본틀 - 생성할 트리
class tree:
    def __init__(self):
        self.root = None
        self.nodes = {}
    # parent를 기준으로 왼쪽 오른쪽 추가
    def add(self, parent, left, right):

        if parent not in self.nodes:
            self.nodes[parent] = node(parent)

        if self.root is None:
            self.root = self.nodes[parent]
        # '.' 인 경우에는 없는것으로 간주
        if left != '.':
            if left not in self.nodes:
                self.nodes[left] = node(left)
            self.nodes[parent].left = self.nodes[left]

        if right != '.':
            if right not in self.nodes:
                self.nodes[right] = node(right)
            self.nodes[parent].right = self.nodes[right]

    # 전위 순회 : 루트 -> 왼쪽 -> 오른쪽
    def preorder(self, current):
        if current is None:
            return

        print(current.key, end='')
        self.preorder(current.left)
        self.preorder(current.right)

    # 중위 순회 : 왼쪽 -> 루트 -> 오른쪽
    def inorder(self, current):
        if current is None:
            return

        self.inorder(current.left)
        print(current.key, end='')
        self.inorder(current.right)

    # 후위 순회 : 왼쪽 -> 오른쪽 -> 루트
    def postorder(self, current):
        if current is None:
            return

        self.postorder(current.left)
        self.postorder(current.right)
        print(current.key, end='')


# 입력 처리
n = int(input())
t = tree()

for _ in range(n):
    parent, left, right = input().split()
    t.add(parent, left, right)

# 출력
t.preorder(t.root)
print()
t.inorder(t.root)
print()
t.postorder(t.root)