x = float(input())
if x >= 0 and x <= 400:
    novo = (x * 15) / 100 + x
    reajuste = novo - x
    percentual = 15
elif x >= 400.01 and x <= 800.00:
    novo = (x * 12) / 100 + x
    reajuste = novo - x
    percentual = 12
elif x >= 800.01 and x <= 1200.00:
    novo = (x * 10) / 100 + x
    reajuste = novo - x
    percentual = 10
elif x >= 1200.01 and x <= 2000.00:
    novo = (x * 7) / 100 + x
    reajuste = novo - x
    percentual = 7
elif x > 2000.00:
    novo = (x * 4) / 100 + x
    reajuste = novo - x
    percentual = 4
print('Novo salario: {:.2f}'.format(novo))
print('Reajuste ganho: {:.2f}'.format(reajuste))
print('Em percentual: {} %'.format(percentual))
