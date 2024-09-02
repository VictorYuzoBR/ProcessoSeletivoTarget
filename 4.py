'''
4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
• SP – R$67.836,43
• RJ – R$36.678,66
• MG – R$29.229,88
• ES – R$27.165,48
• Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.
'''

Array = [["SP",67836.43],["RJ",36678.66],["MG",29229.88],["ES",27165.48],["OUTROS",19849.53]]

total = 0
for item in Array:
    total = total + item[1]
print(f"TOTAL: {total}")
print()
for item in Array:
    p = (item[1]/total)*100
    print(f"ESTADO: {item[0]} --- PARTICIPAÇÃO: {p:.2f}%")
