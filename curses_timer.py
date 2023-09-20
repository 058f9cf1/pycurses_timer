#!/usr/bin/python

import time
import sys
import curses
import templates


def error_check(t):
	try:
		t = int(t)
	except ValueError:
		return 1
	if(t<1):
		return 1
	return 0


def draw_digit(screen, oy, ox, number):
	template = templates.templates(int(number))
	for i in range(len(template)):
		for j in range(len(template[i])):
			screen.addstr(i+oy, j+ox, " ", curses.color_pair(template[i][j]))


def run_timer(screen, t):
	key_pressed = 0
	curses.curs_set(0)
	screen.nodelay(1)
	curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
	while(key_pressed != ord('q') and t > 0):
		screen.erase()
		rows, cols = screen.getmaxyx()
		m, s = divmod(t, 60)
		digits = str(m).zfill(2) + str(s).zfill(2)
		draw_digit(screen, rows//2 - 5, cols//2 - 28, digits[0])
		draw_digit(screen, rows//2 - 5, cols//2 - 14, digits[1])
		draw_digit(screen, rows//2 - 5, cols//2 + 4, digits[2])
		draw_digit(screen, rows//2 - 5, cols//2 + 18, digits[3])
		screen.addstr(rows//2+1,cols//2,"  ",curses.color_pair(1))
		screen.addstr(rows//2-1,cols//2,"  ",curses.color_pair(1))
		t -= 1
		screen.refresh()
		key_pressed = screen.getch()
		time.sleep(1)


if  __name__ == "__main__":
	try:
		t = sys.argv[1]
	except IndexError:
		print("ERROR: No argument given")
	else:
		if(not error_check(t)):
			curses.wrapper(run_timer, int(t))
		else:
			print("ERROR: Argument not a positive integer")
