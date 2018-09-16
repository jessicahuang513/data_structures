class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class BinaryTree:
	def __init__(self):
		self.root = None

	def add(self, val):
		newNode = Node(val)
		if(self.root == None):
			self.root = newNode
		else:
			self._add(self.root, newNode)

	def _add(self, root, node):
		if(root.val > node.val):
			if(root.left == None):
				root.left = node
			else:
				self._add(root.left, node)
		if(root.val <= node.val):
			if(root.right == None):
				root.right = node
			else:
				self._add(root.right, node)

	def printTree(self):
		if(tree.root != None):
			self._printTree(self.root, 0)

	def _printTree(self, root, count):
		if(root != None):
			self._printTree(root.left, count + 1)
			print(" " * count + str(root.val))
			self._printTree(root.right, count + 2)

tree = BinaryTree()
tree.add(3)
tree.add(2)
tree.add(9)
tree.add(-14)
tree.add(15)

tree.printTree()