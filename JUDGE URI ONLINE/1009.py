NOME = str(input())
SALARIO = float(input())
VENDAS = float(input())
TOTAL = (VENDAS*15)/100 + SALARIO
print('TOTAL = R$ {:.2f}'.format(TOTAL))