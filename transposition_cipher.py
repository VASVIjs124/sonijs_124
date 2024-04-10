import math

key = input("Enter the key: ")

# Function to encrypt a message using the Playfair cipher
# Encryption
def encryptMessage(msg):
	cipher = ""  # Initialize an empty encrypted cipher
	
	k_indx = 0 # Initialize a variable to track key indices

	msg_len = float(len(msg))  # Calculate length of msg in float data type
	msg_lst = list(msg) # Convert the message into a list
	key_lst = sorted(list(key)) # Sort the key

	col = len(key) # calculate column of the matrix
	
	row = int(math.ceil(msg_len / col)) # calculate maximum row of the matrix

	fill_null = int((row * col) - msg_len) # Calculate the number of padding characters needed
	msg_lst.extend('_' * fill_null) # add the padding character '_' in empty 

	matrix = [msg_lst[i: i + col] # create Matrix and insert message and padding characters row-wise 
			for i in range(0, len(msg_lst), col)]

	for _ in range(col): # read matrix column-wise using key
		curr_idx = key.index(key_lst[k_indx])
		cipher += ''.join([row[curr_idx] 
						for row in matrix])
		k_indx += 1

	return cipher

# Decryption
def decryptMessage(cipher):
	msg = ""  # Initialize an empty decrypted message
	
	k_indx = 0 # track key indices

	msg_indx = 0 # track msg indices
	msg_len = float(len(cipher))
	msg_lst = list(cipher) # Convert the cipher into a list
	
	col = len(key) # calculate column of the matrix
	
	row = int(math.ceil(msg_len / col)) # calculate maximum row of the matrix

	key_lst = sorted(list(key)) # convert key into list and sort alphabetically so we can access each character by its alphabetical position.

	dec_cipher = [] # create an empty matrix to store deciphered message
	for _ in range(row):
		dec_cipher += [[None] * col]

	for _ in range(col): # Arrange the matrix column wise according to permutation order by adding into new matrix
		curr_idx = key.index(key_lst[k_indx])

		for j in range(row):
			dec_cipher[j][curr_idx] = msg_lst[msg_indx]
			msg_indx += 1
		k_indx += 1

	# convert decrypted msg matrix into a string
	try:
		msg = ''.join(sum(dec_cipher, []))
	except TypeError:
		raise TypeError("This program cannot handle repeating words.")

	null_count = msg.count('_')

	 # Remove null characters from the end of the message
	if null_count > 0:
		return msg[: -null_count]

	return msg

# Driver Code
msg = input("Enter the message: ") # Read the plain text message from user input

# Encrypt the message and print the encrypted cipher text
cipher = encryptMessage(msg) 
print("Encrypted Message: {}". format(cipher))

# Decrypt the cipher text and print the decrypted message
decrypted_msg = decryptMessage(cipher)
print("Decryped Message: {}". format(cipher))