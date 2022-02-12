def search4vowels(word):
    # Выводит гласные, найденные во введенном слове.
    vowels = {"a", "e", "i", "o", "u"}  
    found = vowels.intersection(set(word))
    return bool(found)
a = "hello"
print(search4vowels(a))


