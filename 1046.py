initial_hour, initial_minute, final_hour, final_minute =input().split()
initial_hour = int(initial_hour)
initial_minute = int(initial_minute)
final_hour = int(final_hour)
final_minute = int(final_minute)

def game_time_hours(start, end):
    if start > end:
        i=0
        j=0
        while start < 24:
            i+=1
            start+=1
        while j < end:
            j+=1
        return j + i
    elif start == end:
        return 24
    elif (end - start) == 1:
        return 0
    elif start < end:
        return (end-start)

def game_time_minutes(start, end):
    if start > end:
        i=0
        j=0
        while start < 60:
            i+=1
            start+=1
        while j < end:
            j+=1
        return j + i
    elif start == end:
        return 0
    elif start < end:
        return (end-start)


print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(game_time_hours(initial_hour,final_hour),game_time_minutes(initial_minute,final_minute)))