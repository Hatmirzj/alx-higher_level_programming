(sentence):
    if 0 == len(sentence):
        return 0, None
    return len(sentence), sentence[0]
