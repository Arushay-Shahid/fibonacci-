#a series of numbers in which each number ( Fibonacci number ) is the sum of the two preceding numbers. The simplest is the series 1, 1, 2, 3, 5, 8, etc.
# Input from the user for the number of terms
n = int(input("Enter the number of terms: "))

# First two terms of the Fibonacci series
a, b = 0, 1

# Print the Fibonacci series
print("Fibonacci series:")
for _ in range(n):
    print(a, end=" ")
    # Update a and b for the next term
    a, b = b, a + b
