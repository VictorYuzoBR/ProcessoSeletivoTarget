'''
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
'''

#passos -> Criar uma lista de dicionários com os meses -> adicionar em cada mês seu ID e uma lista de dias -> Produzir todos os calculos necessários de acordo com os dados no momento
# irei considerar 30 dias para todos os meses

meses = []
print("Iniciando inserção de dados")
insercao = True #mantem o loop ativo enquanto estiver inserindo dados

while insercao == True:
    op = input("Digite o número do mês que você deseja inserir dados ou sair para sair: ")
    if op == "sair":
        insercao = False
    else:
        if int(op) < 1 or int(op) > 12:
            print("Digite um mês válido (1 a 12)")
        else:
            existe = False
            if len(meses) > 0:
                for mes in meses:
                    if mes["ID"] == op:
                        existe = True
            if existe == True:
                print("Dados sobre este mês ja existem")
            else:
                print(f"Dados sobre o mês {op} serão criados: ")
                dictaux = {}  # item que será adicionado na lista de meses
                dictaux["ID"] = op
                listafaturamento = []
                for i in range(1, 31):
                    valor = float(input(f"Digite o faturamento do dia {i}: "))
                    listafaturamento.append(valor)
                dictaux["FATURAMENTO"] = listafaturamento
                print()
                meses.append(dictaux)
                print("Dados criados com sucesso")

#agora que o os meses foram criados, serão feitos os calculos

analise = True #Mantem o loop de analise de dados ativo
print()
print("-----Painel de analise-----")
while analise == True:
    op2 = input("Digite o número do mês que você deseja analisar os dados ou sair para sair: ")
    if op2 == "sair":
        analise = False
    else:
        if len(meses) == 0:
            print("Dados sobre nenhum mês foram inseridos, por favor finalize o programa")
        else:
            quant = 0
            for mes in meses:
                if mes["ID"] == op2:
                    arraysorted = sorted(mes["FATURAMENTO"]) #coloca em ordem crescente os faturamentos para descobrir menor e maior valor
                    menor = arraysorted[0]
                    maior = arraysorted[29]
                    soma = 0
                    for num in arraysorted:
                        soma = soma + num
                    media = soma/30
                    contador = 0
                    for num in arraysorted:
                        if num > media:
                            contador += 1
                    print("Gerando relatorio")
                    print()
                    print(f"Lista de faturamentos: {mes["FATURAMENTO"]}")
                    print()
                    print(f"Maior valor no mês: {maior}")
                    print(f"Menor valor no mês: {menor}")
                    print(f"Media do mês: {media}")
                    print(f"Dias em que o faturamento foi maior que a média: {contador}")
                    print()
                    break
                else:
                    quant += 1
                if quant == len(meses):
                    print("Não existem dados sobre este mês")
                    break

'''
Após a conclusão do problema percebi que os dados deveriam vir de um json, nesse caso, considerando que o json traria os dados de apenas um mês, ficaria 
tudo mais fácil.
a ordem correta seria:

receber o json -> transformar o json em um dicionário com json.loads -> descobrir estrutura dos dados -> refazer os calculos com os dados corretos
'''



