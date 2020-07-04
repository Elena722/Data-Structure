class Node:
    def __init__(self, name, is_directory=None, size=0):
        self.name = name
        self.parent = None
        self.children = {}
        self.is_directory = is_directory
        self.size = size if not is_directory else 0

    def __repr__(self):
        return f'{self.name}'

    def add_child(self, node):
        node.parent = self
        self.children[node.name] = node

    def calculate_size(self):
        if not self.is_directory:
            return self.size
        # return sum(ch.calculate_size() for ch in self.children.values())
        sum = 0
        for ch in self.children.values():
            sum += ch.calculate_size()
        return sum


dir = Node('dir', True)

home = Node('home', True)
dir.add_child(home)
jacub = Node('jacob', True)
home.add_child(jacub)

print(dir.children)
print(dir.children['home'].children)


var = Node('var', True)
dir.add_child(var)
log = Node('log ', True)
var.add_child(log)


jacub.add_child(Node('.bashrc', False, 50))
jacub.add_child(Node('.vimrc', False, 100))
jacub.add_child(Node('blob', False, 1023))

log.add_child(Node('sys.log', False, 10))

print(dir.children)  # ok
print(home.children)  # ok
print(var.children)  # ok
print(jacub.children)  # ok

print(jacub.children['blob'].is_directory)

print('----')

print(f'dir -> {dir.calculate_size()}b')
print(f'home -> {home.calculate_size()}b')
print(f'log -> {log.calculate_size()}b')
print(f'var -> {var.calculate_size()}b')
print(f'jacub -> {jacub.calculate_size()}b')