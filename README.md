Algorithm Efficiency and Scalability AnalysisThis project provides the implementation and analysis for two key computer science algorithms as part of Assignment 3, focusing on the practical performance implications of different design choices.Part 1: Randomized vs. Deterministic Quicksort: An empirical analysis comparing the performance of two Quicksort implementations to highlight the benefits of randomization.Part 2: Hashing with Chaining: An interactive implementation of a robust hash table that demonstrates collision resolution and dynamic resizing.📂 Project ContentsThis repository contains the complete submission for the assignment.File NameDescriptionassignment3p1.pyPart 1: Python script for the Quicksort analysis.Quicksort_Analysis_Report.pdfPart 1: Detailed academic report with the rigorous theoretical analysis of Randomized Quicksort's average-case time complexity (O(nlogn)).assignment3p2.pyPart 2: Python script for the interactive Hash Table.Hashing_with_Chaining_Analysis.pdfPart 2: Academic report detailing the analysis of the hash table, including the role of the load factor and time complexities.requirements.txtPython dependencies (matplotlib) required for the Part 1 script.README.mdThis file.🚀 Running the ImplementationsPart 1: Quicksort ComparisonThis script runs a performance comparison between Randomized and Deterministic Quicksort and generates a plot visualizing the results.Set up the environment:# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
Run the script:python assignment3p1.py
This will print timing data to the console and then display the plot.--- Analyzing Random Arrays ---
Size: 100   | Deterministic: 0.00139s | Randomized: 0.00020s
Size: 500   | Deterministic: 0.00252s | Randomized: 0.00220s
Size: 1000  | Deterministic: 0.00527s | Randomized: 0.00279s
Size: 2500  | Deterministic: 0.01344s | Randomized: 0.02303s
Size: 5000  | Deterministic: 0.03929s | Randomized: 0.04398s
Size: 7500  | Deterministic: 0.06088s | Randomized: 0.07530s
--- Analyzing Sorted Arrays ---
Size: 100   | Deterministic: 0.00165s | Randomized: 0.00055s
Size: 500   | Deterministic: 0.02043s | Randomized: 0.00124s
Size: 1000  | Deterministic: 0.11451s | Randomized: 0.00611s
Size: 2500  | Deterministic: 0.67666s | Randomized: 0.01926s
--- Analyzing Reverse Sorted Arrays ---
Size: 100   | Deterministic: 0.00057s | Randomized: 0.00019s
Size: 500   | Deterministic: 0.04717s | Randomized: 0.00760s
Size: 1000  | Deterministic: 0.19455s | Randomized: 0.00601s
Size: 2500  | Deterministic: 1.45629s | Randomized: 0.02649s
--- Analyzing Repeated Arrays ---
Size: 100   | Deterministic: 0.00018s | Randomized: 0.00021s
Size: 500   | Deterministic: 0.01123s | Randomized: 0.00160s
Size: 1000  | Deterministic: 0.00360s | Randomized: 0.01010s
Size: 2500  | Deterministic: 0.01777s | Randomized: 0.02619s
Size: 5000  | Deterministic: 0.05801s | Randomized: 0.07474s
Size: 7500  | Deterministic: 0.08580s | Randomized: 0.18279s
Key FindingsThe results clearly show that while both algorithms perform well on random data, the Deterministic Quicksort suffers from catastrophic performance degradation (O(n2)) on sorted and reverse-sorted data. In contrast, Randomized Quicksort maintains its efficient O(nlogn) performance across all data distributions, proving it is a much more robust choice.Part 2: Interactive Hash TableThis script launches an interactive command-line menu to perform insert, search, and delete operations on a hash table.Run the script (No external dependencies required):python assignment3p2.py
python assignment3p2.py

--- Hash Table Menu ---
1. Insert a key-value pair
2. Search for a key
3. Delete a key
4. Print the current hash table
5. Create an example table
6. Exit
Enter your choice (1-6): 5

--- Example Table Created ---
Bucket 0:
  -> ('fig': 60)
Bucket 1:
 Empty
...
Bucket 9:
  -> ('apple': 10)
---------------------------


--- Hash Table Menu ---
...
Enter your choice (1-6): 1
Enter the key: 4
Enter the value: AV

--- Load factor exceeded. Resizing from 10 to 20... ---
Inserted ('4': AV).

--- Hash Table Menu ---
...
Enter your choice (1-6): 2
Enter the key to search for: 4
Value for '4' is: AV

--- Hash Table Menu ---
...
Enter your choice (1-6): 6

--- Final Hash Table State ---
Total items (size): 10
Table capacity: 20
Final load factor: 0.50
------------------------------
Exiting the program. Goodbye!

