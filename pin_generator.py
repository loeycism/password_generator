import random

# caracteres permitidos
digits = '0123456789'

use_for = digits

print("Quantos caracteres você quer que seu pin tenha?")
print("(1) 4 caracteres    (2) 8 caracteres    (3) 10 caracteres")

escolhido = int(input("Escreva aqui a opção: "))

if (escolhido == 1):
    length_pass = 4
elif (escolhido == 2):
    length_pass = 8
else:
    length_pass = 10

password = "".join(random.sample(use_for, length_pass))

print("A sua senha será: ", password)