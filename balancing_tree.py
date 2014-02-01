# The purpose of this is to implement self-balancing trees, not find the most efficient
# algorithm for the task.

class BSTNode:
	def __init__(self, parent=None):
		self.left = None
		self.max_depth_right = 0
		self.max_depth_left = 0
		self.right = None
		self.data = None
		#requires method compare, attributes key and count
		self.parent = parent
	
	def insert_data(self, data):
		# data type requires a compare() attribute, if not None it should return -1, 0, 1.
		# A value of 0 means data the data type supports the count attribute, which will be incremented.
		# If compare == None, we use <, >, =. Nodes start empty and create child nodes
		# when they get a data object.
		if self.data is None:
			self.data = data
			self.left = BSTNode(self)
			self.max_depth_left += 1
			self.right = BSTNode(self)
			self.max_depth_right += 1
			self.fix_depth_above()
		elif data.compare is not None:
			if data.compare(self.data) is 1:
				self.right.balance()
				self.right.insert_data(data)
			if data.compare(self.data) is -1:
				self.left.balance()
				self.left.insert_data(data)
			if data.compare(self.data) is 0:
				self.data.count += 1
		else:
			if data.key > self.data.key:
				self.right.balance()
				self.right.insert_data(data)
			elif data.key < self.data.key:
				self.left.balance()
				self.left.insert_data(data)
			else:
				self.data.count += 1
		
	def fix_depth_above(self):
		if self.parent is not None:
			if self.parent.right is self:
				self.parent.max_depth_right = max(self.max_depth_left, \
													self.max_depth_right) + 1
			if self.parent.left is self:
				self.parent.max_depth_left =  max(self.max_depth_left, \
													self.max_depth_right) + 1
			self.parent.fix_depth_above()
		
	def balance(self):
		TOL = 2
		if self.max_depth_right > self.max_depth_left + TOL:
			temp = self.right
			if self.parent is not None: 
				if self.parent.right is self:
					self.parent.right = temp
				else:
					self.parent.left = temp
			self.right = temp.left
			if self.right is not None:
				self.right.parent = self
			temp.left = self 
			temp.parent = self.parent
			self.parent = temp
			self.max_depth_right = temp.max_depth_left
			self.fix_depth_above()
		elif self.max_depth_left > self.max_depth_right + TOL:
			temp = self.left
			if self.parent is not None: 
				if self.parent.right is self:
					self.parent.right = temp
				else:
					self.parent.left = temp
			self.left = temp.right
			if self.left is not None:
				self.left.parent = self
			temp.right = self
			temp.parent = self.parent
			self.parent = temp
			self.max_depth_left = temp.max_depth_right
			self.fix_depth_above()
	
class WordCount:
	def __init__(self, key):
		self.compare = None
		self.key = key
		self.count = 1
		
def print_tree(node, prefix=''):
	if node.left is not None:
		print_tree(node.left, prefix+'|')
	if node.data is not None:
		print prefix, '-', node.data.key, node.data.count#\
					#, 'depth right:', node.max_depth_right, 'depth left:', node.max_depth_left
	if node.right is not None:
		print_tree(node.right, prefix + '|')
		
text = """ zounds hello friends and acres aardvarks abaci friends enemies wicked"""

words = [WordCount(word.strip('.,?!\"\';()[]-').lower()) for word in text.split()]

root = BSTNode()

for data in words:
	root.insert_data(data)
	
print_tree(root)
	