# we may generate values to be used in our work
r = range(0, 10**2, 5)

# We may declare a generator (to generate values on demand)
g = (i**2 for i in r)
# However, we may need the values to exist in memory
l = [i**2 for i in r] # this is list comprehension

print(g) # the generator object exists in memory
print(l)
# we may use the generator in any context e.g. a loop
# for _ in g:
#     if _ <= 10000:
#         print(_)
#     else:
#         break # maybe we break out of the loop