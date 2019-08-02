#stack in Python can be interpreted as list, insert at head, pop at LIFO
stack = ["jaime", 1, "three", 5]
stack.append(30)
print(stack)
stack.pop()
print(stack)


#Queue in Python FIFO
"""Queue is a a structure FIFO, Like waiting in Lines"""
class Queue():
	def __init__(self):
		self.queue = list()

	def enqueue(self, value):
		#insert in front
		self.queue.append(value)

	def dequeue(self):
		if self.queue:
			del self.queue[0]
		else:
			print("Queues is empty")

	def get_len(self):
		return(len(self.queue))

q = Queue()
q.dequeue()
for i in range(1, 10):
	q.enqueue(i)
print(q.queue)
q.dequeue()
print(q.queue)