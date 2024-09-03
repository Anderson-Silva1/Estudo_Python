"""
    TIME() >> Provê diversas funções relacionadas a tempo. Também pode ser útil conhecer os módulos datetime e calendar.
"""
import time

tempo = time.time()
# print(f"Se passaram {tempo} segundos desde o dia 01/01/1970 às 00:00:00 UTC")
# Retorna o número de segundos desde o "Epoch" (que é 1 de janeiro de 1970, 00:00:00 UTC). Isso é útil para marcar timestamps ou medir a duração de algo.

tempo = time.ctime(200)
print(f"Voltamos 200 segundos e etamos no tempo: {tempo}")
# Retorna o número de segundos desde o "Epoch" (que é 1 de janeiro de 1970, 00:00:00 UTC). Isso é útil para marcar timestamps ou medir a duração de algo.

print("Inicio")
time.sleep(3)
print("Fim, 3 segundos depois")
# Pausa a execução do programa pelo número de segundos especificado. Isso é útil para criar atrasos entre operações.

tempo = time.ctime()
print(tempo)
# Uma string representando o horário local, calculado a partir do número de segundos passado como parâmetro.
