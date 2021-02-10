# -*- coding: utf-8 -*-
# @Time    : 2021-02-09 22:34
# @Author  : Wxc
# @FileName: time_calculator
# @Software: PyCharm

# 要学会把脑海里的计算方法以程序的方式表达出来
# 每个时段由12个小时构成，以数字12、1、2、3、4、5、6、7、8、9、10、11依次序表示。
WEEK_DAY = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def add_time(start, duration, week_day=None):
    start_hour = int(start.split(':')[0])
    start_minute = int(start.split(':')[1].split()[0])
    am_pm = start.split(':')[1].split()[1]
    temp_am_pm = am_pm
    duration_hour = int(duration.split(':')[0])
    duration_minute = int(duration.split(':')[1])

    end_minute = (start_minute + duration_minute) % 60
    end_hour = (start_hour + duration_hour + (start_minute + duration_minute) // 60) % 12
    if (start_hour + duration_hour + (start_minute + duration_minute) // 60) // 12 % 2 == 1:
        if am_pm == 'AM':
            temp_am_pm = 'PM'
        else:
            temp_am_pm = 'AM'
    if end_hour == 0:
        end_hour = 12
    N_days = (start_hour + duration_hour + (start_minute + duration_minute) // 60) // 12 // 2
    if am_pm == 'PM' and temp_am_pm == 'AM':
        N_days += 1

    new_time = f"{end_hour}:{('0' + str(end_minute)) if end_minute < 10 else end_minute} {temp_am_pm}"
    if week_day:
        new_week_day = WEEK_DAY[(WEEK_DAY.index(week_day.capitalize()) + N_days) % 7]
        new_time += (', ' + new_week_day)
    if N_days == 1:
        new_time += " (next day)"
    elif N_days > 1:
        new_time += f" ({N_days} days later)"
    return new_time
