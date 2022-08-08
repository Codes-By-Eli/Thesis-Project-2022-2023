import nltk

sen = "I love my family"

tokenized = nltk.tokenize.word_tokenize(sen)

group = nltk.pos_tag(tokenized)

total_words = 0

for el in group:
    print(el[1])
    total_words += 1

print(total_words)