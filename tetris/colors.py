class Colors:
    dark_grey = (26, 31, 40)
    green = (33, 156, 144)
    red = (236, 83, 176)
    orange = (249, 76, 16)
    yellow = (233, 184, 36)
    purple = (216, 180, 248)
    cyan = (64, 248, 255)
    blue = (14, 33, 160)
    white = (255, 255, 255)
    dark_blue = (46, 67, 116)
    light_blue = (202, 237, 255)

    @classmethod
    def get_cell_colors(cls):
        return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]