# Function to print diamond pattern
def print_diamond(n):
    # Upper half of the diamond
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))

    # Lower half of the diamond
    for i in range(n - 2, -1, -1):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))


# Example usage
n = 5  # Height of the diamond
print_diamond(n)
