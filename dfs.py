""" A illustration of how dfs works with stack to iterate through all the nodes in graph"""
class node:
	def __init__(self):
		self.index = None
		self.edges = []

class Graph:
	def DFS(self, start_node):
		#LIFO
		#an empty stack to use for recorder
		stack = []
		#append the starting node
		stack.append(start_node)
		#an visited list to remember all the nodes in graph
		visited = []
		#append the start node to visited
		visited.append(start_node)
		while stack:
			#first select node that needs to append
			smallest = min(stack[-1].edges)
			#second, if node in visited, pop the stack
			if smallest in visited:
				stack.pop()
			#third if node not in visited, push on to the stack
			else:
				stack.append(smallest)
		return visited

	
	def BFS(self, start_node):
		#FIFO
		#an empty queue to keep track for recorder
		queue = []
		#append start node
		queue.append(start_node)
		#an visited list to remember all the nodes in graph
		visited = []
		#append the start node
		visited.append(start_node)
		while queue:
			#if current node has connection
			if queue[0].edges:
				#append all the child node
				for child in queue[0].edges:
					queue.append(child)
					if child not in visited:
						visited.append(child)
					
				#remove the first node from left
				del queue[0]
			


