import tkinter as tk

class GUI:
    def __init__(self, root, game):
        self._root = root
        self._game = game
        self._main_view = tk.Canvas(self._root, bg="grey")
        self._main_view.pack(expand=True, fill=tk.BOTH)


        self._main_view.create_text(10, 10, text=f"Generation: {game.get_generation()}")
        self._main_view.create_text(10, 40, text=f"Step: {game.get_step()}")
        self._main_view.create_text(10, 70, text=f"Average Fitness: {game.calculate_average_fitness()}")

    def draw(self):
        self._game.step()
        self._main_view.delete("all")

        self._main_view.create_text(40, 10, text=f"Generation: {self._game.get_generation()}")
        self._main_view.create_text(40, 40, text=f"Step: {self._game.get_step()}")
        self._main_view.create_text(40, 70, text=f"Average Fitness: {self._game.calculate_average_fitness()}")

        obstacles = self._game.get_obstacles()
        for obstacle in obstacles:
            c = obstacle.get_corners_for_rec()
            self._main_view.create_rectangle(c[0], c[1], c[2], c[3], fill="red")

        agents = self._game.get_agents()
        for agent in agents:
            c = agent.get_corners()
            self._main_view.create_rectangle(c[0], c[1], c[2], c[3], fill="red")
        # Draw Agents
        # Draw Obstacles
        #Thats all for now

        self._root.after(self._game.get_interval(), self.draw)

