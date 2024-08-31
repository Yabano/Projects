# x = 7
# for i in range(1, 10, 2):
#     for j in range(x, x-3, -1):
#         print("I={} J={}".format(i, j))
#     x+=2

def tempo_para_segundos(tempo):
    horas, minutos, segundos = map(int, tempo.split(':'))
    return horas * 3600 + minutos * 60 + segundos

def segundos_para_tempo(segundos):
    horas = segundos // 3600
    segundos %= 3600
    minutos = segundos // 60
    segundos %= 60
    return horas, minutos, segundos

def calcular_duracao_evento():
    entrada = []
    for _ in range(4):
        entrada.append(input())

    dia_inicio = int(entrada[0].split()[1])
    inicio = tempo_para_segundos(entrada[1])
    dia_fim = int(entrada[2].split()[1])
    fim = tempo_para_segundos(entrada[3])

    duracao_total_segundos = (dia_fim - dia_inicio) * 24 * 3600 + (fim - inicio)
    dias, horas, minutos, segundos = duracao_total_segundos // (24 * 3600), (duracao_total_segundos % (24 * 3600)) // 3600, (duracao_total_segundos % 3600) // 60, duracao_total_segundos % 60

    print(f"{dias} dia(s)")
    print(f"{horas} hora(s)")
    print(f"{minutos} minuto(s)")
    print(f"{segundos} segundo(s)")

calcular_duracao_evento()