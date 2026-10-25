class HashTableLinearProbing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.deleted_marker = "DELETED"

    def _hash_function(self, key):
        return key % self.size

    def insert(self, key):
        original_index = self._hash_function(key)
        index = original_index
        
        for i in range(self.size):
            if self.table[index] is None or self.table[index] == self.deleted_marker:
                self.table[index] = key
                print(f"Key {key} inserted at index {index}.")
                return
            elif self.table[index] == key:
                print(f"Key {key} already exists.")
                return
            index = (original_index + i + 1) % self.size
        print("Hash table overflow: Table is full.")

    def search(self, key):
        original_index = self._hash_function(key)
        index = original_index
        
        for i in range(self.size):
            if self.table[index] is None:
                print(f"Search({key}): Key not found.")
                return -1
            if self.table[index] == key:
                print(f"Key {key} found at index {index}.")
                return index
            index = (original_index + i + 1) % self.size
        print(f"Search({key}): Key not found.")
        return -1

    def delete(self, key):
        index = self.search(key)
        if index != -1:
            self.table[index] = self.deleted_marker
            print(f"Key {key} deleted successfully.")

    def display(self):
        print("Hash Table Status:")
        for idx, val in enumerate(self.table):
            print(f"Index {idx}: {val}")

# --- Test Case Execution ---
if __name__ == "__main__":
    ht = HashTableLinearProbing(10)
    ht.insert(15)            # Test Case 1
    ht.insert(25)            # Test Case 2 (Collision -> Index 6)
    ht.insert(35)            # Test Case 3 (Collision -> Index 7)
    ht.search(25)            # Test Case 4
    ht.search(45)            # Test Case 5
    ht.delete(25)            # Test Case 6
    ht.search(25)            # Test Case 7
    ht.display()             # Test Case 8