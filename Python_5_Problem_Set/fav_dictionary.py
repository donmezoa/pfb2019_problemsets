#!/usr/bin/env python3

# Defining dictionary of fav things
fav_dict = { 'book' : 'Eragon' ,
	'song' : 'Macklamore' ,
	'tree' : 'Sycamore' } 

# Print favorite book
print(fav_dict['book'])

# Define and print favorite book
fav_thing = 'book'
print(fav_dict[fav_thing])

# Print favorite tree
print(fav_dict['tree'])

# Add fav organism to dictionary
fav_dict['organism'] = 'plant'
print(fav_dict['organism'])

# Print dictionary keys
print(fav_dict.keys())

# Change fav organism
fav_dict['organism'] = 'orchid'
print(fav_dict['organism'])

# Print key value with for loop
for key in fav_dict:
	value = fav_dict[key]
	print(key, value)

