"""
Trees

Implementation of a Binary Search Tree with associated methods.
"""

class Node:
	def __init__(self, value = None, left = None, right = None):
		self.left = left
		self.value = value
		self.right = right

	@property
	def isLeaf(self):
		if self.left == None and self.right == None:
			return True
		else:
			return False

	def defoliate(self):
		"""
		Removes leaves from tree. Root nodes are not considered leaves
		when they have no children.
		"""
		if self != None:
			if self.left != None:
				if self.left.isLeaf:
					self.left = None
				else:
					self.left.defoliate()

			if self.right !=None:
				if self.right.isLeaf:
					self.right = None
				else:
					self.right.defoliate()

class BinarySearchTree:
	def __init__(self, node = None):
		self.root = node

	def insertIterative(self, value):
		current_node = self.root
		node_not_inserted = True

		while node_not_inserted:
			if value < current_node.value:
				if current_node.left == None:
					current_node.left = Node(value)
					node_not_inserted = False
				else:
					current_node = current_node.left
			else:
				if current_node.right == None:
					current_node.right = Node(value)
					node_not_inserted = False
				else:
					current_node = current_node.right


def insertRecursive(node, value):
	if value < node.value:
		if node.left == None:
			node.left = Node(value)
		else:
			insertRecursive(node.left, value)
	else:
		if node.right == None:
			node.right = Node(value)
		else:
			insertRecursive(node.right, value)


def printInOrder(node):
	if node != None:
		printInOrder(node.left)
		print node.value
		printInOrder(node.right)

def printPreOrder(node):
	if node != None:
		print node.value
		printPreOrder(node.left)
		printPreOrder(node.right)

def printBreadthFirst(node):
	queue = []
	current_node = node
	queue.append(node)
	while len(queue) > 0:
		current_node = queue[0]
		print current_node.value
		queue.pop(0)
		if current_node.left != None:
			queue.append(current_node.left)
		if current_node.right != None:
			queue.append(current_node.right)


def printTree(me):
  if me == None:
    return ""
  else:
    return getRoot(me) + printTree(getLeft(me)) + printTree(getRight(me))


def height(node):
	if node == None:
		return 0
	else:
		return max(height(node.left), height(node.right)) + 1


# tests

node = Node(10)
tree = BinarySearchTree(node)
tree.insertIterative(1)
tree.insertIterative(8)
tree.insertIterative(20)
insertRecursive(node, -2)
insertRecursive(node, 11)
insertRecursive(node, 5)
# printInOrder(node)
# print "preOrder"
# printPreOrder(node)

# print "height"
# print height(node)
# print "defoliate"
# node.defoliate()
# printInOrder(node)
# printTree(node)
printBreadthFirst(node)
