class TextEditor:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []
        self.current_state = ""

    def make_change(self, new_state):
        # Push current state to undo stack before updating
        self.undo_stack.append(self.current_state)
        self.current_state = new_state
        # Clear redo stack on a new change
        self.redo_stack.clear()
        print(f"Document State: '{self.current_state}'")

    def undo(self):
        if not self.undo_stack:
            print("Cannot Undo: No previous state available.")
            return
        # Push current state to redo stack
        self.redo_stack.append(self.current_state)
        # Pop previous state from undo stack
        self.current_state = self.undo_stack.pop()
        print(f"Undo performed. Document State: '{self.current_state}'")

    def redo(self):
        if not self.redo_stack:
            print("Cannot Redo: No action to redo.")
            return
        # Push current state back to undo stack
        self.undo_stack.append(self.current_state)
        # Pop state from redo stack
        self.current_state = self.redo_stack.pop()
        print(f"Redo performed. Document State: '{self.current_state}'")

    def display(self):
        print(f"Current Document State: '{self.current_state}'")

# --- Test Case Execution ---
if __name__ == "__main__":
    editor = TextEditor()
    editor.make_change("Hello")           # Test Case 1
    editor.make_change("Hello World")     # Test Case 2
    editor.undo()                         # Test Case 3 (Back to "Hello")
    editor.redo()                         # Test Case 4 (Back to "Hello World")
    editor.undo()
    editor.undo()                         # Test Case 5 (Back to "")
    editor.redo()                         # Test Case 6 (Back to "Hello")