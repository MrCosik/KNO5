from treelib import Tree, Node

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

def dupilcate_node_path_check(tree,node):



x = tree.get_node("h2")
print(dupilcate_node_path_check(tree, x))
x = tree.get_node("m")
print(dupilcate_node_path_check(tree, x))