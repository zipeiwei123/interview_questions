""" A tree like structure , used in key word search"""
"""            A
			/	  \
		   p	   c
		   				"""
#Build the trie 
longest_word_len = 26
class Node():
	def __init__(self, key):
		self.next = [None]*longest_word_len
		#check if this is the end
		self.end_word = False

class Trie():
	def __init__(self):
		self.root - None

	def insert(self, key):
		continue