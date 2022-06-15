# Queue_LIFO(Last-In-First-Out)
class Queue_LIFO:
	"""
	Make Queue used Python List
	---------------------------
	
	enqueue : Insert to Data
	
	dequeue : Take-Out and Remove to Data, Last In First Out

	qsize : How Many Data in Queue
	"""

	def __init__(self):
		"""
		Make Empty List
		"""
		self.list_ = []

	def enqueue(self, data):
		"""
		return None

		data : Data to be Inserted
		"""
		self.list_.append(data)

	def dequeue(self):
		"""
		return, print First data

		Last In First Out
		Binding to Last Data
		and, Remove to Last Data
		"""
		get = self.list_[-1]
		del self.list_[-1]
		print(f'Get Data : {get}')
		return get

	def qsize(self):
		"""
		return, print  Queue Size
		"""
		qsize_ = len(self.list_)
		print(f'Qsize : {qsize_}')
		return qsize_



# Make Queue
test_queue = Queue_LIFO()

# Insert Data
for i in range(10):
	test_queue.enqueue(i)

# Check How Many Data in Queue
test_queue.qsize()

# Get, Remove to 3 Data
for _ in range(3):
	test_queue.dequeue()

# Check How Many Data in Queue
test_queue.qsize()

# Get, Remove to All Data
for _ in range(7):
	test_queue.dequeue()

# Check How Many Data in Empty Queue
test_queue.qsize()
