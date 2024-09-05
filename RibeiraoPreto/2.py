String1 = input("Digite uma palavra ou frase: ")
array = []
for l in String1:
    array.append(l)

contador = 0

for item in array:
    if item == "a" or item =="A":
        contador += 1

if contador > 0:
    print(f"A letra [A] apareceu {contador} vezes durante sua string")

else:
    print("Sua string não tem a letra a")