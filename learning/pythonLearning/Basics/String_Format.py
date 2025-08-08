#we cannot combine strings and numbers like this:
"""
age = 36
txt = "My name is John, I am " + age
print(txt)
"""

#we use F-string to combine str and numbers

#To specify a string as an f-string,
#simply put an f in front of the string literal,
#and add curly brackets {} as placeholders for variables and other operations.
age = 31 #Placeholder
txt = f"My name is john, I am {age}"
print(txt)

#A placeholder can contain variables, operations, functions,
# Modifier -modifiers to format the value.
price = 59
txt = f"The price is {price:.2f} dollars"  #here we use modifier as :.2f to add .00 in o/p
print(txt)

txt = f"The price is {20 * 59} dollars"
txt = f"The price is {20 * 59:.2f} dollars"
print(txt)
