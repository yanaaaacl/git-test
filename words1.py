def search4vowels(word):
    # Выводит гласные, найденные во введенном слове.
    vowels = {"a", "e", "i", "o", "u"}  
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)
a = "hello"
search4vowels(a)


