class Node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next
	
	def print_node(self):
		print(self.data)
	
	
class LinkedList:
	def __init__(self):
		self.head = None
	
	def append_node(self, data):
		if not self.head :
			self.head = Node(data)
			return
		current = self.head
		while current.next:
			current = current.next
		current.next = Node(data)
		
	def search(self,target):
		current = sef.head
		while current != None:
			if current.data == target:
				print('Element found!')
				return True
			current = current.next
		print('Element Not Found in the list!')
		return False
	
	def print_list(self):
		node = self.head
		while node is not None:
			print(node.data)
			node = node.next

			
if __name__ == '__main__':
	linked_list = LinkedList()
	linked_list.append_node('Monday')
	linked_list.append_node('Tuesday')
	linked_list.print_list()

""" Code written by Karthik V (https://github.com/karthik200116/) """
