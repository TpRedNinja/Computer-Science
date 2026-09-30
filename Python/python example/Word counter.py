# This program will count how many words are in a sentence you specify

sentence = input('Enter a Sentence here: ')
sentence = sentence.split()
total_words = len(sentence)
print(f'This sentence has {total_words} total words in it')

