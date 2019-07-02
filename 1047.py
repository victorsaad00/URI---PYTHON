initial_hour, initial_minute, final_hour, final_minute = input().split()

initial_hour = int(initial_hour)
initial_minute = int(initial_minute)
final_hour = int(final_hour)
final_minute = int(final_minute)

total_hour = final_hour - initial_hour
total_min = final_minute - initial_minute

if total_hour < 0 :
    total_hour += 24

if total_min < 0:
    total_min+=60
    total_hour-=1

if total_min == 0 and total_hour == 0:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
else:
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(total_hour,total_min))




