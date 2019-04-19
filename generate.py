from string import ascii_letters as letters, digits
from random import randint as rand, choice
import os

sfnd = True
afnd = True

try:
	import build.server
except:
	sfnd = False

try:
	import build.activation
except:
	afnd = False

subletters = "=*+-&^"
available = letters+digits+subletters
DEF_LEN = 260

class Col:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

	def info(string):
		return Col.OKBLUE+Col.BOLD+string

	def menu(string):
		return Col.OKGREEN+Col.BOLD+string

	def substr(string):
		return Col.HEADER+Col.BOLD+string

	def input(string):
		return Col.WARNING+Col.BOLD+string

	def err(string):
		return Col.FAIL+Col.BOLD+string

chooser = -1
while chooser != 0:

	print(Col.info("=-------------------------------------------="))
	print(Col.info("Python Code Activation generator"))
	print(Col.info("=-------------------------------------------="))
	print(Col.substr("[?] ") + Col.err("Select option:"))
	print(Col.menu("[1] ") + Col.info("Generate main files"))
	print(Col.menu("[2] ") + Col.info("Generate request-code"))
	print(Col.menu("[3] ") + Col.info("Generate activation code by request-code"))
	print(Col.menu("[4] ") + Col.info("Check activation code for validity"))
	print(Col.substr("[~]"))
	print(Col.menu("[0] ") + Col.info("Exit"))

	chooser = input(Col.input("Input: "))

	try:
		chooser = int(chooser)

	except:
		chooser = -1


	print(Col.info("=-------------------------------------------="))

	if chooser == 1:

		if not os.path.exists('build'):
			os.makedirs('build')
	
		print()
		print(Col.input("[!] ") + Col.info("Generating randomized alphabet"))

		randomized = list(available)
		randlen = len(randomized)

		for i in range(rand(1, 100)):

			x = rand(1, randlen//2)
			y = rand(randlen//2, randlen-1)
			randomized[x], randomized[y] = randomized[y], randomized[x]
			randomized = randomized[x:]+randomized[:x]


		randomized = "".join(randomized)
		print(Col.input("[!] ") + Col.substr("Alphabet generated"))

		print()
		print(Col.input("[!] ") + Col.info("Generating Hash String"))

		hashstring = ""
		for i in range(DEF_LEN):
			hashstring += choice(available)


		print(Col.input("[!] ") + Col.substr("Hash String generated"))
		
		print()
		print(Col.input("[!] ") + Col.info("Generating Random Shifting Number"))

		rand_ord = rand(10, 50)
		print(Col.input("[!] ") + Col.substr("Random Shifting Number generated"))

		print()
		print(Col.input("[!] ") + Col.info("Generating Activation.Py file"))


		with open("templates/activation.py", "r") as activ_from, open("build/activation.py", "w") as activ_to:

			print(Col.substr(" [~] ") + Col.info("Reading content"))

			content = activ_from.read()
			content = content.replace("$AVAILABLE$", available)
			content = content.replace("$RANDOMIZED$", randomized)
			content = content.replace("$HASHSTRING$", hashstring)
			content = content.replace("'$RANDORD$'", str(rand_ord))

			print(Col.substr(" [~] ") + Col.info("Writing content"))
			activ_to.write(content)
			print(Col.substr(" [~] ") + Col.menu("Content has been written"))


		print(Col.input("[!] ") + Col.substr("Activation.Py file generated"))

		print()
		print(Col.input("[!] ") + Col.info("Generating Server.Py file"))

		with open("templates/server.py", "r") as server_from, open("build/server.py", "w") as server_to:

			print(Col.substr(" [~] ") + Col.info("Reading content"))

			content = server_from.read()
			content = content.replace("$AVAILABLE$", available)
			content = content.replace("$RANDOMIZED$", randomized)
			content = content.replace("$HASHSTRING$", hashstring)
			content = content.replace("'$RANDORD$'", str(rand_ord))

			print(Col.substr(" [~] ") + Col.info("Writing content"))
			server_to.write(content)
			print(Col.substr(" [~] ") + Col.menu("Content has been written"))


		print(Col.input("[!] ") + Col.substr("Server.Py file generated"))

		print()
		print(Col.input("[!] ") + Col.info("Generating Server.Lua file"))

		with open("templates/server.lua", "r") as server_from, open("build/server.lua", "w") as server_to:

			print(Col.substr(" [~] ") + Col.info("Reading content"))

			content = server_from.read()
			content = content.replace("$AVAILABLE$", available)
			content = content.replace("$RANDOMIZED$", randomized)
			content = content.replace("$HASHSTRING$", hashstring)
			content = content.replace("'$RANDORD$'", str(rand_ord))

			print(Col.substr(" [~] ") + Col.info("Writing content"))
			server_to.write(content)
			print(Col.substr(" [~] ") + Col.menu("Content has been written"))


		print(Col.input("[!] ") + Col.substr("Server.Lua file generated"))

		print()
		print(Col.menu("[!] ") + Col.info("Finished"))

	elif chooser == 2:

		try:
			import build.server
			sfnd = True
		except:
			sfnd = False

		if sfnd:

			print()
			print(Col.input("[!] ") + Col.info("Import Server.Py file"))

			from build.server import get_request
			print(Col.input("[!] ") + Col.menu("Successfully Imported"))

			print()
			print(Col.input("[~] ") + Col.substr("Your Request Code"))
			print(Col.info("=-------------------------------------------="))
			print(Col.input(get_request()))
			print(Col.info("=-------------------------------------------="))
			print(Col.input("[~] "))
			print()

		else:

			print(Col.substr("[!] ") + Col.err("Server.Py file not found"))
			print()
			continue

		print(Col.menu("[!] ") + Col.info("Finished"))

	elif chooser == 3:

		try:
			import build.activation
			afnd = True
		except:
			afnd = False

		if afnd:
			
			print()
			print(Col.input("[!] ") + Col.info("Import Activation.Py file"))
			
			from build.activation import get_activation
			print(Col.info("[!] ") + Col.menu("Successfully Imported"))
		
			print()
			print(Col.menu("[?] ") + Col.substr("Enter Your Request Code:"))
			request = input(Col.input("Input: "))
			
			print()
			print(Col.input("[~] ") + Col.substr("Your Activation Code"))
			print(Col.info("=-------------------------------------------="))
			print(Col.input(get_activation(request)))
			print(Col.info("=-------------------------------------------="))
			print(Col.input("[~] "))
			print()

		else:

			print(Col.substr("[!] ") + Col.err("Activation.Py file not found"))
			print()
			continue

		print(Col.menu("[!] ") + Col.info("Finished"))

	elif chooser == 4:

		try:
			import build.server
			sfnd = True
		except:
			sfnd = False
			
		if sfnd:
			print()
			print(Col.input("[!] ") + Col.info("Import Server.Py file"))
			from build.server import check_activation_code

			print(Col.info("[!] ") + Col.menu("Successfully Imported"))

			print()
			print(Col.menu("[?] ") + Col.substr("Enter Your Request Code:"))
			request = input(Col.input("Input: "))
			print()

			print()
			print(Col.menu("[?] ") + Col.substr("Enter Your Activation Code:"))
			activation = input(Col.input("Input: "))
			print()
			print(Col.input("[~] ") + Col.substr("Activation Status:"))
			print(Col.info("=-------------------------------------------="))
			#print(Col.input(str(check_activation_code(request, activation))))
			print(Col.info("Code Is Correct" if (check_activation_code(request, activation) == True) else "Invalid Code"))
			print(Col.info("=-------------------------------------------="))
			print(Col.input("[~] "))
			print()
		
		else:

			print(Col.substr("[!] ") + Col.err("Server.Py file not found"))
			print()
			continue

		print(Col.menu("[!] ") + Col.info("Finished"))
	
	print()
