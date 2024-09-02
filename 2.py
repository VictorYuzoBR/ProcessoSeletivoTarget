'''
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
'''
n1 = 0
n2 = 1
aux = 0
NumeroEscolhido = int(input("Digite um numero inteiro positivo para saber se ele pertence à sequencia de Fibonacci: "))
print()
print("Calculando sequência até o ponto mais próximo do seu numero...")
print("0")

#Calcular a sequência até o valor mais próximo do número escolhido
while n1 < NumeroEscolhido:
  aux = n1
  n1 = n2 + n1
  n2 = aux
  if n1 == NumeroEscolhido:
      print("["+str(n1)+"]")
  else:
      print(str(n1))

#Comparar o ultimo valor de N1 com o número escolhido para descobrir se faz parte ou não
if n1 == NumeroEscolhido:
    print("Seu número faz parte da sequência")
else:
    print("Seu número não faz parte da sequencia")