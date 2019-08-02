#Array 
#Python does not have an array structure, use list instead
array = [2,3,4,5,6,6,7]

#linked list
"""build a class for linked list, where the advantage of linked list is saving memory. disadvantage where it has linear search time"""

#first create a class object for node
"""Node[value, next]-> Node[value, next]"""
class Node():
	def __init__(self, value, n = None):
		self.next_node = n
		self.value = value

	def get_value(self):
		return(self.value)

	def get_next(self):
		return(self.next)

	

#second create a class object for linkedlist
class Linked_list():
	def __init__(self, head = None):
		#empty linked list, head == NONE
		self.head = head

	#running time O(1)
	def insert(self, value):
		#init node object
		new_node = Node(value, self.head)
		self.head = new_node

	# def get_size(self):
	# 	current = self.head
	# 	count = 0
	# 	while current:
	# 		count += 1
	# 		current = current.get_next()
	# 	return count

trial = Linked_list()

trial.insert(10)
trial.insert(20)
print(trial.head.next_node.value)


