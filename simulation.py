import turtle
import random
from ball import Ball
class Simulation:
    def __init__(self, num_balls):
        self.num_balls = num_balls
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        self.ball_radius = 0.05 * self.canvas_width
        self.balls = []

    def initialize_balls(self):
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        turtle.colormode(255)

        for _ in range(self.num_balls):
            x = random.uniform(-1 * self.canvas_width + self.ball_radius, self.canvas_width - self.ball_radius)
            y = random.uniform(-1 * self.canvas_height + self.ball_radius, self.canvas_height - self.ball_radius)
            vx = random.uniform(1, 0.01 * self.canvas_width)
            vy = random.uniform(1, 0.01 * self.canvas_height)
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            ball = Ball(color, self.ball_radius, x, y, vx, vy)
            self.balls.append(ball)

    def update_state(self):
        for ball in self.balls:
            ball.move_circle(self.canvas_width, self.canvas_height)

    def draw_balls(self):
        turtle.clear()
        for ball in self.balls:
            ball.draw_circle()
        turtle.update()

    def run_simulation(self):
        self.initialize_balls()
        while True:
            self.draw_balls()
            self.update_state()

        turtle.done()
