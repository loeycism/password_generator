import random

# caracteres permitidos
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
punctuation = '#$%&*?@_-'

use_for = ascii_lowercase + ascii_uppercase + digits + punctuation

print("Quantos caracteres você quer que sua senha tenha?")
print("(1) 8 caracteres    (2) 12 caracteres    (3) 18 caracteres")

escolhido = int(input("Escreva aqui a opção: "))

if (escolhido == 1):
    length_pass = 8
elif (escolhido == 2):
    length_pass = 12
else:
    length_pass = 18

password = "".join(random.sample(use_for, length_pass))

print("A sua senha será: ", password)