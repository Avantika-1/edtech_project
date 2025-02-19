# Function to find the maximum of three amounts
def find_maximum(Mob1, Mob2, Mob3):
    return max(Mob1, Mob2, Mob3)

# Taking user input for the three amounts
Mob1 = float(input("Enter the first amount: "))
Mob2 = float(input("Enter the second amount: "))
Mob3 = float(input("Enter the third amount: "))

# Finding and displaying the maximum amount
max_amount = find_maximum(Mob1, Mob2, Mob3)
print(f"The maximum amount is: {max_amount}")
