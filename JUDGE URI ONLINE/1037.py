N = float(input())
if N >= 0 and N <= 25.0000:
    print('Intervalo [0,25]')
elif N >= 25.00001 and N <= 50.0000000:
    print('Intervalo (25,50]')
elif N >= 50.00001 and N <= 75.0000000:
    print('Intervalo (50,75]')
elif N >= 75.00001 and N <= 100.0000000:
    print('Intervalo (75,100]')
else:
    print('Fora de intervalo')
