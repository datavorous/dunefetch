import curses
import random
from dunefetch.elements import *
from dunefetch.cursu import cursu
from dunefetch.sand_core import SandCore
from dunefetch.utils import *
# import os
import argparse
import sys


width, height = 30, 30


def parse_args():
    parser = argparse.ArgumentParser(description="Dunefetch - a neofetch-style terminal particle sim.")
    parser.add_argument("--version", action="store_true", help="show version info and exit")
    parser.add_argument("--help-controls", action="store_true", help="show keyboard controls and exit")
    return parser.parse_args()


def main(stdscr):
    # os.system('printf "\e[8;40;100t"')
    # global cpu_percent
    # weather_condition = get_weather("Kolkata")
    
    pause = False
    
    app = cursu(stdscr)
    sim = SandCore(width=width, height=height)
    spawn_y, spawn_x = width//2, height//2  # random.randint(0, 20), random.randint(0, 30)
    
    while True:
        app.clear()
        if not pause:
            sim.update_physics()
        
        # rendering stuff
        for y in range(1, sim.height-1):
            for x in range(1, sim.width-1):
                p = sim.get(y, x)
                if p != EMPTY:
                    app.draw_pixel(y+2, x*2+2, SYMBOLS[p], color=get_color(p))
        app.draw_pixel(spawn_y+2, spawn_x*2+2, "██", color=get_color(sim.selected_material))

        panel_x = sim.width * 2 + 5
        system_info = get_system_info()
        
        ascii_start_y = 1
        for i, line in enumerate(ascii_face):
            app.draw_pixel(ascii_start_y + i, panel_x, line, color = 15)
            
        magic_number = len(ascii_face) + 1
        app.draw_pixel(2 + magic_number, panel_x, "┏━━━ ◆ SYSTEM INFO ◆ ━━━━", color=14 | curses.A_BOLD)
        for i, (label, value) in enumerate(system_info):
            app.draw_pixel(3 + i + magic_number, panel_x, f"┃ {label}: {value}", color = 15)

             
        app.draw_pixel(3 + len(system_info) + 1 + magic_number, panel_x, "┏━━━ ◆ SIMULATION ◆ ━━━━", color=14 | curses.A_BOLD)
        app.draw_pixel(3 + len(system_info) + 2 + magic_number, panel_x, f"┃ ▲ Material: {ELEMENTS_DIC[sim.selected_material]['name']}", color=ELEMENTS_DIC[sim.selected_material]["color"][0])
        particle_count = count_particles(sim)
        app.draw_pixel(3 + len(system_info) + 3 + magic_number, panel_x, f"┃ ▲ Particles: {particle_count}", color=15)
        
        app.draw_pixel(3 + len(system_info) + 4 + magic_number, panel_x, f"┃ ▲ Spawner: ({spawn_y}, {spawn_x})", color = 15)
        app.draw_pixel(3 + len(system_info) + 5 + magic_number, panel_x, f"┃ ▲ Status: {'Paused' if pause else 'Running'}", color= 15)
        
        # app.draw_pixel(3 + len(system_info) + 7, panel_x, "┏━━━ ◆ WEATHER ◆ ━━━━", color=15 | curses.A_BOLD)
        # app.draw_pixel(3 + len(system_info) + 8, panel_x, f"┃ ▲ Weather: {weather_condition}", color=13)
        # app.draw_pixel(3 + len(system_info) + 7, panel_x, "█"*int(100*(particle_count/1800)), color = 5)
        # should have used mapping similar to p5js
   
        app.render()
        
        # input handling 4
        key = app.get_key()
        
        if key == ord('q'):
            break
        
        elif key == ord('p'):
            pause = not pause
            
        elif key == curses.KEY_UP and spawn_y > 0:
            spawn_y -= 1
        elif key == curses.KEY_DOWN and spawn_y < sim.height-1:
            spawn_y += 1
        elif key == curses.KEY_LEFT and spawn_x > 0:
            spawn_x -= 1
        elif key == curses.KEY_RIGHT and spawn_x < sim.width-1:
            spawn_x += 1
        
        elif key == ord(' '):
            for _ in range(5):
                dy, dx = 0, 0
                if not ((sim.selected_material == WALL) or (sim.selected_material == WOOD)):
                    dy, dx = random.randint(-1,1), random.randint(-1,1)
                sim.add_particle(spawn_y+dy, spawn_x+dx, sim.selected_material)
                
        elif key in (ord('1'),ord('2'),ord('3'),ord('4'),ord('5'), ord('6'), ord('7'), ord('8'), ord('9')):
            sim.selected_material = int(chr(key))
            
        elif key == ord('c'):
            # TODO: need to add another elif to manage brush radius
            sim.clear_area(spawn_y, spawn_x)
            
        elif key == ord('r'):
            sim = SandCore(width=width, height=height)
            
        app.sleep(0.02)


def run():
    args = parse_args()

    if args.version:
        print("dunefetch v0.1.0")
        print("Author: datavorous")
        print("License: MIT")
        print("Description: neofetch + falling sand engine for your terminal.")
        sys.exit(0)

    if args.help_controls:
        print("dunefetch controls:")
        print("  Arrow keys  -> Move spawn cursor")
        print("  [Space]     -> Place selected material")
        print("  1 - 8       -> Select material:")
        # print("               1. EMPTY")
        print("               1. SAND")
        print("               2. WATER")
        print("               3. WALL")
        print("               4. OIL")
        print("               5. FIRE")
        print("               6. PLANT")
        print("               7. STEAM")
        print("               8. WOOD")
        print("  p           -> Pause/unpause simulation")
        print("  c           -> Clear particles near cursor")
        print("  r           -> Reset simulation")
        print("  q           -> Quit")
        sys.exit(0)

    curses.wrapper(main)

