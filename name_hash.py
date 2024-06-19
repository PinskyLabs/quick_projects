import hashlib

name = input("Enter your name: ")
name_list = list(name)

# Convert each character to a SHA-256 hash and store in a list
hash_list = [hashlib.sha256(char.encode()).hexdigest() for char in name_list]

# Concatenate the hashes into a single string
concatenated_hashes = ''.join(hash_list)

# Compute the SHA-256 hash of the concatenated string
final_hash = hashlib.sha256(concatenated_hashes.encode()).hexdigest()

print(final_hash)
