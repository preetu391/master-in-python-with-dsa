import queue
stack = queue.LifoQueue()
stack.put(1)
print(stack.queue,end=" ")
print(f"top element is {stack.queue[-1]}")
stack.put(2)
print(stack.queue,end=" ")
print(f"top element is {stack.queue[-1]}")
stack.put(3)
print(stack.queue,end=" ")
print(f"top element is {stack.queue[-1]}")
stack.get()
print(stack.queue,end=" ")
print(f"top element is {stack.queue[-1]}")
stack.get()
print(stack.queue,end=" ")
print(f"top element is {stack.queue[-1]}")
stack.put(6)
print(stack.queue,end=" ")
print(f"top element is {stack.queue[-1]}")
