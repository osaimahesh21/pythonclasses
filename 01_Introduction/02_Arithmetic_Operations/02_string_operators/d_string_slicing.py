"""
Purpose: String slicing operations
"""
language = "Python Programming"

# P   y  t  h  o n   P r o g  r  a  m  m  i  n  g
# 0   1  2  3  4 5 6 7 8 9 10 11 12 13 14 15 16 17   - forward indexing
# -18                                    -3 -2 -1    - reverse indexing


# String Slicing [start_index:final_index, step]
# default start_index = 0
# default final_index = string length
# default step = +1

def reverse_words(sentence):
    """
    Reverse each word in the given sentence while maintaining the same order.
    
    Args:
    - sentence (str): The input sentence.
    
    Returns:
    - str: The sentence with each word reversed.
    """
    # Split the sentence into individual words
    words = sentence.split()
    
    # Initialize an empty list to store the reversed words
    reversed_words = []
    
    # Iterate through each word in the list of words
    for word in words:
        # Reverse the current word and append it to the list of reversed words
        reversed_word = word[::-1]
        reversed_words.append(reversed_word)
    
    # Join the reversed words back into a single sentence
    reversed_sentence = ' '.join(reversed_words)
    
    return reversed_sentence

# Example usage:
input_sentence = "today is good day"
output_sentence = reverse_words(input_sentence)
print("Input sentence:", input_sentence)
print("Output sentence:", output_sentence)
