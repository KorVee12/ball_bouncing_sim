import turtle
import random
from simulation import Simulation

num_balls = int(input("Number of balls to simulate: "))
simulation = Simulation(num_balls)
simulation.run_simulation()