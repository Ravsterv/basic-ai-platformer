import random
from climb_agent import ClimbAgent

class Game:
    def __init__(self, gen_size):
        # create a step counter(Program will run at 10 frames per second so 100milli seconds per frame)
        # It will also Ech Step will go for 5 frame(0.5 second) Can change if needed
        # make gravity and such dynamic(change if the frame rate is changed
        self._players = []
        self._generation = 0
        self._gen_size = gen_size
        self._step = 0
        self._frame = 0 # Used to keep track of when to allow the next move to perform
        self._obstacles = []
        self._frames_per_sec = 10
        self._interval = int((1/self._frames_per_sec)*1000)
        # print(self._interval)
        self._possible_actions = ["left", "right", "jump", "stop"]
        self._gravity = 9.8/self._frames_per_sec # Normally 9.8 m/s so it is 9.8/frames_per_second
        # To detect the floor, shoot a small lazer which if it collides with an obstacle it should snap to it's top
        # But only if it collides with the lazer, otherwise bounce off
        #using the direction of the speed I should be able to snap to edges

    def get_frame_rate(self):
        return self._frames_per_sec

    def get_interval(self):
        return self._interval

    def get_frame_count(self):
        return self._frame

    def set_agents(self, agents):
        self._players = agents

    def add_agent(self, agent):
        self._players.append(agent)

    def add_obstacle(self, obstacle):
        self._obstacles.append(obstacle)

    def add_obstacles(self, obstacles):
        for obstacle in obstacles:
            self._obstacles.append(obstacle)

    def set_obstacles(self, obstacles):
        self._obstacles = obstacles

    def get_generation(self):
        return self._generation

    def get_step(self):
        return self._step

    def calculate_average_fitness(self):
        fit_sum = 0
        for player in self._players:
            fit_sum += player.get_fitness()
        return fit_sum/self._gen_size

    def get_obstacles(self):
        return self._obstacles

    def get_agents(self):
        return self._players

    def reset_sim(self):
        # Called when it reaches the end of the moveset
        # Will handle Reseting the sim, creating the new players, mutating the new players,
        # Adding on more moves every 10 generations
        # Based of Fitness score
        #
        self._step = 0
        self._generation += 1
        self._frame = 0
        choose = int(self._gen_size/2)
        new_players = []

        while len(new_players) < choose:
            max_fitness = -1
            player_index = 0
            for index, player in enumerate(self._players):
                if player.get_fitness() > max_fitness:
                    max_fitness = player.get_fitness()
                    player_index = index

            new_players.append(self._players[player_index].get_actions())
            self._players.pop(player_index)


        # Create new moves if generation a %10 == 0

        if self._generation % 10 == 0:
            for player in new_players:
                for i in range(5):
                    player.append(self._possible_actions[random.randint(0, 3)])


        # Do mutation after putting them into the game To actually give variety

        # vprint(player)
        # Now check if an extra 5 moves should be added
        # Mutate a move from the last five moves
        # Generate a number between 0,10 if it is 1 or less mutate 1 move
        # CHoose a random num between 1,6(mover to change)
        # Generate new climb agents

        self._players = []
        for i in range(self._gen_size):
            select = i % choose
            agent = ClimbAgent(900, 770)
            agent.create_set_agent(new_players[select].copy())
            agent.mutate_agent()
            self._players.append(agent)

        # print(len(self._players))


    def step(self):
        """
        Passes though every agent and sees how they end up after the tick, draw function is also on its own timer
        The GUI access the game to be able to draw the field but the game does not need access to GUI really
        :return:
        """
        # If current action is greater than the len, use a method in game to recreate the characters
        # and mutate them, also increment generation
        # TODO: Implement player actions and repeating/mutations
        # apply affects of gravity on agents(Add acceleration to them and then add to y)
        # print(self._interval)
        if self._frame % 5 == 0:
            self._step += 1


        for player in self._players:
            """
            if player.get_ground():
                pass
            else:
            """
            # Calculate if a move should be done
            # Take Action: frames%5 == 0

            if self._frame % 5 == 0:

                action = player.get_current_action()
                player.increment_action()
                # print(action)

                if action == "left":
                    player.set_x_speed(-4)
                if action == "right":
                    player.set_x_speed(4)
                if action == "stop":
                    player.set_x_speed(0)
                if action == "jump":
                    if player.get_ground():
                        player.set_y_speed(-12)


            # Do y speed
            player.add_y_speed(self._gravity)

            player.set_y(player.get_y() + player.get_y_speed())
            player.set_x(player.get_x() + player.get_x_speed())
            # Do x speed and agent actions
            player.update_all()

        for player in self._players:


            for obstacle in self._obstacles:
                obstacle_corners = obstacle.get_corners_for_rec()
                block_left, block_top, block_right, block_bottom = obstacle_corners
                points = player.get_colliders()


                if ((points["bottom"] > block_top and points["bottom"] < block_bottom)
                        and ((points["bottom_left"] > block_left and points["bottom_left"] < block_right)
                        or (points["bottom_right"] > block_left and points["bottom_right"] < block_right))):
                    player.set_y(player.get_y() - (points["bottom"] - block_top))
                    player.ground()

                    # player.update_all()

                if ((points["top"] < block_bottom and points["top"] > block_top)
                        and ((points["width_mid"] > block_left and points["width_mid"] < block_right))):
                    player.set_y(player.get_y() + (block_bottom - points["top"]))
                    player.set_y_speed(0)

                if (points["height_mid"] > block_top and points["height_mid"] < block_bottom):
                    if ((points["right"] > block_left and points["right"] < block_right)):

                        player.set_x(player.get_x() - (points["right"] - block_left))

                    elif ((points["left"] < block_right and points["right"] > block_left)):
                        player.set_x(player.get_x() + (block_right - points["left"]))
            if player.get_y_speed() == 0:
                pass
            else:
                player.no_ground()

            player.calculate_fitness()

        # Stop frame from getting too big
            player.update_all()
        self._frame += 1
        """
        if self._frame == 6:
            self._frame = 1
            """
        # print(self._step)
        if self._step >= self._players[0].get_action_size():
            self.reset_sim()

            # print(player.get_ground())
