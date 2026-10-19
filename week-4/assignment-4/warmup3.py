# Create two hardcoded lists of programming languages (some overlap, some unique to each list). Convert each to a set and print:
# The union (all languages from both lists, no duplicates)
# The intersection (languages in both lists)
# The difference (languages only in the first list)


first_language_list = ["Python", "C#", "C++", "Java", "PHP"]
second_language_list = ["C#", "Java", "PHP","JavaScript", "Go"]

first_language_set = set (first_language_list)
second_language_set = set (second_language_list)

print (first_language_set)
print (second_language_set)
print (first_language_set.union(second_language_set))
print (first_language_set.intersection(second_language_set))
print (first_language_set.difference(second_language_set))
