from paddle import Paddle


class Brick(Paddle):
    def __init__(self, pos, color):
        super().__init__(pos)
        self.color(color)
        self.shapesize(stretch_wid=0.8, stretch_len=3)
        self.half_width = self.shapesize()[0] * 10 / 2  # Multiply by 10 to convert from pixels to turtle units
        self.half_height = self.shapesize()[1] * 10 / 2
