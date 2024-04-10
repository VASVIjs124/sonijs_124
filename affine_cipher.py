from random import randint  # Importing the random integer function from the 'random' module
import math              # Importing the 'math' module

# Affine Cipher Encryption Function                                          
# This function takes in two parameters (a, b) and a message to be encrypted. 
def affine_encrypt(message, a, b):

    # Initialize an empty cipher message                                      
    # A variable 'cipher' is created to store the encrypted message.
    cipher = ""

    # Convert the message to lowercase and remove any non-alphabetic characters 
    message = [char.lower() for char in message if char.isalpha()]
    # The given message is converted to lowercase and all non-alphabetic characters are removed.
    # The resulting list is stored in the 'message' variable for further processing.

    # m is the number of letters in the alphabet, which is 26 in English
    m = 26
    # Here, 'm' is used in the encryption formula to represent the total number of letters in the alphabet.

    # Encrypt the message
    # The function iterates over each character in the 'message' list, performing the affine encryption.
    for char in message:
        if char.isalpha():

            # Map each letter to a number between 0 and 25
            # The 'ord()' method converts the given character to its corresponding ASCII value.
            # By subtracting the ASCII value of 'a', the function maps the alphabet characters to a consistent range (0-25).
            char_num = ord(char) - ord('a')

            # Apply the affine cipher formula
            # The encryption formula is 'ciphertext_num = (a * char_num + b) % m'
            # The result of the operation is again mapped to the range of (0-25) using the modulo operation (%) with 'm'.
            ciphertext_num = (a * char_num + b) % m

            # Map the encrypted number back to a letter
            # The 'chr()' method converts the 'ciphertext_num' to its corresponding ASCII value.
            # By adding the ASCII value of 'a', the function maps the number back to the corresponding alphabet character.
            cipher += chr(ciphertext_num + ord('a'))

        else:
            # If the character is not alphabetic, append it to the cipher message without encryption
            # Non-alphabetic characters are not affected by the encryption process and are added directly to the cipher.
            cipher += char

    # Return the encrypted message
    return cipher


# Affine Cipher Decryption Function
# 
# This function is designed to decrypt messages that have been encrypted using the Affine Cipher encryption method.
# 
# Parameters:
#   cipher (str): The encrypted message to be decrypted.
#   a (int): The first parameter of the Affine Cipher encryption method. Must be a positive integer and not divisible by 26.
#   b (int): The second parameter of the Affine Cipher encryption method. Must be a positive integer less than 26.
# 
# Returns:
#   str: The decrypted message.
# 
def affine_decrypt(cipher, a, b):
    # Initialize an empty decrypted message
    msg = ""
    
    # Convert the cipher message to lowercase and remove any non-alphabetic characters
    # This is done to ensure that the decryption works only with alphabetic characters (both lower and upper case)
    cipher = [char.lower() for char in cipher if char.isalpha()]
    
    # m is the number of letters in the alphabet, which is 26 in English
    m = 26
    
    # Calculate the inverse of a (mod m)
    # This is necessary to decrypt the message using the Affine Cipher decryption method
    a_inverse = pow(a, -1, m)
    
    # Decrypt the cipher message
    # For each letter in the cipher message, apply the inverse affine cipher formula
    for char in cipher:
        if char.isalpha():
            # Map each letter to a number between 0 and 25
            # This is necessary to perform the mathematical operations using the numerical representation of the characters
            char_num = ord(char) - ord('a')
            
            # Apply the inverse affine cipher formula
            # The inverse Affine Cipher decryption method is defined as: (a_inverse * (letter_num - b)) % m
            msg_num = (a_inverse * (char_num - b)) % m
            
            # Map the decrypted number back to a letter
            # This is necessary to convert the numerical representation of the character back to its corresponding letter
            msg += chr(msg_num + ord('a'))
                
        else:
            # If the character is not alphabetic, append it to the decrypted message without decryption
            # This is necessary to ensure that any non-alphabetic characters in the original message are preserved in the decrypted message
            msg += char
    
    return msg


# This function generates a key for the RSA encryption algorithm.
# 
# Args:
#   m (int): The integer value of the modulus.
#
# Returns:
#   (a, b, m) (tuple): A tuple containing the public key (a) and private key (b) along with the modulus (m).
#
# The function uses the `randint` function from the `random` module to generate random integers.
# It ensures that the public key (a) is co-prime to the modulus (m) by checking the great common divisor (gcd) of the two values.
# If the gcd is not 1, it means that the two values are not co-prime, and the function generates a new random value.
# The private key (b) is a random integer in the range of [0, m-1].
#
# Example:
#   generate_key(17) -> (13, 6, 17)
#
# Raises:
#   None
def generate_key(m):
    a = randint(1, m - 1)
    while (math.gcd(a, m) != 1):
        a = randint(1, m - 1)

    b = randint(0, m - 1)

    return (a, b, m)


# Main function:
#   1. Get user input for the secret message
#   2. Generate an Affine Cipher key
#   3. Encrypt the message using the key
#   4. Decrypt the encrypted message using the same key
#   5. Check if the decrypted message matches the original message
#      - If yes, print the message "Correct decryption achieved!"
#         and exit the loop
#   6. If the decrypted message does not match, go back to step 2
#         and generate a new key to try again
def main():
    message = input("Enter your secret message: ")

    while True:
        key = generate_key(26)

        encrypted_message = affine_encrypt(message, key[0], key[1])

        print("Encrypted message: ", encrypted_message)

        decrypted_message = affine_decrypt(encrypted_message, key[0], key[1])

        print("Decrypted message: ", decrypted_message)

        if decrypted_message == message:
            print("Correct decryption achieved!")
            break


# If the script is run as the main program, run the 'main()' function
if __name__ == "__main__":
    main()