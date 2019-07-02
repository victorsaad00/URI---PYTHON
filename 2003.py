while True:
    try:
        time = input().split(':')
        late_time = int(time[0]) * 60 + int(time[1]) - 420
        if late_time < 0:  late_time = 0

        print('Atraso maximo: {}'.format(late_time))

    except EOFError: break