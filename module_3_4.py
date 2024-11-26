def single_root_words (root_word, *other_words):
    unswer = []
    for word in other_words:
        if word.lower().find(root_word.lower()) != -1 or root_word.lower().find(word.lower()) != -1:
            unswer.append(word)
    return unswer

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
