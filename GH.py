#Esse código tem como o intuito ser o gerador de Hashs.
import hashlib

while True:
    string = input('\nDigite o texto a ser transformado em Hashe: ')
    menu = int(input(''' ### MENU - TIPO DE HASH ###
                 1) MD5
                 2) SHA1
                 3) SHA256
                 4) SHA512
                 Digite o número do tipo de hash a ser gerado: '''))


    if menu == 1:
        resultado = hashlib.md5(string.encode('utf-8'))
        print(f'O hash MD5 da string {string} é:', resultado.hexdigest())

    elif menu == 2:
        resultado = hashlib.sha1(string.encode('utf-8'))
        print(f'O hash SHA1 da string {string} é:', resultado.hexdigest())

    elif menu == 3:
        resultado = hashlib.sha256(string.encode('utf-8'))
        print(f'O hash SHA256 da string {string} é:', resultado.hexdigest())

    elif menu == 4:
        resultado = hashlib.sha512(string.encode('utf-8'))
        print(f'O hash SHA512 da string {string} é:', resultado.hexdigest())

    else:
        print('Foi digitado um número incorreto.')
