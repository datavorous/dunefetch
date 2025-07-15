from dunefetch.elements import * 


class SandUtils:
    def __init__(self, width=80, height=40):
        self.width = width
        self.height = height
        
        self.grid = [[EMPTY for _ in range(width)] for _ in range(height)]
        self.create_boundaries()
        self.life = [[0]*width for _ in range(height)]
        
        # self.color_map = [[None for _ in range(width)] for _ in range(height)]
        # self.color_map = {}  # (y, x) : color
        
        # self.max_fire_life = 5
        # self.selected_material = SAND
    
    def create_boundaries(self):
        self.grid[0] = [EMPTY] * self.width
        self.grid[-1] = [EMPTY] * self.width
        
        for row in self.grid:
            row[0] = row[-1] = EMPTY 
        '''
        # can I do this in a single pass with some trick?
        # TODO: think in terms of flattening
        for x in range(self.width):
            self.grid[self.height - 1][x] = EMPTY
        for y in range(self.height):
            self.grid[y][0] = EMPTY
            self.grid[y][self.width - 1] = EMPTY
        '''
    
    def is_valid(self, y, x):
        return 0 <= y < self.height and 0 <= x < self.width
    
    def get(self, y, x):
        return self.grid[y][x] if self.is_valid(y, x) else EMPTY
    
    def set(self, y, x, val):
        if not self.is_valid(y, x):
            return
        self.grid[y][x] = val
            # if val == FIRE:
                # self.life[y][x] = self.max_fire_life
    
    def swap(self, y1, x1, y2, x2):
        if self.is_valid(y1, x1) and self.is_valid(y2, x2):
            self.grid[y1][x1], self.grid[y2][x2] = self.grid[y2][x2], self.grid[y1][x1]
            self.life[y1][x1], self.life[y2][x2] = self.life[y2][x2], self.life[y1][x1]