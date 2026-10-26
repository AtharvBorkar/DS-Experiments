class EventQueueSystem:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.queue = []

    def add_event(self, event):
        if len(self.queue) >= self.capacity:
            print("Hash table/Queue overflow: Cannot add more events.")
            return
        self.queue.append(event)
        print(f"Event added successfully: '{event}'")

    def process_event(self):
        if not self.queue:
            print("Queue underflow: No pending events to process.")
            return
        processed = self.queue.pop(0)  # Dequeue from front
        print(f"Processed Event: '{processed}'")

    def display_events(self):
        if not self.queue:
            print("Queue is empty (Shows empty queue).")
        else:
            print("Pending Events (Front to Rear):", ", ".join(self.queue))

    def cancel_event(self, event):
        if event in self.queue:
            self.queue.remove(event)
            print(f"'{event}' canceled successfully.")
        else:
            print(f"Event '{event}' not found in queue.")

# --- Test Case Execution ---
if __name__ == "__main__":
    system = EventQueueSystem()
    system.add_event("Login Request")       # Test Case 1
    system.add_event("File Upload")         # Test Case 2
    system.display_events()                 # Test Case 3
    system.process_event()                  # Test Case 4
    system.cancel_event("File Upload")      # Test Case 5
    system.display_events()                 # Test Case 6