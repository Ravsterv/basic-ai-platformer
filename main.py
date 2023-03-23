import tkinter as tk
from Game import Game
from climb_agent import ClimbAgent
from CollisionObject import CollisionObject
from GUI import GUI

# use step to go through all the parts
def main():
    gen_size = 40
    root = tk.Tk()
    root.geometry("1000x800")
    game = Game(gen_size)

    # Generate Starting Agents
    for i in range(gen_size):
        agent = ClimbAgent(900, 770)
        agent.create_random_agent()
        game.add_agent(agent)

    # Add objects
    game.add_obstacle(CollisionObject(800, 750, 20, 20))
    game.add_obstacle(CollisionObject(710, 695, 40, 20))

    game.add_obstacle(CollisionObject(730, 620, 40, 20))

    game.add_obstacle(CollisionObject(850, 600, 40, 20))

    game.add_obstacle(CollisionObject(950, 550, 80, 20))

    game.add_obstacle(CollisionObject(870, 440, 40, 20))



    # Add Walls
    game.add_obstacle(CollisionObject(500, 790, 1000, 20))
    game.add_obstacle(CollisionObject(10, 400, 20, 1000))
    game.add_obstacle(CollisionObject(990, 400, 20, 1000))
    gui = GUI(root, game)

    gui.draw()

    root.mainloop()

if __name__ == "__main__":
    main()