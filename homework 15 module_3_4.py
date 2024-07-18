def single_root_words(root_word, *other_words):
    same_words = []
    lower_rtw = root_word.lower()
    for i in other_words:
        lower_i = i.lower()
        if lower_rtw in lower_i or lower_i in lower_rtw:
            same_words.append(i)
    return same_words and print(same_words)


single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
