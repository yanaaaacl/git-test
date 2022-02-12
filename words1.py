def search4vowels(word):
    # Выводит гласные, найденные во введенном слове.
    vowels = {"a", "e", "i", "o", "u"}  
    return vowels.intersection(set(word))
a = "hello"
print(search4vowels(a))


def search4letters(word, letters):
    return set(letters).intersection(set(word))
d = "hello"
b = "aetyuohjgfkfjrfv"
print(search4letters(d, b))

