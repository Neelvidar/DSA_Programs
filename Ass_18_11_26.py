class node:
  def __init__(self, pid, name, pr):
    self.pid = pid
    self.name = name
    self.priority = pr
    self.next = None

class PriorityQueue:
  def __init__(self):
    self.front = self.rear = None

  # 1. Add Process (enqueue)
  def enqueue(self, new_node):
    if self.front == None:  # First node to be inserted
      self.front = new_node
      return
    if self.front.priority > new_node.priority:  # Insert at first position
      new_node.next = self.front
      self.front = new_node
      return
    else:
      temp = self.front
      while temp:
        if new_node.priority < temp.priority:  # Same priority keeps arrival order
          break
        else:
          prev = temp
          temp = temp.next
      prev.next = new_node
      new_node.next = temp

  # Helper: check whether a process ID already exists
  def exists(self, pid):
    temp = self.front
    while temp:
      if temp.pid == pid:
        return True
      temp = temp.next
    return False

  # 2. Execute Process (dequeue)
  def dequeue(self):
    if self.front:
      temp = self.front
      print(f"Executed Process -> ID: {temp.pid}, Name: {temp.name}, Priority: {temp.priority}")
      self.front = self.front.next
    else:
      print("No pending processes in queue")

  # 3. View Next Process (display_next)
  def display_next(self):
    if self.front:
      print(f"Next Process -> ID: {self.front.pid}, Name: {self.front.name}, Priority: {self.front.priority}")
    else:
      print("No pending processes in queue")

  # 4. Display Processes (display_all)
  def display_all(self):
    if self.front == None:
      print("No pending processes in queue")
      return
    temp = self.front
    print("Pending Processes:")
    while temp:
      print(f"[ID: {temp.pid} | Name: {temp.name} | Priority: {temp.priority}]")
      temp = temp.next

  # 5. Count Processes (count)
  def count(self):
    temp = self.front
    total = 0
    while temp:
      total += 1
      temp = temp.next
    print("Total pending processes:", total)


# --- Menu Driven Program ---
pq = PriorityQueue()

while True:
  print("\n--- CPU Process Scheduler ---")
  print("1. Add Process")
  print("2. Execute Process")
  print("3. View Next Process")
  print("4. Display All Processes")
  print("5. Count Processes")
  print("6. Exit")

  choice = input("Enter your choice: ").strip()

  if choice == "1":
    try:
      pid = int(input("Enter Process ID: "))
      name = input("Enter Process Name: ").strip()
      print("Priority: 1-System, 2-Interactive, 3-Background, 4-Low")
      pr = int(input("Enter Priority (1-4): "))

      if pr < 1 or pr > 4:
        print("Invalid priority! Choose 1 to 4.")
      elif pq.exists(pid):
        print(f"Process ID {pid} already exists!")
      else:
        pq.enqueue(node(pid, name, pr))
        print(f"Process added: ID={pid}, Name={name}, Priority={pr}")
    except ValueError:
      print("Invalid input! ID and priority must be numbers.")
  elif choice == "2":
    pq.dequeue()
  elif choice == "3":
    pq.display_next()
  elif choice == "4":
    pq.display_all()
  elif choice == "5":
    pq.count()
  elif choice == "6":
    print("Exiting...")
    break
  else:
    print("Invalid choice! Try again.")