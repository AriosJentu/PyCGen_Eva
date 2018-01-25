available = "$AVAILABLE$"
randomized = "$RANDOMIZED$"
hashstring = "$HASHSTRING$"
rand_ord = '$RANDORD$'

from random import randint as rand

def get_sum(value):
	sums = 0

	for k, v in enumerate(value):
		sums += ord(v)+k

	return sums

def get_activation(request):

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

	ln = len(oldstr)

	if hashstring[pos:pos+ln] != oldstr:
		return False

	sumsr = 0
	for k, v in enumerate(oldstr):
		sumsr += ord(v) + k + pos

	sums = get_sum(hashstring)
	sumsr = sums-sumsr 

	sumsr = "%.4x"%sumsr

	codestr = ""
	for k, v in enumerate(sumsr):
		codestr += randomized[int(v, 16)+k]

	rand_size = rand(40, 50)
	rand_pos = rand(0, rand_size)
	
	newstr = str(randomized[rand_pos])
	for i in range(rand_size):
		if i == rand_pos:
			newstr += codestr
		elif not (rand_pos < i < rand_pos+4):
			newstr += randomized[rand(0, len(randomized)-1)]

	return newstr
