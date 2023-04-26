from queue import Queue

q = Queue(maxsize=-1)

q.put('a')
q.get()
q.put('b')
q.put('c')
print(q.get())

print(q)