"""Heap is a special data structure, that is a full balanced tree, parent-left-right, ordered by sorted size"""

""" Use index to represent the pointers in tree
	PARENT = (CHILD_INDEX-1)/2
	LEFT_CHILD = INDEX*2+1
	RIGHT_CHILD = INDEX*2+2 """

class Heap:
	def __init__(self, array):
		self.heap = array
		self.size = len(self.heap)


	def get_left_child(self, index):
		return index*2+1 


	def get_right_child(self, index):
		return index*2+2 

	def get_parent(self, child_index):
		return (child_index-1)+2 


	def has_left_child(self, index):
		return True if index < self.size else False


	def has_right_child(self, index):
		return True if index < self.size else False

	def has_parent(self, child_index):
		return True if child_index < self.size else False

	#swap value between node
	def swap(self, index_one, index_two):
		tmp = self.heap[index_one]
		self.heap[index_one] = self.heap[index_two]
		self.heap[index_two] = tmp

	#get max/min
	def peek(self):
		#return the first element if heap is not empty
		if self.heap:
			return self.heap[0]
		else:
			return False






	#sorted by heap
	def heapify(self):
		pass


