import hashlib

name = input("Enter your name: ")
name_list = list(name)

# Converting each letter to a hash and put it in a list
hash_list = [hashlib.sha256(char.encode()).hexdigest() for char in name_list]

# Concatenate the hashes into a single string
concatenated_hashes = ''.join(hash_list)

# Finding the hash of the concatenated string
final_hash = hashlib.sha256(concatenated_hashes.encode()).hexdigest()

print(final_hash)
