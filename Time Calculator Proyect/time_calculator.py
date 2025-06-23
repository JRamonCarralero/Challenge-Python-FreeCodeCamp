def check_day(day):
    if day == 'monday' or day == 0:
        return ('Monday', 0)
    elif day == 'tuesday' or day == 1:
        return ('Tuesday', 1)
    elif day == 'wednesday' or day == 2:
        return ('Wednesday', 2)
    elif day == 'thursday' or day == 3:
        return ('Thursday', 3)
    elif day == 'friday' or day == 4:
        return ('Friday', 4)
    elif day == 'saturday' or day == 5:
        return ('Saturday', 5)
    elif day == 'sunday' or day == 6:
        return ('Sunday', 6)

def add_time(start, duration, day = ''):
    array_time = start.split(' ')
    total_time = array_time[0]
    meridian = array_time[1]
    array_total_time = total_time.split(':')
    hours = array_total_time[0]
    minutes = array_total_time[1]
    duration_array = duration.split(':')
    duration_hours = duration_array[0]
    duration_minutes = duration_array[1]

    hours = int(hours) + int(duration_hours)
    minutes = int(minutes) + int(duration_minutes)

    plus_hours = minutes // 60
    minutes = minutes % 60
    hours += plus_hours
    days = hours // 24
    hours = hours % 24

    if hours >= 12:
        if meridian == 'AM':
            meridian = 'PM'
        else:
            meridian = 'AM'
            days += 1
        if hours > 12:
            hours = hours % 12

    minutes = str(minutes).zfill(2)
    str_hours = f'{hours}:{minutes} {meridian}'
    str_days = ''
    if days == 1:
        str_days += ' (next day)'
    elif days > 1:
        str_days += f' ({days} days later)'
    new_time = ''
    if day:
        number_day = check_day(day.lower())
        final_day = (number_day[1] + days) % 7
        day_final = check_day(final_day)
        day_name = day_final[0]
        new_time = f'{str_hours}, {day_name}{str_days}'
    else:
        new_time = f'{str_hours}{str_days}'


    return new_time


print(add_time('3:30 PM', '2:12', 'Monday'))