import random

class HashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity=10, load_factor_threshold=0.7):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity
        self.load_factor_threshold = load_factor_threshold
        self._p = 1000000007
        self._a = random.randint(1, self._p - 1)
        self._b = random.randint(0, self._p - 1)

    def _hash(self, key):
        hash_val = hash(key)
        return ((self._a * hash_val + self._b) % self._p) % self.capacity

    def _resize(self, new_capacity):
        print(f"\n--- Load factor exceeded. Resizing from {self.capacity} to {new_capacity}... ---")
        old_table = self.table
        self.capacity = new_capacity
        self.size = 0
        self.table = [None] * self.capacity
        self._a = random.randint(1, self._p - 1)
        self._b = random.randint(0, self._p - 1)

        for head_node in old_table:
            current = head_node
            while current:
                self.insert(current.key, current.value)
                current = current.next

    def insert(self, key, value):
        if (self.size / self.capacity) >= self.load_factor_threshold:
            self._resize(2 * self.capacity)
            
        index = self._hash(key)
        node = self.table[index]
        
        while node:
            if node.key == key:
                node.value = value
                return
            node = node.next
            
        new_node = HashNode(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node
        self.size += 1

    def search(self, key):
        index = self._hash(key)
        node = self.table[index]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return None

    def delete(self, key):
        index = self._hash(key)
        node = self.table[index]
        prev = None
        while node:
            if node.key == key:
                if prev is None:
                    self.table[index] = node.next
                else:
                    prev.next = node.next
                self.size -= 1
                return True
            prev = node
            node = node.next
        return False

    def get_performance_stats(self):
        load_factor = self.size / self.capacity if self.capacity > 0 else 0
        return {
            "size": self.size,
            "capacity": self.capacity,
            "load_factor": f"{load_factor:.2f}"
        }

    def __str__(self):
        items = []
        for i in range(self.capacity):
            items.append(f"Bucket {i}:")
            node = self.table[i]
            if node is None:
                items.append(" Empty")
            else:
                while node:
                    items.append(f"  -> ('{node.key}': {node.value})")
                    node = node.next
        return "\n".join(items)

def create_example_table(ht):
    """
    Populates the given hash table instance with example data.
    """
    ht.__init__() 
    ht.insert("apple", 10)
    ht.insert("banana", 20)
    ht.insert("cherry", 30)
    ht.insert("date", 40)
    ht.insert("elderberry", 50)
    ht.insert("fig", 60)
    ht.insert("grape", 70)
    print("\n--- Example Table Created ---")
    print(ht)
    print("---------------------------\n")

def main():
    ht = HashTable()
    
    while True:
        print("\n--- Hash Table Menu ---")
        print("1. Insert a key-value pair")
        print("2. Search for a key")
        print("3. Delete a key")
        print("4. Print the current hash table")
        print("5. Create an example table")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            key = input("Enter the key: ")
            value = input("Enter the value: ")
            ht.insert(key, value)
            print(f"Inserted ('{key}': {value}).")
        
        elif choice == '2':
            key = input("Enter the key to search for: ")
            result = ht.search(key)
            if result is not None:
                print(f"Value for '{key}' is: {result}")
            else:
                print(f"Key '{key}' not found.")
                
        elif choice == '3':
            key = input("Enter the key to delete: ")
            if ht.delete(key):
                print(f"Key '{key}' deleted successfully.")
            else:
                print(f"Key '{key}' not found.")
                
        elif choice == '4':
            print("\n--- Current Hash Table ---")
            print(ht)
            print("--------------------------")

        elif choice == '5':
            create_example_table(ht)
            
        elif choice == '6':
            stats = ht.get_performance_stats()
            print("\n--- Final Hash Table State ---")
            print(f"Total items (size): {stats['size']}")
            print(f"Table capacity: {stats['capacity']}")
            print(f"Final load factor: {stats['load_factor']}")
            print("------------------------------")
            print("Exiting the program. Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == '__main__':
    main()
