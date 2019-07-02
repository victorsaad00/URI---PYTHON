i = int(input())
def calc_days(years_ad, years, months, days):
    if years_ad >= 365:
        years_ad -= 365
        years += 1
        return calc_days(years_ad, years, 0, 0)
    elif years_ad >= 30:
        years_ad -= 30
        months += 1
        return calc_days(years_ad, years, months, 0)
    elif years_ad < 30 and years_ad > 0:
        years_ad -= 1
        days += 1
        return calc_days(years_ad, years, months, days)
    else:
        print('{} ano(s)'.format(int(years)))
        print('{} mes(es)'.format(int(months)))
        print('{} dia(s)'.format(int(days)))


calc_days(i, 0, 0, 0)

