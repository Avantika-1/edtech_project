input_string = input("Enter a string: ")
count = sum(1 for char in input_string if char.lower() == 'i')
print(f"The letter 'a' appears {count} times in the string.")
