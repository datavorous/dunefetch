# import json
# import requests
import os
import platform
import psutil
import time
from dunefetch.elements import * 
import random

ascii_art = """
┏━━━━━━━━ ◆ SAND BOX ◆ ━━━━━━━
┃ ⣿⡇⣿⣿⣿⠛⠁⣴⣿⡿⠿⠧⠹⠿⠘⣿⣿⣿⡇⢸⡻⣿⣿⣿⣿⣿⣿⣿
┃ ⢹⡇⣿⣿⣿⠄⣞⣯⣷⣾⣿⣿⣧⡹⡆⡀⠉⢹⡌⠐⢿⣿⣿⣿⡞⣿⣿⣿
┃ ⣾⡇⣿⣿⡇⣾⣿⣿⣿⣿⣿⣿⣿⣿⣄⢻⣦⡀⠁⢸⡌⠻⣿⣿⣿⡽⣿⣿
┃ ⡇⣿⠹⣿⡇⡟⠛⣉⠁⠉⠉⠻⡿⣿⣿⣿⣿⣿⣦⣄⡉⠂⠈⠙⢿⣿⣝⣿
┃ ⠤⢿⡄⠹⣧⣷⣸⡇⠄⠄⠲⢰⣌⣾⣿⣿⣿⣿⣿⣿⣶⣤⣤⡀⠄⠈⠻⢮
┃ ⠄⢸⣧⠄⢘⢻⣿⡇⢀⣀⠄⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠄⢀
┃ ⠄⠈⣿⡆⢸⣿⣿⣿⣬⣭⣴⣿⣿⣿⣿⣿⣿⣿⣯⠝⠛⠛⠙⢿⡿⠃⠄⢸
┃ ⠄⠄⢿⣿⡀⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⡾⠁⢠⡇⢀
┃ ⠄⠄⢸⣿⡇⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⣫⣻⡟⢀⠄⣿⣷⣾
┃ ⠄⠄⢸⣿⡇⠄⠈⠙⠿⣿⣿⣿⣮⣿⣿⣿⣿⣿⣿⣿⣿⡿⢠⠊⢀⡇⣿⣿
┃ ⠒⠤⠄⣿⡇⢀⡲⠄⠄⠈⠙⠻⢿⣿⣿⠿⠿⠟⠛⠋⠁⣰⠇⠄⢸⣿⣿⣿
"""
ascii_face = ascii_art.strip().split('\n')


def get_system_info():
    uname = platform.uname()
    boot_time = psutil.boot_time()
    uptime = time.time() - boot_time
    uptime_str = time.strftime("%Hh %Mm %Ss", time.gmtime(uptime))
    mem = psutil.virtual_memory()
    process = psutil.Process()
    process_mem = process.memory_info()
    
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory().percent
    
    info = [
        ("▲ User", os.getlogin()),
        ("▲ OS", uname.system),
        ("▲ Release", uname.release),
        # ("● Kernel", uname.version.split()[0] if uname.version else "Unknown"),
        ("▲ Uptime", uptime_str),
        ("▲ Machine", uname.machine),
        # ("● CPU", platform.processor() or uname.processor or "Unknown"),
        # ("● Cores", f"{psutil.cpu_count(logical=True)}"),
        ("▲ RAM Total", f"{round(mem.total / (1024**3), 1)} GB"),
        ("▲ Python", platform.python_version()),
        ("▲ CPU Usage:", f"{cpu_percent}%"),
        ("▲ RAM Usage:", f"{memory_percent}%"),
        ("▲ Process CPU", f"{process.cpu_percent()}%"),
        ("▲ Process RAM", f"{round(process_mem.rss / (1024**2), 1)} MB")
    ]
    return info

def count_particles(sim):
    count = 0
    for y in range(sim.height):
        for x in range(sim.width):
            if sim.get(y, x) != EMPTY:
                count += 1
    return count

def get_color(index):
    color = COLORS[index]
    if isinstance(color, list):
        return random.choice(color)
    return color

'''
def get_weather(city="Delhi"):
    try:
        url = f"https://wttr.in/{city}?format=1"
        response = requests.get(url)
        if response.status_code == 200:
            return response.text.strip()
        else:
            return "Weather unavailable"
    except Exception:
        return "Error fetching weather"
'''