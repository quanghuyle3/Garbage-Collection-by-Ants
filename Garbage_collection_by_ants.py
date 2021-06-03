
import random
import numpy as np
from matplotlib import pyplot as plt
import pycxsimulator

n = 50  # number of ants
w = 10  # number of rows in 2D space
h = 10  # number of collunms in 2D space
init_garbage_ground = 40  # number of garbage on ground


class Agent():
    def __init__(self):
        # currently carrying garbage: True or False
        self.have_garb = random.choice([True, False])
        # set 1 garbage if ant is carrying
        self.num_carryings = 1 if self.have_garb else 0

        self.x = random.randrange(w)
        self.y = random.randrange(h)


def initialize():
    global ants, space

    # Create an array to represent the 2D space
    space = np.zeros([w, h])

    # Scatter garbage on ground
    for i in range(init_garbage_ground):
        x = random.randrange(w)
        y = random.randrange(h)
        space[x][y] += 1

    # Create a list holding all agents
    ants = []

    # Create ants
    for i in range(n):
        ant = Agent()
        ants.append(ant)


def update():
    global ants, space

    # Select one ant to wander to other place randomly
    ag = random.choice(ants)
    ag.x = random.randint(0, w - 1)
    ag.y = random.randint(0, h - 1)

    if space[ag.x][ag.y] > 0:  # That specific location has garbage
        if ag.have_garb == True:   # ant is carrying garbage --> PUTTING IT DOWN

            ag.num_carryings -= 1
            ag.have_garb = False
            space[ag.x][ag.y] += 1   # that location will have 1 more garbage

        else:   # ant isn't carrying any
            # pick up garbage from ground and start carrying
            space[ag.x][ag.y] -= 1
            ag.num_carryings += 1
            ag.have_garb = True


def observe():
    global ants, space

    plt.cla()
    # plot grabage
    plt.imshow(space, cmap=plt.cm.binary)
    plt.axis('image')

    # plot ants
    ant_x = [a.x for a in ants]
    ant_y = [a.y for a in ants]

    plt.plot(ant_x, ant_y, 'b.')


pycxsimulator.GUI().start(func=[initialize, observe, update])
