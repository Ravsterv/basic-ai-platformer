import random

class ClimbAgent:
    # Basic as in it isn't really a true AI, It can't adapt to any changes in the environment
    # Con't deal with random seeds
    # But it can learn its fixed environment very well
    def __init__(self, x, y):
        self._actions = []
        self._possible_actions = ["left", "right", "jump", "stop"]

        self._current_action = 0
        self._max_y_speed = 8
        self._y_speed = 0
        self._x_speed = 0

        self._width = 20
        self._height = 20
        self._x = x
        self._y = y
        self._corners = [int(x-self._width/2),
                         int(y - self._height/2),
                         int(x+self._width/2),
                         int(y + self._height/2)]

        self._colliding_points = {
            "top": self._y - self._height * 0.5,
            "bottom": self._y + self._height * 0.5,
            "left": self._x - self._width * 0.5,
            "right": self._x + self._width * 0.5,
            "height_mid": self._y,
            "width_mid": self._x,
            "bottom_left": self._x - (self._width * 0.5) * 0.4,
            "bottom_right": self._x + (self._width * 0.5) * 0.4,
        }
        self._fitness = 0
        self._grounded = False

        # Action Description:
        #   left: Move the character left at a set velocity
        #   right: Move character right at a set velocity
        #   jump: move the character move in the vertical direction, keeping any and all horizontal velocity
        #   stop: make the character stop moving

    def ground(self):
        self._grounded = True
        self._y_speed = 0

    def no_ground(self):
        self._grounded = False

    def increment_action(self):
        self._current_action += 1

    def calculate_fitness(self):
        if self._grounded:
            self._fitness = 800 - self._y

    def mutate_agent(self):
        mutate = random.randint(0, 10)
        if mutate <= 8:
            # print(player)
            mutate_action = random.randint(1, 5)
            new_action = random.choice(self._possible_actions)
            self._actions[-mutate_action] = new_action


    def get_fitness(self):
        return self._fitness

    def get_current_action(self):
        return self._actions[self._current_action]

    def get_actions(self):
        return self._actions

    def get_action_size(self):
        return len(self._actions)

    def get_y_speed(self):
        return self._y_speed

    def get_x_speed(self):
        return self._x_speed

    def add_y_speed(self, acceleration):
        self._y_speed += acceleration
        if self._y_speed > self._max_y_speed:
            self._y_speed = self._max_y_speed

    def set_y_speed(self, speed):
        self._y_speed = speed

    def set_x_speed(self, speed):
        self._x_speed = speed

    def create_random_agent(self):
        for i in range(5):
            self._actions.append(self._possible_actions[random.randint(0, 3)])

    def get_possible_actions(self):
        return self._possible_actions

    def create_set_agent(self, actions):
        self._actions = actions

    def update_corners(self):
        self._corners = [int(self._x - self._width / 2),
                         int(self._y - self._height / 2),
                         int(self._x + self._width / 2),
                         int(self._y + self._height / 2)]

    def update_collider_points(self):
        self._colliding_points = {
            "top": self._y - self._height * 0.5,
            "bottom": self._y + self._height * 0.5,
            "left": self._x - self._width * 0.5,
            "right": self._x + self._width * 0.5,
            "height_mid": self._y,
            "width_mid": self._x,
            "bottom_left": self._x - (self._width * 0.5) * 0.4,
            "bottom_right": self._x + (self._width * 0.5) * 0.4,
        }

    def update_all(self):
        self.update_corners()
        self.update_collider_points()

    def get_colliders(self):
        return self._colliding_points

    def get_ground(self):
        return self._grounded

    def set_y(self, y):
        self._y = y

    def set_x(self, x):
        self._x = x

    def get_y(self):
        return self._y

    def get_x(self):
        return self._x

    def get_moves(self):
        return self._actions

    def get_corners(self):
        return self._corners