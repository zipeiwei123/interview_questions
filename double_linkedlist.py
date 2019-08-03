#need more practice
class Node:
	def __init__(self, value):
		self.val = value
		self.previous = None
		self.next = None


class Double_linkedlist:
	def __init__(self):
		self.head = None


	def insert(self, value):
		new_node = Node(value)
		#first set new node to where the head point to
		new_node.next = self.head
		#set the previous pointer point to the new node
		if self.head is not None:
			self.head.previous = new_node


		self.head = new_node



	def remove(self):


	def search_for_node(self, value):
		Node = self.search(self.head, value)
		if Node != None:
			return Node
		else:
			print("Node is not found in linked list")


	def search(self, node, value):
		if node.value == value:
			return node
		if node == None:
			return None
		self.search(node.next, value)