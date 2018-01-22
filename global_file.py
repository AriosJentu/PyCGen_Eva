from string import ascii_letters as letters, digits
from random import choice, randint as rand

#Объявляю переменные доступных символов
subletters = "=*+-&^"
available = letters+digits+subletters

randomized = list(available)
for i in range(rand(1, 100)):
	x = rand(1, len(randomized)//2)
	y = rand(len(randomized)//2, len(randomized)-1)
	randomized[x], randomized[y] = randomized[y], randomized[x]
	randomized = randomized[x:]+randomized[:x]

randomized = "".join(randomized)


#Цель - перемешать буквы в начале 

DEF_LEN = 260 #допустимая длина хеш-кода

#Берем рандомное смещение таблицы символов
rand_ord = rand(10, 50)

#################################
print(available)
print(len(available))
print(randomized)
print("".join(set(list(randomized))))
print()
#################################

#Объявляю строку, в которую будет помещен рандомный хеш-код, составленный из допустимых символов
string = ""
for i in range(DEF_LEN):
	string += choice(available)

#################################
print(string)
#################################

#Пример рандомно-сгенерированного хеш-кода
start = "ANp&NZq0R86aiJmXr6TFJhpK1SyNpPq9eKMZKzfU*havawOJRDiHOWyBXEf8xsbaqfDVAGOILK^J6AvEHyxm1Tz&wo=GxCg=eEj7z&=e40073AILSjDBf5zTv=IFYwni2qUk9CXQtjFZGP9lGGPXZ68f&^rQ&SeqMOA5H-R^HBX5QRZbW1D6bnbJStCwIaEj*Qf3CV&M8qFcHDp0LlkKS78icMNG+IUYw8s0xuUhhPmsQtGcYDc&YgmpCCQNE0NO^aE6"
#Пример хеш-кода с максимальной суммой (65390 ~ 2^16: 65536)
end = "".join(["z" for _ in range(DEF_LEN)])

#################################
print()
#################################

#Функция, получающая сумму элементов хеш-кода
def get_sum(value):
	sums = 0

	#Сумма будет зависить еще от позиции элемента в хеш-коде
	for k, v in enumerate(value):
		#print(k, ord(v), v)
		sums += ord(v)+k

	return sums

#################################
#print(get_sum(start), get_sum(string), get_sum(end))
#print(get_sum(start))
print()
#################################

#Функция для получения рандомного реквест-кода (запроса для активации) из хеш-кода
def get_request():

	#Берем рандомную длину
	strlen = rand(50, 80)

	#Берем рандомную позицию
	pos = rand(1, DEF_LEN-strlen)
	print("POS:", pos, "%.2x"%pos)
	print("RANDOM:", rand_ord, randomized[rand_ord])

	#Вырезаем подстроку из строки значения, чтобы получить из нее реквест-код
	substr = start[pos:pos+strlen]
	
	#Делаем смещение таблицы символов
	moved_av = "".join([randomized[i+rand_ord] for i in range(-len(randomized), 0)])
	print("SUBSTRING:")
	print(substr)
	print()
	
	#Собираем строку-реквест относительно вырезанной подстроки, заменяя каждый элемент для randomized на соответствующий ему из смещенной таблицы
	newstr = ""
	for i in substr:
		newstr += moved_av[randomized.index(i)]

	print(newstr)
	print()

	#Возвращается строка вида, где первый символ - это индекс смещения, записанный в виде элемента массива randomized
	#   затем 2 символа - начальная позиция подстроки внутри хеш-кода
	#   остальные символы - это преобразованная строка
	return randomized[rand_ord] + "%.2x"%pos + newstr

print("REQUEST CODE:")
x = get_request()
print(x)

#Функция получения активирующего кода для реквест-кода
def get_activation(request):

	#DBG:
	if request[0] not in randomized or len(request) <= 10:
		return False

	try:
		int(request[1:3], 16)
	except:
		return False



	#Получение значений из текущей строки запроса
	rand_ord = randomized.index(request[0])
	pos = int(request[1:3], 16)
	print(rand_ord, pos)

	#По полученному смещению организовать смещенный массив
	moved_av = "".join([randomized[i+rand_ord] for i in range(-len(randomized), 0)])

	#Организовать оригинальную строку
	oldstr = ""
	for i in request[3:]:
		oldstr += randomized[moved_av.index(i)]

	ln = len(oldstr)
	if start[pos:pos+ln] != oldstr:
		return False

	#Посчитать сумму текущей строки внутри исходной
	sumsr = 0
	for k, v in enumerate(oldstr):
		sumsr += ord(v) + k + pos

	#Получить новое число суммы с вычлененным значением относительно старого числа
	sums = get_sum(start)
	sumsr = sums-sumsr 

	print(sumsr)

	#Получить HEX-код числа
	sumsr = "%.4x"%sumsr
	
	print(sumsr)

	#Преобразовать строку суммы 
	codestr = ""
	for k, v in enumerate(sumsr):
		codestr += randomized[int(v, 16)+k]

	print(codestr)
	
	#Собрать рандомную длину строки и позицию элемента в ней
	rand_size = rand(40, 50)
	rand_pos = rand(0, rand_size)
	
	print(rand_size, rand_pos)

	#Сборка новой строки
	newstr = str(randomized[rand_pos])
	for i in range(rand_size):
		#На i-е место поместить codestr
		if i == rand_pos:
			newstr += codestr
		elif not (rand_pos < i < rand_pos+4):
			newstr += randomized[rand(0, len(randomized)-1)]

	return newstr

print()
print("ACTIVATION:")
y = get_activation(x)
print(y)

def check_activation_code(request, activation):

	#DBG:
	if request[0] not in randomized or len(request) <= 10:
		return False

	try:
		int(request[1:3], 16)
	except:
		return False



	#Получение значений их текущей строки запроса
	rand_ord = randomized.index(request[0])
	pos = int(request[1:3], 16)
	print(rand_ord, pos)

	#По полученному смещению организовать смещенный массив
	moved_av = "".join([randomized[i+rand_ord] for i in range(-len(randomized), 0)])

	#Организовать оригинальную строку
	oldstr = ""
	for i in request[3:]:
		oldstr += randomized[moved_av.index(i)]

	#Посчитать сумму текущей строки внутри исходной
	sumsr = 0
	for k, v in enumerate(oldstr):
		sumsr += ord(v) + k + pos

	#Получить новое число суммы с вычлененным значением относительно старого числа
	sums = get_sum(start)
	sumsr = sums-sumsr 


	#Проводим обратную операцию для кода активации, получаем позицию кода
	actpos = randomized.index(activation[0])+1

	print(activation[actpos:actpos+4])

	#Получаем код
	code = activation[actpos:actpos+4]

	#Преобразуем код к 16ричному виду
	hexad = ""
	for i in range(len(code)):
		hexad += "%x"%(randomized.index(code[i])-i)

	#DBG
	try:
		int(hexad, 16)
	except:
		return False

	#Возвращаем совпадение разности сумм кода активации и реквест-кода
	return int(hexad, 16) == sumsr


print()
print(check_activation_code(x, y))
print(check_activation_code(x, "abcbsdsgjk"))


