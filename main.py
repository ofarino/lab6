
def encode_password(): # Kristian LaPlante Encoder
	global encoded_password
	password = input("Please enter your password to encode: ")
	encoded_password = ""
	for char in password:
		encoded_char = str((int(char) + 3) % 10) #  % 10  to avoid 1212
		encoded_password += encoded_char
	print("Your password has been encoded!")

while True: # Kristian LaPlante Main 
	print("Menu\n-------------") 
	print("1. Encode")
	print("2. Decode")
	Print("3. Quit")
	option = input("Please enter an option: ")
	
	if option == "1":
		encode_password()
	elif option == "2":
		#decode_password()
		break
	elif option == "3":
		break
	else:
		print("Invalid option. Please select a valid option (1, 2, or 3).")
