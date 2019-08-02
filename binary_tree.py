""" Tree structure in Python, where we will have a tree node, and a tree class object"""
class Node():
	def __init__(self, key):
		self.value = key
		self.left = None
		self.right = None


class Tree():
	def __init__(self):
		self.root = None

    #if it is a search tree, that's mean left has the most small value, right has the largest value
	def insert_node(self, value):
		#check if root is none
		if self.root == None:
			self.root = Node(value)
		else:
			if self.root.value < value:
				#go right
				if self.root.right is None:
					#make a right node
					self.root.right = Node(value)
				else:
					self.insert_node(self.root.right, value)
			else:
				#go left
				if self.root.left is None:
					#make a right node
					self.root.left = Node(value)
				else:
					self.insert_node(self.root.left, value)

	def tree_traversal(self):
		self.tree_traversal_preorder(self.root)

	#preorder traversal root left right
	def tree_traversal_preorder(Node):
		#first stop condition
		if Node != None:
			self.tree_traversal_preorder(Node.left)
			print(Node.value)
			self.tree_traversal_preorder(Node.right)





alpha = Tree()
alpha.insert_node(20)
alpha.insert_node(30)
alpha.insert_node(10)
# print(alpha.root.value)
# print(alpha.root.right.value)
# print(alpha.root.left.value)
alpha.tree_traversal()


	
