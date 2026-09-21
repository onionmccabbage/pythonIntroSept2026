# we have met many collections in Python
# string, tuple, list, dict
# [] for list, () for tuple, {} for dict or set
# the set collection is a non-ordinal collection of unique values

s = {1, 2, 5, 3, 4, 3, 5}
s.add(6)
s.add(-6)
s.add(False)
s.add(6)
s.remove(5)
print(s, type(s))

