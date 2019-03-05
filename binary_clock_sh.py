#!/usr/bin/env python

from sense_hat import SenseHat
import time, datetime

hat = SenseHat()

year_color = (0, 127, 0)
month_color = (0, 0, 127)
day_color = (127, 0, 0)
hour_color = (0, 127, 0)
minute_color = (0, 0, 127)
second_color = (127, 0, 0)
hundrefths_color = (49, 49, 49)
weekday_color  = (120, 120, 0)
dst_color = (100, 100, 0)
off = (0, 0, 0)
on = (127, 127, 127)

hat.clear()

def display_binary(value, row, color):
	binary_str = "{0:8b}".format(value)
	for x in range(0, 8):
		if binary_str[x] == '1':
			hat.set_pixel(x, row, color)
		else:
			hat.set_pixel(x, row, off)

def display_dst():
    global weekday_color
    if time.localtime().tm_isdst  == '1':
            weekday_color = (127, 127, 0)
    else:
            weekday_color = (0, 127, 127)

while True:
	t = datetime.datetime.now()
        w = datetime.datetime.today()
	display_binary(t.year % 100, 0, year_color)
	display_binary(t.month, 1, month_color)
	display_binary(t.day, 2, day_color)
        display_dst()
        display_binary(w.isoweekday(), 3, weekday_color)
	display_binary(t.hour, 4, hour_color)
	display_binary(t.minute, 5, minute_color)
	display_binary(t.second, 6, second_color)
	display_binary(t.microsecond / 10000, 7, hundrefths_color)
	time.sleep(0.0001)
