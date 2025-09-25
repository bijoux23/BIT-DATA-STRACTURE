# ASSIGNMENT-1
project 1
school grades manager

- Integer Operations: Functions to compute the total, average, minimum, and maximum grades.
- String Formatting: A function to generate a formatted report of the grades.
- Booleans: A function to check if the average grade is below a specified threshold.
- Lists: A GradesList class for managing a dynamic list of grades, with methods to add and remove grades.
- Arrays: A GradesArray class that utilizes Python’s array module to handle a fixed-size array of grades.
- Dictionaries: A StudentRecords class to manage student records using a dictionary, allowing for adding and updating student grades.

  **assignment 3 project 3**
  **stack and queue**

  **Stack** (LIFO – Last In, First Out)

A stack keeps items in order, but the last added (pushed) item is the first removed (popped).

Think of it like a pile of plates: the top plate is taken off first.

Questions:

Practical (Rwanda – UR Canvas):

Stack = ["Register Course", "Upload Assignment", "Submit Quiz"].

Pop twice → removes "Submit Quiz" and then "Upload Assignment".

Remaining = "Register Course".

Practical (Rwanda – BK Mobile Banking):

Stack = ["Deposit", "Transfer", "Pay Bills"].

Undo last action → remove "Pay Bills".

Remaining = ["Deposit", "Transfer"].

Challenge (Reversing names):

Push names in stack: Eric → Alice → Jean.

Pop them out → Jean, Alice, Eric.

The order is reversed because stack always takes the last first.

Reflection (Why queue can’t reverse):

A queue is FIFO (first in, first out).

If you put words in, they come out in the same order, not reversed.

Queue (FIFO – First In, First Out)

A queue works like a line at a bank: the first to arrive is the first served.

Questions:

Practical (Rwanda – CHUK Pharmacy):

Patients = [P1, P2, P3, P4, P5].

After serving 3 → left = [P4, P5].

Front = P4.

Practical (Rwanda – Nyabugogo Buses):

Buses = [B1, B2, B3, B4].

After 1 departs (B1), next = B2.

Challenge (UR Cafeteria Orders):

Queue: orders served in arrival order → fair service.

If stack is used → last order placed is served first → unfair, earlier customers wait longer.

Reflection (Why queue in customer support):

Customers expect first come, first served.

Queue ensures fairness; stack would make new complaints jump ahead.
  
