# Queue_FIFO(First-In-First-Out)
class Queue_FIFO:
	"""
	Make Queue used Python List
	---------------------------
	
	enqueue : Insert to Data
	
	dequeue : Take-Out and Remove to Data, First In First Out

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

		First In First Out
		Binding to First Data
		and, Remove to First Data
		"""
		get = self.list_[0]
		del self.list_[0]
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
test_queue = Queue_FIFO()

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
