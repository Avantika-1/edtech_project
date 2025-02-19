def letter_frequency(s):
    s = s.replace(" ", "").lower()  # Remove spaces and convert to lowercase
    freq_dict = {}
    for char in s:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    return freq_dict

# Example usage:
string = "The apple is red"
frequency_dict = letter_frequency(string)
print(frequency_dict)
