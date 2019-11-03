N1, N2, N3, N4 = (input().split())
N1 = float(N1)
N2 = float(N2)
N3 = float(N3)
N4 = float(N4)
MEDIA = (N1 * 2 + N2 * 3 + N3 * 4 + N4) / (10)
if MEDIA >= 7.0:
    print('Media: {:.1f}'.format(MEDIA))
    print('Aluno aprovado.')
elif MEDIA < 5.0:
    print('Media: {:.1f}'.format(MEDIA))
    print('Aluno reprovado.')
elif MEDIA >= 5.0 and MEDIA <= 6.9:
    print('Media: {:.1f}'.format(MEDIA))
    print('Aluno em exame.')
    notaExame = float(input())
    print('Nota do exame: {}'.format(notaExame))
    N5 = (notaExame + MEDIA) / 2
    if N5 >= 5.0:
        print('Aluno aprovado.')
        print('Media final: {:.1f}'.format(N5))
    if N5 <= 4.9:
        print('Aluno reprovado.')
        print('Media final: {:.1f}'.format(N5))
