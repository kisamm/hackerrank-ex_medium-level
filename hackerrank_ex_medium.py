def is_leap(year):
    leap = False
    leap1 = True

    if year%400 == 0:
        return leap1
    elif year % 4 ==0 and not year%100 == 0 or year%100 ==0 and not year % 4 ==0:
        return leap1 or leap
    else: return leap

year = int(input())
print(is_leap(year))