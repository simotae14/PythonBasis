# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Simple tuple
fruit_tuple = ('Apple', 'Orange', 'Mango')
# using constructor
#fruit_tuple = tuple(('Apple', 'Orange', 'Mango'))

# Get single value
#print(fruit_tuple[1])

# Can not change value
#fruit_tuple[1] = 'Grape'

# Tuples with one value should have a trailing comma
fruit_tuple_2 = ('Apple',)

del fruit_tuple_2

# Get length of tuple
#print(len(fruit_tuple_2))
# A Set is a collection which is unordered and unindexed. No duplicate members.
# Create set

fruit_set = { 'Apple', 'Orange', 'Mango', 'Apple' }

# Check if in set
print('Apple' in fruit_set)

# Add to set
fruit_set.add('Grape')

# Remove from set
fruit_set.remove('Grape')

# Clear set
fruit_set.clear()

# delete Set
del fruit_set

print(fruit_set)
