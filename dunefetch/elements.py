ELEMENTS_DIC = [
    {"name": "EMPTY", "color": [15], "symbol": '  '},
    {"name": "SAND", "color": [24, 25, 25, 25, 25], "symbol": '██'},
    #  [21, 24, 25]
    {"name": "WATER", "color": [11, 13], "symbol": '██'},  # ▒▒
    {"name": "WALL", "color": [15], "symbol": '██'},
    {"name": "OIL", "color": [12], "symbol": '▒▒'},
    {"name": "FIRE", "color": [5, 1, 2, 21, 5, 25, 25, 5, 5], "symbol": '██'},
    {"name": "PLANT", "color": [26], "symbol": '██'},
    {"name": "STEAM", "color": [11, 12, 13], "symbol": '▒▒'},
    {"name": "WOOD", "color": [27], "symbol": "██"},
    {"name": "MUD", "color": [29], "symbol": "██"}
]

ELEMENTS = {}
COLORS = {}
SYMBOLS = {}
NAME_TO_INDEX = {}
INDEX_TO_NAME = {}

for index, element in enumerate(ELEMENTS_DIC):
    name = element["name"]

    ELEMENTS[name] = {
        "index": index,
        "color": element["color"],
        "symbol": element["symbol"]
    }

    COLORS[index] = element["color"]
    SYMBOLS[index] = element["symbol"]

    NAME_TO_INDEX[name] = index
    INDEX_TO_NAME[index] = name

globals().update(NAME_TO_INDEX)
