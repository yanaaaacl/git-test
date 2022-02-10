vowels = set("aeiou")
word = "hello"
u = vowels.union(set(word))
u_list = sorted(list(u))
d = vowels.difference(set(word))
i = vowels.intersection(set(word))
print(u_list)
print(d)
print(i)
