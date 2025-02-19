# string = "The apple is red"..
#output dict should be the the letter and the frequency..
#output dic = {"t":1, "h" : 1, "e": 3, "a":1,"p":2,"l":1,"r":1,"d":1}

from collections import Counter

def letter_frequency(s):
    s = s.replace(" ", "").lower()  # Remove spaces and convert to lowercase
    return dict(Counter(s))

# Example usage:
string = "The apple is red"
frequency_dict = letter_frequency(string)
print(frequency_dict)
