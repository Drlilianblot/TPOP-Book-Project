def histogram(text):
    hist = dict()
    for character in text:
        if character not in hist:
            hist[character] = 1
        else:
            hist[character] += 1
    return hist


def print_histogram(hist):
    for character in hist:
        print(character, hist[character])


def reverse_lookup(dico, value):
    for key in dico:
        if dico[key] == value:
            return key
    raise ValueError('No such value in dictionary!')


def invert_dict(dico):
    inverted = dict()
    for key in dico:
        value = dico[key]
        if value not in inverted:
            inverted[value] = [key]
        else:
            inverted[value].append(key)
    return inverted
