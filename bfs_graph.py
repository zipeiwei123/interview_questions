""" As defined, BFS is a broader search, thus we will have a list of queue to remember the current visited node"""
def Node:
	def __init__(self, name, edges):
		self.name = name
		self.edges = []

def Graph:
	def __init__(self):
		#initial graph with key for node id and value for correspondence vertices
		self.number_of_nodes = {}

	#visist all the nodes
	def bfs_traverse(self, start):
		# a queue to keep check current level of ndoe
		queue = []
		# a list to store all visited node
		list_nodes = []
		#start with the first node
		queue.append(start.name)
		while queue:
			#first action pop the queue
			node = queue.pop()
			if node not in list_nodes:
				list_nodes.append(node)
				#two ways, one use node, one use graph
				childrens = node.edges
				# childrens = Graph[nodes]
				for children in childrens:
					queue.append(children)
		return list_nodes


	def bfs_shortest_path(self, start,  end):
		# a queue to keep check current level of ndoe
		queue = []
		# a list to store all visited node
		path = []

		if start.name == end.name:
			path.append(start.name)
			print("start is the end")
			return path
		#start with the first node
		queue.append(start.name)
		while queue:
			node = queue.pop()
			if node not in path:
				path.append(node)
				#two ways, one use node, one use graph
				childrens = node.edges
				for children in childrens:
					queue.append(children)
					if children.name == end.name:
						print("path found")
						path.append(children)
						return path

		return print("path is not found")




			
