import math
#Convierte un numero a base 256a fijo de N bytes
def encode(numero_inicial, base = 256, numero_bytes = 4):
	resto=(numero_inicial%base)
	return chr(resto)
	
def encode_last(numero_inicial, base = 256, numero_bytes = 4):
	n=numero_inicial
	while (n >= base):
		k = int(math.floor(n / base))
		resto = n - k * base
		n = k
	return chr(n)
def decode(c, exp,base = 256):
	print ord(c),"+",base,"^",exp
	numero = (ord(c) * math.pow(base, exp))
	return int(numero)
