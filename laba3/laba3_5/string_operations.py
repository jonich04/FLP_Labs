def find_longest_word(sentence):
    return max(sentence.split(), key=len)
