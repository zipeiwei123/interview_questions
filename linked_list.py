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
	def insert_at_head(self, value):
		#init node object
		new_node = Node(value, self.head)
		self.head = new_node

	#insert at specific location
	def insert_at_node(self, previous_node, value):
		#init node object
		new_node = Node(value, previous_node)
		previous_node = new_node

	def insert_at_tail(self, value):
		#set the next pointer to None
		new_node = Node(value)
		#iterate through the linked list to find the last node on the linkedlist
		last = self.head
		while last.next_node:
			last = last.next_node
		
		#set last pointer point to the new node
		last.next_node = new_node
		

	def search_for_node(self, value):
		last = self.head
		while(last.next_node):
			if last.value == value:
				return last
		return "node not found"


	def traverse(self):
		l = []
		last = self.head
		while last:
			l.append(last.value)
			last = last.next_node

		return l




trial = Linked_list()

trial.insert_at_head(10)
trial.insert_at_head(20)
trial.insert_at_head(30)
print(trial.traverse())
trial.insert_at_tail(40)
print(trial.traverse())
print(trial.search_for_node(30).value)
print(trial.search_for_node(70))

#print(trial.head.next_node.value)


