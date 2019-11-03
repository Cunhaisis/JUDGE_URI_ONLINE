CODIGO,QUANTIDADE = (input()).split()
CODIGO = int(CODIGO)
QUANTIDADE = int(QUANTIDADE)
if CODIGO == 1:
    TOTAL = QUANTIDADE * 4.00
elif CODIGO == 2:
    TOTAL = QUANTIDADE * 4.50
elif CODIGO == 3:
    TOTAL = QUANTIDADE * 5.00
elif CODIGO == 4:
    TOTAL = QUANTIDADE * 2.00
elif CODIGO == 5:
    TOTAL = QUANTIDADE * 1.50
print('Total: R$ {:.2f}'.format(TOTAL))