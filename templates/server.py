available = "$AVAILABLE$"
randomized = "$RANDOMIZED$"
hashstring = "$HASHSTRING$"
rand_ord = '$RANDORD$'

from random import randint as rand
DEF_LEN = 260

def get_sum(value):
	sums = 0

	for k, v in enumerate(value):
		sums += ord(v)+k

	return sums

def get_request():

	strlen = rand(50, 80)

	pos = rand(1, DEF_LEN-strlen)
	substr = hashstring[pos:pos+strlen]
	rand_ord_local = rand(1, rand_ord)
	
	moved_av = "".join([randomized[i+rand_ord_local] for i in range(-len(randomized), 0)])

	newstr = ""
	for i in substr:
		newstr += moved_av[randomized.index(i)]

	return randomized[rand_ord_local] + "%.2x"%pos + newstr

def check_activation_code(request, activation):

	if not request[0] in randomized or len(request) <= 10:
		return False

	try:
		int(request[1:3], 16)
	except:
		return False

	rand_ord_local = randomized.index(request[0])
	pos = int(request[1:3], 16)

	moved_av = "".join([randomized[i+rand_ord_local] for i in range(-len(randomized), 0)])

	oldstr = ""
	for i in request[3:]:
		oldstr += randomized[moved_av.index(i)]

	# print("---")
	# print(oldstr)
	# print("---")
		
	ln = len(oldstr)
	if hashstring[pos:pos+ln] != oldstr:
		return False

	sumsr = 0
	for k, v in enumerate(oldstr):
		sumsr += ord(v) + k + pos

	sums = get_sum(hashstring)
	sumsr = sums-sumsr 

	actpos = randomized.index(activation[0])+1

	code = activation[actpos:actpos+4]

	hexad = ""
	for i in range(len(code)):
		hexad += "%x"%(randomized.index(code[i])-i)

	try:
		int(hexad, 16)
	except:
		return False

	sumnstrlen = randomized.index(activation[-1])
	sumstr = activation[-(sumnstrlen+1):-1]
	strsum = int("".join([str(randomized.index(i)) for i in sumstr]))
	print("|~", sumnstrlen, sumstr, strsum, get_sum(activation[:-(sumnstrlen+1)]), "~|")

	return int(hexad, 16) == sumsr and strsum == get_sum(activation[:-(sumnstrlen+1)])

