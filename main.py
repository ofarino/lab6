
def encode_password(): # Kristian LaPlante Encoder
	global encoded_password
	password = input("Please enter your password to encode: ")
	encoded_password = ""
	for char in password:
		encoded_char = str((int(char) + 3) % 10) #  % 10  to avoid 1212
		encoded_password += encoded_char
	print("Your password has been encoded and stored!")


def decode(encoded_password):  # Olivia Farino decoder
	original = ""
	for digit in encoded_password:
		decoded_digit = str((int(digit) - 3) % 10)
		original += decoded_digit

	return original


while True: # Kristian LaPlante Main 
	print("Menu\n-------------") 
	print("1. Encode")
	print("2. Decode")
	print("3. Quit")
	option = input("Please enter an option: ")
	
	if option == "1":
		encode_password()
	elif option == "2":
		original_password = decode(encoded_password)
		print(f"The encoded password is {encoded_password}, and the original password is {original_password}.")
	elif option == "3":
		break
	else:
		print("Invalid option. Please select a valid option (1, 2, or 3).")
