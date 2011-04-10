import math
#Convierte un numero a base 256a fijo de N bytes
def encode(numero_inicial, base = 256, numero_bytes = 4):
#	resto=0
#	n=numero_inicial
#	while (n >= base):
#		k = int(math.floor(n / base))
#		resto = n - k * base
	resto=(numero_inicial%base)
#	k=(n-resto)/base
#	print"Resto: ",resto,"\tn: ",n,"k: ",k
#	n = k
	return chr(resto)

def decode(c, exp,base = 256):
#    i = 0
#    for c in string:
	numero = (ord(c) * math.pow(base, exp))
#        i += 1
#	print string,"\t",numero
	return int(numero)
