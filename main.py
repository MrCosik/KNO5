import time

from treelib import Tree, Node

# 1)
tree = Tree()
tree.create_node("Harry", "h")
tree.create_node("Jane", "j", parent="h")
tree.create_node("Bill", "b", parent="h")
tree.create_node("Diane", "d", parent="j")
tree.create_node("Mary", "m", parent="d")
tree.create_node("Harry", "h2", parent="j")

tree.show()

x = tree.get_node("m")
print(x.tag)
print(x.identifier)
y = tree.parent("m")
print(y.tag)
print(y.identifier)
z = tree.get_node("h")
print(z.tag)
print(z.is_root())


# b)
def dupilcate_node_path_check(tree, node):
    current_node = node
    duplicates = set()
    while current_node.identifier != tree.root:
        parent = tree.parent(current_node.identifier)
        if node.tag == parent.tag:
            duplicates.add(parent.tag)
        current_node = parent
    if len(duplicates) > 0:
        return True
    else:
        return False


print('----------------------------------------')
print('2 b)')
x = tree.get_node("h2")
print(dupilcate_node_path_check(tree, x))
x = tree.get_node("m")
print(dupilcate_node_path_check(tree, x))

# 2
reachable_states = {"Gdansk": [["Gdynia", 24], ["Koscierzyna", 58], ["Tczew", 33], ["Elblag", 63]],
                    "Gdynia": [["Gdansk", 24], ["Lebork", 60], ["Wladyslawowo", 42]],
                    "Koscierzyna": [["Gdansk", 58], ['Lebork', 58], ['Bytow', 40], ['Chojnice', 70], ['Tczew', 59]],
                    'Chojnice': [['Koscierzyna', 70], ['Bytow', 65]],
                    'Bytow': [['Chojnice', 65], ['Koscierzyna', 40], ['Slupsk', 70]],
                    'Slupsk': [['Bytow', 70], ['Lebork', 55], ['Ustka', 21]],
                    'Ustka': [['Slupsk', 21], ['Leba', 64]],
                    'Leba': [['Ustka', 64], ['Wladyslawowo', 66], ['Lebork', 29]],
                    'Wladyslawowo': [['Leba', 66], ['Hel', 35], ['Gdynia', 42]],
                    'Hel': [['Wladyslawowo', 35]],
                    'Lebork': [['Leba', 29], ['Slupsk', 55], ['Koscierzyna', 58], ['Gdynia', 60]],
                    'Tczew': [['Gdansk', 33], ['Koscierzyna', 59], ['Elblag', 53]],
                    'Elblag': [['Gdansk', 63], ['Tczew', 53]]
                    }


# b)

def breadth_first_search(start_state, target_state):
    id = 0
    tree = Tree()
    current_node = tree.create_node(start_state, id)
    fifo_queue = []
    fifo_queue.append(current_node)
    while id < 200000:
        if len(fifo_queue) == 0:
            tree.show()
            print("failed to reach the target state")
            return 1
        current_node = fifo_queue[0]
        if current_node.tag == target_state:
            tree.show()
            print("the target state " + str(current_node.tag) + " with id = " + str(
                current_node.identifier) + " has been reached!")
            return 0
        del (fifo_queue[0])
        for elem in reachable_states[current_node.tag]:
            id += 1
            new_elem = tree.create_node(elem[0], id, parent=current_node.identifier)
            if not dupilcate_node_path_check(tree, new_elem): #sprawdzanie czy node już znajduje się w drzewie
                fifo_queue.append(new_elem)
    print("time limit exceeded")


print('----------------------------------------')
print('2 c)')
start = time.time()
breadth_first_search("Gdansk", "Ustka")
end = time.time()
print(end - start)
