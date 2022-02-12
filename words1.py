def search4vowels(word):
    # Выводит гласные, найденные во введенном слове.
    vowels = {"a", "e", "i", "o", "u"}  
    return vowels.intersection(set(word))
a = "hello"
print(search4vowels(a))


