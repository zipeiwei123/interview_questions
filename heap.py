""" Heap is a sorted near complete tree that could use to sort array , run time O(logN)"""
array = [9, 78, 34, 10, 23]

def build_min_heap(array):
    for i in reversed(range(len(array)//2)):
        min_heapify(array, i)

def min_heaify(array, index):
	#sort left and right array
	left = 2*i+1
	right = 2*i+2
	length = len(array) - 1
	smallest = i	
