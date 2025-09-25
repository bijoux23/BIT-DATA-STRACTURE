# UR Canvas stack simulation
stack = []

# Push operations
stack.append("Register Course")
stack.append("Upload Assignment")
stack.append("Submit Quiz")

print("Initial stack:", stack)

# Pop twice
stack.pop()
stack.pop()

print("Stack after popping twice:", stack)
print("Action that remains:", stack[-1])
# BK Mobile Banking stack simulation
stack = []

# Push operations
stack.append("Deposit")
stack.append("Transfer")
stack.append("Pay Bills")

print("Initial stack:", stack)

# Undo last action (pop)
last_action = stack.pop()

print("Action undone:", last_action)
print("Stack after undo:", stack)
names = ["Eric", "Alice", "Jean"]
stack = []

# Step 2: Push all names into the stack
for name in names:
    stack.append(name)

# Step 3: Pop names to reverse
reversed_names = []
while stack:
    reversed_names.append(stack.pop())

print("Original order:", names)
print("Reversed order:", reversed_names)
from collections import deque

# Queue of patients
queue = deque(["Patient1", "Patient2", "Patient3", "Patient4", "Patient5"])
print("Initial queue:", list(queue))

# 3 patients served (dequeue)
queue.popleft()
queue.popleft()
queue.popleft()

print("Queue after serving 3 patients:", list(queue))
print("Patient at the front now:", queue[0])
# Queue of buses
queue = deque(["Bus1", "Bus2", "Bus3", "Bus4"])
print("Initial queue:", list(queue))

# First bus departs
queue.popleft()

print("Queue after 1 departs:", list(queue))
print("Next bus to depart:", queue[0])
# Step 1: Queue for cafeteria orders
orders = deque()

# Step 2: Students place orders
orders.append("Order1")
orders.append("Order2")
orders.append("Order3")

# Step 3: Serve in arrival order
while orders:
    print("Preparing:", orders.popleft())

