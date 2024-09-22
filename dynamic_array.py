import time
import bisect
import sys

# Step 2: Create a dynamic array with different resizing strategies
class DynamicArray:
    def __init__(self, strategy):
        # Step 2: Initialize with size 2, and set the strategy for resizing
        self.array = []
        self.capacity = 2
        self.strategy = strategy
        self.fib_seq = [2, 3]  # Initial Fibonacci sequence for strategy C
        self.increase_count = 0

    # Step 3: Resizing strategies (A: Incremental, B: Doubling, C: Fibonacci)
    def _resize(self):
        if self.strategy == 'A':
            # Incremental strategy: increase capacity by 10
            self.capacity += 10
        elif self.strategy == 'B':
            # Doubling strategy: double the capacity
            self.capacity *= 2
        elif self.strategy == 'C':
            # Fibonacci strategy: increase capacity based on Fibonacci sequence
            next_fib = self.fib_seq[-1] + self.fib_seq[-2]
            self.fib_seq.append(next_fib)
            self.capacity = next_fib
        print(f"Resizing: New capacity = {self.capacity}")

    # Step 4: Insert words using binary search (to keep it sorted)
    def insert(self, word):
        # Measure time for each binary search and insertion
        start_time = time.time()
        
        # Step 6: Check if we need to resize the array
        if len(self.array) >= self.capacity:
            self._resize()
            self.increase_count += 1
            # Step 12: Print size, memory, and required elements after resizing
            self.print_stats()

        # Use binary search to insert the word in the sorted array
        bisect.insort(self.array, word)
        
        end_time = time.time()
        # Step 5: Measure the time at each insertion
        print(f"Time for inserting {word}: {end_time - start_time:.6f} seconds")

    # Step 12: Print stats like array size, capacity, and key elements at each resizing point
    def print_stats(self):
        n = len(self.array)
        if n > 0:
            print(f"Array size = {n}, Capacity = {self.capacity}")
            print(f"1st -> {self.array[0]}")
            if n >= 4:
                print(f"[n/4]th -> {self.array[n//4]}")
            print(f"[n/2]th -> {self.array[n//2]}")
            if n >= 4:
                print(f"[3n/4]th -> {self.array[3*n//4]}")
            print(f"nth -> {self.array[-1]}")
            # Step 10: Memory usage
            print(f"Memory used: {sys.getsizeof(self.array)} bytes")


# Step 1: Load words from EOWL (text file containing words)
def load_words(file_path):
    with open(file_path, 'r') as f:
        words = f.read().splitlines()  # Read words from file and split by line
    return sorted(words)  # Sorting words initially to maintain sorted array easily

# Step 7: Measure time for insertion of words into dynamic array
def timed_insert(dynamic_array, word_list):
    start_time = time.time()
    for word in word_list:
        dynamic_array.insert(word)
    end_time = time.time()
    print(f"Total time: {end_time - start_time:.6f} seconds")


# Step 9: Perform the same task with Python’s built-in list
def python_list_insert(word_list):
    python_list = []
    start_time = time.time()
    for word in word_list:
        bisect.insort(python_list, word)
    end_time = time.time()
    print(f"Total time for Python list: {end_time - start_time:.6f} seconds")
    # Print key elements for comparison
    n = len(python_list)
    if n > 0:
        print(f"1st -> {python_list[0]}")
        if n >= 4:
            print(f"[n/4]th -> {python_list[n//4]}")
        print(f"[n/2]th -> {python_list[n//2]}")
        if n >= 4:
            print(f"[3n/4]th -> {python_list[3*n//4]}")
        print(f"nth -> {python_list[-1]}")


# Main Execution
# Step 1: Load words from the Open English Word List
word_list = load_words('words.txt')

# Step 8: Use different strategies for resizing and measure the performance
# Strategy A: Incremental growth (Increase by 10)
print("\n--- Strategy A: Incremental Growth ---")
dynamic_array_A = DynamicArray('A')
timed_insert(dynamic_array_A, word_list)

# Strategy B: Doubling growth (Double the array size)
print("\n--- Strategy B: Doubling Growth ---")
dynamic_array_B = DynamicArray('B')
timed_insert(dynamic_array_B, word_list)

# Strategy C: Fibonacci growth (Fibonacci sequence for array resizing)
print("\n--- Strategy C: Fibonacci Growth ---")
dynamic_array_C = DynamicArray('C')
timed_insert(dynamic_array_C, word_list)

# Step 9: Compare with Python's built-in list (ArrayList implementation)
print("\n--- Python Built-in List ---")
python_list_insert(word_list)

# Step 10: Empirical time and space complexity has been measured through the timed insertion and memory prints.
# Step 11: Compare the theoretical analysis of time and space complexity with the empirical results.