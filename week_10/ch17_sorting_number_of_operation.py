import matplotlib.pyplot as plt
import numpy as np

# Define the list size
n = np.arange(1, 101, 1)

# Define the number of operations for each algorithm's case
insertion_best = n
insertion_worst = n**2

merge_best_worst = n * np.log2(n)

quick_best = n * np.log2(n)
quick_worst = n**2

# Set up the plotting area
plt.figure(figsize=(12, 8))

# Insertion Sort
plt.fill_between(n, insertion_best, insertion_worst, color='skyblue', alpha=0.5, label='Insertion Sort Best-Worst')

# Merge Sort
plt.plot(n, merge_best_worst, color='green', alpha=1, label='Merge Sort Best-Worst')

# Quick Sort
slice = int(len(n)*0.9)
plt.fill_between(n[:slice], quick_best[:slice], quick_worst[:slice], color='salmon', alpha=0.2, label='Quick Sort Best-Worst')

# Titles and Labels
plt.title('Number of Operations for Sorting Algorithms (Best vs Worst Case)')
plt.xlabel('List Size (n)')
plt.ylabel('Number of Operations')
plt.legend()
plt.yscale('log')  # Set the y-axis to a logarithmic scale for better visualization

# Show the plot
plt.grid(True)
plt.show()
