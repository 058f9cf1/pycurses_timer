#!/usr/bin/env python3

import time
import sys
import curses

SIZE = 2
digit_height = SIZE * 5
digit_width = SIZE * 6

# Digit character parts
f = [1, 1, 1, 1, 1, 1]
l = [1, 1, 0, 0, 0, 0]
r = [0, 0, 0, 0, 1, 1]
g = [1, 1, 0, 0, 1, 1]

templates = [[f, g, g, g, f],  # 0
             [r, r, r, r, r],  # 1
             [f, r, f, l, f],  # 2
             [f, r, f, r, f],  # 3
             [g, g, f, r, r],  # 4
             [f, l, f, r, f],  # 5
             [f, l, f, g, f],  # 6
             [f, r, r, r, r],  # 7
             [f, g, f, g, f],  # 8
             [f, g, f, r, f]]  # 9


def is_p_int(t):
    """Determine if t is a positive integer"""

    # Check if t is an integer
    try:
        t = int(t)
    except ValueError:
        return False

    # Check that t is positive
    return t > 0


def draw_digit(screen, oy, ox, number):
    """Draw the given digit on the screen starting at coordinates (oy, ox)"""

    template = templates[int(number)]
    for y in range(len(template) * SIZE):
        for x in range(len(template[y//SIZE])):
            screen.addstr(oy+y, ox+(x*SIZE), " " * SIZE, curses.color_pair(template[y//SIZE][x]))


def run_timer(screen, t):
    """Main program loop"""

    # Initialise curses
    key_pressed = 0
    curses.curs_set(0)
    screen.nodelay(1)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_RED)

    start = time.time()
    elapsed = 0

    # Loop until the user presses 'q'
    while key_pressed != ord('q'):

        # Clear the screen
        screen.erase()

        # Get screen size
        rows, cols = screen.getmaxyx()
        screen.addstr(rows - 1, 0, "press 'q' to quit", curses.color_pair(1))

        if elapsed < t:
            # Calculate how much time has passed
            elapsed = time.time() - start

            # Convert time left in seconds to minutes and seconds
            m, s = divmod(int(t - elapsed) + 1, 60)

            # Add leading zeroes to the time if only one digit
            digits = str(m).zfill(2) + str(s).zfill(2)
        else:
            # Turn background red once time's up
            screen.bkgd(' ', curses.color_pair(2))
            digits = "0000"

        # Display digits on the screen
        oy = rows//2 - digit_height//2
        ox = cols//2
        draw_digit(screen, oy, ox - digit_width * 2 - SIZE * 2,     digits[-4])
        draw_digit(screen, oy, ox - digit_width     - SIZE,         digits[-3])
        draw_digit(screen, oy, ox                   + SIZE + 2,     digits[-2])
        draw_digit(screen, oy, ox + digit_width     + SIZE * 2 + 2, digits[-1])

        # Display the colon between minutes and seconds
        screen.addstr(rows//2 + 1, ox, "  ", curses.color_pair(1))
        screen.addstr(rows//2 - 1, ox, "  ", curses.color_pair(1))

        # Update the screen
        screen.refresh()

        # Check if the user has quit
        key_pressed = screen.getch()


if __name__ == "__main__":

    # Get the timer length from the arguments
    if len(sys.argv) > 1:
        t = sys.argv[1]

        # Check if the argument is in the correct format
        if is_p_int(t):
            curses.wrapper(run_timer, int(t))
        else:
            print("ERROR: Argument not a positive integer")
    else:
        print("USAGE: ./curses_timer.py <time>")
