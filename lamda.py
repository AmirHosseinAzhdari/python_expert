# ananimous functions and single use
# we can't use other functions in lambda
# in common we use lambda with map, filter, reduce, sort
f = lambda a: a * a
print(f(5))

# sorting list of tuples
list1 = [("egg", 5.25), ("honey", 1.25), ("carrots", 3.5), ("peaches", 2.45)]
list1.sort(key=lambda a: a[0])
print(list1)

# sorting list of dictionaries
list2 = [
    {"key": 255, "year": 2005},
    {"key": 600, "year": 1999},
    {"key": 189, "year": 2008},
]
a = sorted(list2, key=lambda a: a["year"])
print(a)

# filtering a list of integers
list3 = [2, 4, 52, 2, 5, 2, 5, 25]
list3 = list(filter(lambda a: a % 2 == 0, list3))
print(list3)

# lambda for a list using map
list4 = [2, 4, 52, 2, 5, 2, 5, 252]
list4 = list(map(lambda a: a**2, list4))
print(list4)

# lambda conditions
start_with_a = lambda a: True if a.startswith("a") else False
print(start_with_a("hasan"))
print(start_with_a("amir"))

word_before = lambda s, w: s.split()[s.split().index(w) - 1] if w in s else None
sentence = "Four score and seven years ago"
print(word_before(sentence, "seven"))
