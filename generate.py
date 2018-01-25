from string import ascii_letters as letters, digits
from random import randint as rand, choice

sfnd = True
afnd = True

try:
	import server
except:
	sfnd = False

try:
	import activation
except:
	afnd = False

subletters = "=*+-&^"
available = letters+digits+subletters
DEF_LEN = 260

chooser = -1
while chooser != 0:

	print("=-------------------------------------------=")
	print("Python Code Activation generator")
	print("=-------------------------------------------=")
	print("[?] Select option:")
	print("[1] Generate main files")
	print("[2] Generate request-code")
	print("[3] Generate activation code by request-code")
	print("[4] Check activation code for validity")
	print("[~]")
	print("[0] Exit")

	chooser = input("Input: ")

	try:
		chooser = int(chooser)

	except:
		chooser = -1


	print("=-------------------------------------------=")

	if chooser == 1:
	
		print()
		print("[!] Generating randomized alphabet")

		randomized = list(available)

		for i in range(rand(1, 100)):
			x = rand(1, len(randomized)//2)
			y = rand(len(randomized)//2, len(randomized)-1)
			randomized[x], randomized[y] = randomized[y], randomized[x]
			randomized = randomized[x:]+randomized[:x]

		randomized = "".join(randomized)
		print("[!] Alphabet generated")

		print("")

		print("[!] Generating Hash String")

		hashstring = ""
		for i in range(DEF_LEN):
			hashstring += choice(available)

		print("[!] Hash String generated")
		
		print()

		print("[!] Generating Random Shifting Number")
		rand_ord = rand(10, 50)
		print("[!] Random Shifting Number generated")

		print()

		print("[!] Generating Activation.Py file")

		with open("templates/activation.py", "r") as activ_from, open("activation.py", "w") as activ_to:

			print(" [~] Reading content")
			content = activ_from.read()
			content = content.replace("$AVAILABLE$", available)
			content = content.replace("$RANDOMIZED$", randomized)
			content = content.replace("$HASHSTRING$", hashstring)
			content = content.replace("'$RANDORD$'", str(rand_ord))
			print(" [~] Writing content")
			activ_to.write(content)
			print(" [~] Content has been written")

		print("[!] Activation.Py file generated")
		print()

		print("[!] Generating Server.Py file")

		with open("templates/server.py", "r") as server_from, open("server.py", "w") as server_to:

			print(" [~] Reading content")
			content = server_from.read()
			content = content.replace("$AVAILABLE$", available)
			content = content.replace("$RANDOMIZED$", randomized)
			content = content.replace("$HASHSTRING$", hashstring)
			content = content.replace("'$RANDORD$'", str(rand_ord))
			print(" [~] Writing content")
			server_to.write(content)
			print(" [~] Content has been written")

		print("[!] Server.Py file generated")
		print()

		print("[!] Generating Server.Lua file")

		with open("templates/server.lua", "r") as server_from, open("server.lua", "w") as server_to:

			print(" [~] Reading content")
			content = server_from.read()
			content = content.replace("$AVAILABLE$", available)
			content = content.replace("$RANDOMIZED$", randomized)
			content = content.replace("$HASHSTRING$", hashstring)
			content = content.replace("'$RANDORD$'", str(rand_ord))
			print(" [~] Writing content")
			server_to.write(content)
			print(" [~] Content has been written")

		print("[!] Server.Lua file generated")
		print()

		print("[!] Finished")

	elif chooser == 2:

		try:
			import server
			sfnd = True
		except:
			sfnd = False

		if sfnd:
			print()
			print("[!] Import Server.Py file")
			from server import get_request

			print("[~] Your Request Code:")
			print("=-------------------------------------------=")
			print(get_request())
			print("=-------------------------------------------=")
			print("[~]")
			print()

		else:

			print("[!] Server.Py file not found")
			print()

			print("[!] Successfully Imported")

		print("[!] Finished")

	elif chooser == 3:

		try:
			import activation
			afnd = True
		except:
			afnd = False

		if afnd:
			print()
			print("[!] Import Activation.Py file")
			from activation import get_activation
		
			print("[!] Successfully Imported")
			print()
			print("[?] Enter Your Request Code:")
			request = input("Input: ")
			print()
			print("[~] Your Activation Code:")
			print("=-------------------------------------------=")
			print(get_activation(request))
			print("=-------------------------------------------=")
			print("[~]")
			print()

		else:

			print("[!] Activation.Py file not found")
			print()

		print("[!] Finished")

	elif chooser == 4:

		try:
			import server
			sfnd = True
		except:
			sfnd = False
			
		if sfnd:
			print()
			print("[!] Import Server.Py file")
			from server import check_activation_code

			print("[!] Successfully Imported")

			print()
			print("[?] Enter Your Request Code:")
			request = input("Input: ")
			print()

			print()
			print("[?] Enter Your Activation Code:")
			activation = input("Input: ")
			print()
			print("[~] Your Request Code:")
			print("=-------------------------------------------=")
			print(check_activation_code(request, activation))
			print("Code Is Correct" if check_activation_code(request, activation) == True else "Invalid Code")
			print("=-------------------------------------------=")
			print("[~]")
			print()
		
		else:

			print("[!] Server.Py file not found")
			print()

		print("[!] Finished")
	
	print()
