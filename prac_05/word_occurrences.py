"""
Word Occurrences
Estimate: 20 minutes
Actual:   30 minutes
"""
text = input("Text: ")
words = text.split(" ")
word_count = {}

for i in words:
    if i not in word_count:
        word_count[i] = 1
    else:
        word_count[i] += 1
        
max_word_length = max([len(i) for i in word_count])
word_count_sorted = sorted(word_count.items())

for word,count in word_count_sorted:
    print(f"{word:<{max_word_length}} : {count}")