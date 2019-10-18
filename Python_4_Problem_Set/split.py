#!/usr/bin/env python3


# Script to split a string into a list

# Define the list
taxa = 'sapiens, erectus, neanderthalensis'

# Print taxa
print(taxa)

# Print the first second variable in taxa
print(taxa[1])

# Determine the what type taxa is
print(type(taxa))

# split into a list
species = taxa.split(',')

# Print species which is a list
print(species)

# Print the first variable is species
print(species[1])

# Determine what type species is
print(type(species))

# Sort the species alphabetically
species.sort()

# Print the new species list
print(species)


# Sort the species based upon word size
species.sort(key=len)

# Print the new species list
print(species)
