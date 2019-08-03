"""DFS used to find graph edges"""
#a class for each node in graph, where each node will have edges/key(name)/weights
class Node:
	def __init__(self, name = None, edges = []):
		self.name = name
		self.edges = edges
		self.weight = 1

class Graph:
	def __init__(self):
		"""An empty dictionary to store node as key, and correspondence edges of the node as value"""
		self.number_of_nodes = {}

	def insert_node(self, node):
		#append node in this step
		#check is the object is a class node
		#check if the node already exist in graph
		if isinstance(node, Node) and node not in self.number_of_nodes:
			#set the node
			self.number_of_nodes[node.name] = node.edges

	"""DFS works with stack, use stack to keep tracking the current path. starts with a cell, moves to its neighbours 
	randomly
		One path goes to end """
	def dfs(self, initial_node):
		stack = []
		stack.append(initial_node.name)
		last = initial_node
		while last:
			for neighbours in initial_node:
				"""select a neighbours on some conditions***"""
				if neighbours.value == 'B':
					initial_node = self.number_of_nodes['B']
					stack.append(initial_node)
	"""Three conditions
		1)if childnode not existed in visited.
		2)if childnode is the destine
		3)if childnode needs the backtracking (the childnode is exhausted)
												"""
	def dfs_with_backtracking(self, initial_node, destination):
		visited = set()
		
		
			



y  = Node("a", ["a", "b", "c"])
z  = Node("b", [ "c"])
x  = Node("c", ["b", "c"])

g = Graph()
g.insert_node(y)
g.insert_node(z)
g.insert_node(x)


