"""
Word Occurrences
Estimate: 30 minutes
Actual:  15 minutes
"""
"""Count and display sorted, aligned word occurrences from user input."""
word_to_count = {}
text = input("Text: ")
words = text.split()

# Count occurrences of each word
for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1

# Sort the unique words alphabetically
sorted_words = sorted(word_to_count.keys())

# Find the length of the longest word for column alignment
max_length = max((len(word) for word in sorted_words), default=0)

# Print the aligned results
for word in sorted_words:
    print(f"{word:{max_length}} : {word_to_count[word]}")
