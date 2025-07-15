from dunefetch.sand_utils import SandUtils
from dunefetch.elements import *
import random


class SandCore(SandUtils):
    def __init__(self, width=80, height=40):
        super().__init__(width, height)
        self.selected_material = SAND
        self.max_fire_life = 7
    
    def set(self, y, x, val):
        super().set(y, x, val)
        if val == FIRE:
            self.life[y][x] = self.max_fire_life
    
    def update_sand(self, y, x):
        if self.get(y + 1, x) in [EMPTY, WATER, OIL]:
            self.swap(y, x, y + 1, x)
            return True
        for dx in (-1,1):
            if self.get(y + 1, x + dx) in [EMPTY, WATER, OIL]:
                self.swap(y, x, y + 1, x + dx)
                return True
        return False
    
    def update_mud(self, y, x):
        if self.get(y + 1, x) in [EMPTY, WATER, OIL, SAND]:
            self.swap(y, x, y + 1, x)
            return True
        for dx in (-1,1):
            if self.get(y + 1, x + dx) in [EMPTY, WATER, OIL, SAND]:
                self.swap(y, x, y + 1, x + dx)
                return True
        return False
    
    def update_water(self, y, x):
        if self.get(y + 1, x) == EMPTY:
            self.swap(y, x, y + 1, x)
            return True
        for dx in random.sample([-1,1],2):
            if self.get(y, x + dx) == EMPTY:
                self.swap(y, x, y, x + dx)
                return True
        return False
    
    def update_oil(self, y, x):
        # THIS IS NOT OIL THIS IS NOT OIL
        # THIS IS SLIMY SOMETHING
        # this part is fucked beyond comprehension
        below = self.get(y + 1, x)
        if below == EMPTY or below == WATER:
            self.swap(y, x, y + 1, x)
            return True
        for dx in random.sample([-1,1],2):
            if self.get(y, x + dx) in (EMPTY, WATER):
                self.swap(y, x, y, x + dx)
                return True
        return False
    
    def update_fire(self, y, x):
        if self.life[y][x] <= 0:
            self.set(y, x, EMPTY)
            return False

        for dy, dx in [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1,  0), (1,  0), (0, -1), (0,  1)]:
            target = self.get(y + dy, x + dx)
            if target == WATER:
                self.set(y + dy, x + dx, STEAM)
                
            if target in (OIL, PLANT):
                self.set(y+dy, x+dx, FIRE)
                # giving fire a full life or a boosted one
                self.life[y+dy][x+dx] = self.max_fire_life + 2
                
            if target == WOOD:
                if random.random() < 0.7:
                    self.set(y+dy, x+dx, FIRE)
                    self.life[y+dy][x+dx] = self.max_fire_life + 5
                    # wood burns longer hence this
        
        # occasionally it can leap two cells
        if random.random() < 0.0001:
            dy, dx = random.choice([(-2,0), (2,0), (0,-2), (0,2)])
            ny, nx = y + dy, x + dx
            if 0 < ny < self.height-1 and 0 < nx < self.width-1:
                if self.get(ny, nx) == EMPTY:
                    self.set(ny, nx, FIRE)
                    self.life[ny][nx] = self.max_fire_life
                    
        decay = random.randint(1, 2)
        self.life[y][x] = max(0, self.life[y][x] - decay)

        return True
    
    def update_plant(self, y, x):
        
        for dy, dx in random.sample([(-1, 0), (1,0), (0, -1), (0, 1)], 4):
            if self.get(y + dy, x + dx) == WATER and random.random() < 0.02:
                self.set(y + dy, x + dx, PLANT)
                break
            elif self.get(y + dy, x + dx) == EMPTY and random.random() < 0.002:
                self.set(y + dy, x + dx, PLANT)
                break
        # if  (self.get(y + 1, x) == WATER or self.get(y + 1, x + 1) == WATER):
          #  self.set(y, x, PLANT)
           #  return 
        # spreading 
        '''
        if random.random() < 0.009:
            for dy, dx in random.sample([(-1, 0), (1,0), (0, -1), (0, 1)], 4):
                if self.get(y + dy, x + dx) == EMPTY:
                    self.set(y + dy, x + dx, PLANT)
                    break'''
                    
                    
    def update_steam(self, y, x):
        #if random.random() < 0.09:
         #   self.set(y, x, EMPTY)
          #  return

        maybe = random.randint(-1, 1)
        if self.get(y - 1, x + maybe) == EMPTY and y - 1 > 0:
            self.swap(y, x, y - 1, x + maybe)
            return
        
        if y < 2 and random.random() < 0.01:
            self.set(y, x, WATER)

        #for dx in random.sample([-1, 1], 2):
            #if self.get(y, x + dx) == EMPTY:
             #   self.swap(y, x, y, x + dx)
              #  return
              
    def clear_borders(self):
        #for x in range(self.width):
         #   self.set(0, x, EMPTY)
          #  self.set(self.height-1, x, EMPTY)
        for y in range(1, self.height-1):
            self.set(y, 0, EMPTY)
            self.set(y, self.width-1, EMPTY)

    def update_physics(self):
        for y in range(self.height - 1, -1, -1):
            for x in range(1, self.width - 1):
                p = self.get(y, x)
                if p == SAND:
                    self.update_sand(y, x)
                elif p == WATER:
                    self.update_water(y, x)
                elif p == OIL:
                    self.update_oil(y, x)
                elif p == FIRE:
                    self.update_fire(y, x)
                elif p == PLANT:
                    self.update_plant(y, x)
                elif p == MUD:
                    self.update_mud(y, x)
                # elif p == STEAM:
                  #  self.update_steam(y, x)
                    
        for y in range(1, self.height - 1):
            for x in range(1, self.width - 1):
                p = self.get(y, x)
                if p == STEAM:
                    self.update_steam(y, x)
        # self.clear_borders()
    
    def add_particle(self, y, x, particle_type):
        if 0 <= y < self.height - 1 and 1 <= x < self.width - 1:
            if self.get(y, x) == EMPTY:
                self.set(y, x, particle_type)
            
    def clear_area(self, y, x, radius=2):
        for dy in range(-radius, radius+1):
            for dx in range(-radius, radius+1):
                if dy*dy + dx*dx <= radius*radius:
                    self.set(y + dy, x + dx, EMPTY)