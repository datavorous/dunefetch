import curses
import time


class cursu:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.pixels = []
        # (y, x, char, color_pair)
        curses.curs_set(0)
        curses.start_color()
        curses.use_default_colors()
        self.init_colors()
        self.stdscr.nodelay(True)
        self.stdscr.timeout(100)

    # LLMs are so helpful
    def init_colors(self):
        # Catppuccin “pastel” palette (1–15):
        curses.init_pair(1,  224, -1)  # Rosewater
        curses.init_pair(2,  217, -1)  # Flamingo
        curses.init_pair(3,  225, -1)  # Pink
        curses.init_pair(4,  183, -1)  # Mauve
        curses.init_pair(5,  210, -1)  # Red
        curses.init_pair(6,  211, -1)  # Maroon
        curses.init_pair(7,  216, -1)  # Peach
        curses.init_pair(8,  229, -1)  # Yellow
        curses.init_pair(9,  151, -1)  # Green
        curses.init_pair(10, 158, -1)  # Teal
        curses.init_pair(11, 117, -1)  # Sky
        curses.init_pair(12, 110, -1)  # Sapphire
        curses.init_pair(13, 111, -1)  # Blue
        curses.init_pair(14, 147, -1)  # Lavender
        curses.init_pair(15, 189, -1)  # Text
        curses.init_pair(16, 233, -1)  # Black0 (Crust)
        curses.init_pair(17, 234, -1)  # Black1 (Mantle)
        curses.init_pair(18, 235, -1)  # Black2 (Base)
        curses.init_pair(20, 229, -1)  # Light Golden Yellow
        curses.init_pair(21, 228, -1)  # Soft Yellow
        curses.init_pair(22, 187, -1)  # Light Tan Yellow
        curses.init_pair(23, 186, -1)  # Sandy Yellow
        curses.init_pair(24, 222, -1)  # Bright Sand (Warm Yellow)
        curses.init_pair(25, 221, -1)  # Orange-Yellow
        curses.init_pair(26, 114, -1)  # Darker green, close to Latte green
        curses.init_pair(27, 94, -1) # brown
        curses.init_pair(28, curses.COLOR_WHITE, -1)
        curses.init_pair(29, 130, -1) # brown

    def draw_pixel(self, y, x, char='██', color=1):
        self.pixels.append((y, x, char, color))

    def clear(self):
        self.pixels.clear()
        self.stdscr.clear()

    def render(self):
        for y, x, char, color in self.pixels:
            try:
                self.stdscr.addstr(y, x, char, curses.color_pair(color))
            except curses.error:
                pass
        self.stdscr.refresh()

    def get_key(self):
        return self.stdscr.getch()

    def sleep(self, secs):
        time.sleep(secs)
