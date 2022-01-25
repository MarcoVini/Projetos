import random
import string

tamanho = int(input('Digite o tamanho da senha desejada: '))

chars = string.ascii_letters + string.digits + '!@+-*'

rnd = random.SystemRandom() #os.urandom

print(''.join(rnd.choice(chars) for i in range(tamanho)))

#rnd.choice retorna uma lista com os caracteres randomicos gerados através do chars

