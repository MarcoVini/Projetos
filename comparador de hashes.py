#Código feito para comparar se hashes códigos são iguais ou diferentes.
import hashlib

arq1= 'cp.txt'
arq2= 'cp2.txt'

hash1 = hashlib.new('ripemd160')

hash1.update(open(arq1, 'rb').read())

hash2 = hashlib.new('ripemd160')

hash2.update(open(arq2, 'rb').read())

if hash1.digest() != hash2.digest():
    print(f'O arquivo: {arq1} é diferente do arquivo: {arq2}. ')
    print(f'{hash1.hexdigest()} ≠ {hash2.hexdigest()}')
else:
    print('Os arquivos são iguais.')
    print(f'{hash1.hexdigest()} = {hash2.hexdigest()}')
