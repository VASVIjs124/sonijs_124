# This script implements the Caesar Cipher algorithm for encryption and decryption
# Caesar Cipher is a type of substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet
# In this implementation, the shift is determined by the length of the hash input by the user

def caesar_encrypt(key, message):
    # Encrypt the message using Caesar Cipher with the given key
    # key: the number of shifts in the alphabet (integer)
    # message: the message to be encrypted (string)
    # returns: the encrypted message (string)

    encrypted = ""  # Initialize an empty string to store the encrypted message
    for char in message:
        # Iterate through each character in the message
        if char.isalpha():
            # If the character is a letter, shift it by the key value
            shift = key % 26  # Ensure the shift is within the alphabet range (0-25)
            if char.islower():
                # If the character is lowercase, shift accordingly
                encrypted += chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
            else:
                # If the character is uppercase, shift accordingly
                encrypted += chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
        else:
            # If the character is not a letter, keep it as is
            encrypted += char
    return encrypted

def caesar_decrypt(key, message):
    # Decrypt the message using Caesar Cipher with the given key
    # key: the number of shifts in the alphabet (integer)
    # message: the message to be decrypted (string)
    # returns: the decrypted message (string)

    decrypted = ""  # Initialize an empty string to store the decrypted message
    for char in message:
        # Iterate through each character in the message
        if char.isalpha():
            # If the character is a letter, shift it by the inverse of the key value
            shift = key % 26  # Ensure the shift is within the alphabet range (0-25)
            if char.islower():
                # If the character is lowercase, shift accordingly
                decrypted += chr((ord(char) - ord("a") - shift) % 26 + ord("a"))
            else:
                # If the character is uppercase, shift accordingly
                decrypted += chr((ord(char) - ord("A") - shift) % 26 + ord("A"))
        else:
            # If the character is not a letter, keep it as is
            decrypted += char
    return decrypted

# Get user inputs
hash = input("Enter the hash: ")
key = len(hash)  # Determine the key based on the length of the hash
message = input("Enter the message: ")

# Encrypt the message
encrypted = caesar_encrypt(key, message)
print("Encrypted message:", encrypted)

# Decrypt the encrypted message
decrypted = caesar_decrypt(key, encrypted)
print("Decrypted message:", decrypted)