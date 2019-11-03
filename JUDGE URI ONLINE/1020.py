idade = int((input()))
ano = idade//365
mes = (idade-(ano*365))//30
dia = idade-(ano*365)-(mes*30)
print('{} ano(s)'.format(ano))
print('{} mes(es)'.format(mes))
print('{} dia(s)'.format(dia))