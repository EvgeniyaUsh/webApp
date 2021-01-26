def search4letters(phrase, letter='aiueo'):
    return set(phrase).intersection(set(letter))
