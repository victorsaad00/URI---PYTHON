seconds = int(input())
def calc_horas(seconds_ad,horas,minuts,seconds):
    if seconds_ad >= 3600:
        seconds_ad -= 3600
        horas += 1
        return calc_horas(seconds_ad, horas, 0, 0)
    elif seconds_ad >= 60:
        seconds_ad -= 60
        minuts += 1
        return calc_horas(seconds_ad, horas,minuts,0)
    elif seconds_ad < 60 and seconds_ad > 0:
        seconds_ad -= 1
        seconds += 1
        return calc_horas(seconds_ad, horas, minuts, seconds)
    else:
        print('{}:{}:{}'.format(horas,minuts,seconds))

calc_horas(seconds,0,0,0)