n1, n2, n3, n4 =input().split()

media = (float(n1)*2 + float(n2)*3 + float(n3)*4 + float(n4)) / (2+3+4+1)

if float(media) >= float(7):
    print("Media: {:0.1f}\nAluno aprovado.".format(float(media)))
elif media < 5:
    print("Media: {:0.1f}\nAluno reprovado.".format(float(media)))
elif media >= 5 and media < 7:
    print("Media: {:0.1f}\nAluno em exame.".format(float(media)))
    score = float(input())
    avarage = (float(media) + float(score))/2
    if avarage < 5:
        print("Nota do exame: {:0.1f}\nAluno reprovado.\nMedia final: {:0.1f}".format(float(score),float(avarage)))
    elif avarage >= 5:
        print("Nota do exame: {:0.1f}\nAluno aprovado.\nMedia final: {:0.1f}".format(float(score), float(avarage)))