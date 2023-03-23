class CollisionObject:
    def __init__(self, x, y, width, height):
        self._left_x = int(x - width/2)
        self._right_x = int(x + width/2)
        self._top_y = int(y - height/2)
        self._bottom_y = int(y + height/2)

        self._width = width
        self._heigth = height

        self._x = x
        self._y = y

    def get_corners_for_rec(self):
        return [self._left_x, self._top_y, self._right_x, self._bottom_y]