def is_pangram(sentence):
    return all(
        letter in sentence.lower()
        for letter in 'abcdefghijklmnopqrstuvwxyz'
        )
