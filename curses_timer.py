#!/usr/bin/env python3

import time
import sys
import curses
import templates

SIZE = 2


def error_check(t):
	#Check if t is an integer
	try:
		t = int(t)
	except ValueError:
		return 1
	#Check that t is positive
	return t < 1


def draw_digit(screen, oy, ox, number):
	template = templates.templates(int(number))
	for i in range(0, len(template) * SIZE, SIZE):
		for j in range(len(template[i//SIZE])):
			for k in range(SIZE):
				screen.addstr(i+oy+k, j+ox, " ", curses.color_pair(template[i//SIZE][j]))


def run_timer(screen, t):
	key_pressed = 0
	curses.curs_set(0)
	screen.nodelay(1)
	curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
	#Loop whilst the time has not elapsed
	while(key_pressed != ord('q') and t > 0):
		#Clear the screen
		screen.erase()
		#Get screen size
		rows, cols = screen.getmaxyx()

		#Subtract a second
		t -= 1
		#Convert seconds to minutes and seconds
		m, s = divmod(t, 60)
		#Add leading zeroes to the time if only one digit
		digits = str(m).zfill(2) + str(s).zfill(2)
		#Display digits on the screen
		draw_digit(screen, (rows - SIZE * 5)//2, cols//2 - 28, digits[0])
		draw_digit(screen, (rows - SIZE * 5)//2, cols//2 - 14, digits[1])
		draw_digit(screen, (rows - SIZE * 5)//2, cols//2 + 4, digits[2])
		draw_digit(screen, (rows - SIZE * 5)//2, cols//2 + 18, digits[3])
		#Display the colon between minutes and seconds
		screen.addstr(rows//2+1,cols//2, "  ", curses.color_pair(1))
		screen.addstr(rows//2-1,cols//2, "  ", curses.color_pair(1))
		#Show the new digits
		screen.refresh()
		#Check if the user quits
		key_pressed = screen.getch()
		#Wait 1 second
		time.sleep(1)


if  __name__ == "__main__":
	#Error if no argument given
	if len(sys.argv) < 2:
		print("ERROR: No argument given")
	else:
		t = sys.argv[1]
		#Check if the argument is in the correct format
		if(not error_check(t)):
			curses.wrapper(run_timer, int(t))
		else:
			print("ERROR: Argument not a positive integer")
