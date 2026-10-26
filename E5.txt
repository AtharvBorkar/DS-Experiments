class HashTableChaining:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        # Check if key already exists, update value if found
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                print(f"Key {key} updated with value '{value}' at index {index}.")
                return
        # Otherwise append new (key, value) pair
        self.table[index].append([key, value])
        print(f"Key {key} inserted at index {index}.")

    def search(self, key):
        index = self._hash_function(key)
        for item in self.table[index]:
            if item[0] == key:
                print(f"Search({key}): Value = '{item[1]}'")
                return item[1]
        print(f"Search({key}): Key not found.")
        return None

    def delete(self, key):
        index = self._hash_function(key)
        for i, item in enumerate(self.table[index]):
            if item[0] == key:
                del self.table[index][i]
                print(f"Key {key} deleted successfully.")
                return
        print(f"Delete({key}): Key not found.")

# --- Test Case Execution ---
if __name__ == "__main__":
    ht = HashTableChaining()
    ht.insert(15, "A")       # Test Case 1 (Index 5)
    ht.insert(25, "B")       # Test Case 2 (Index 5 - Collision handled by chaining)
    ht.search(15)            # Test Case 3
    ht.search(30)            # Test Case 4
    ht.delete(25)            # Test Case 5
    ht.search(25)            # Test Case 6