def word_search(list, keyword):
    indices = []
    for token in list:
        token.lower()
        token.split()
        for word in token:
            keyword.lower()
            if word == keyword:
                indices.append(token.index(word))
    return indices


list = ['Hi how are you','hello world','never found you','helloewy']
keyword = 'Hello'
word_search(list,keyword)

