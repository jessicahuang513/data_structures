class Node:
	def __init__(self, val):
		self.val = val
		self.next = None
		self.prev = None

class LinkedList:
	def __init__(self):
		self.head = None

	def add(self, val):
		newNode = Node(val)
		if(self.head == None):
			self.head = newNode
		else:
			self.head.prev = newNode
			newNode.next = self.head
			self.head = newNode

	def printList(self):
		current = self.head
		count = 0
		while(current != None):
			print("Node %d: %d" % (count, current.val))
			current = current.next
			count += 1

	def delete(self, val):
		current = self.head
		while(current != None):
			if(current.val == val):
				previousNode = current.prev
				nextNode = current.next
				if(previousNode != None):
					previousNode.next = nextNode
				if(nextNode != None):
					nextNode.prev = previousNode
				if(current == self.head):
					self.head = current.next
				current = None
				return
			current = current.next
		print('Node with value %d not found' % val)



list = LinkedList()
list.add(3)
list.add(2)
list.add(15)
list.add(9)

list.delete(9)
list.delete(10)

list.printList()