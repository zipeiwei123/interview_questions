"""DFS used to find graph edges"""
#a class for each node in graph, where each node will have edges/neigbours
class Node:
	def __init__(self, name):
		self.name = name
		self.edges = list()


class Graph:
	def __init__(self):
		#store node and its edges as dictionary Node:[Edge1, Edge2, Edge3]
		self.number_of_nodes = {}

	def add_node(self, node):
		if isinstance(node, Node) and node.name not in self.number_of_nodes:
			#add node
			self.number_of_nodes[node.name] = node


