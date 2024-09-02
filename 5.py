'''
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
'''

palavra = input("Digite uma palavra: ")
letras = []
for l in palavra:
    letras.append(l)

letrasaocontrario = letras[::-1]

palavracontraria = ""
for l in letrasaocontrario:
    palavracontraria = palavracontraria+l

print(f"Sua palavra ao contrario: {palavracontraria}")

