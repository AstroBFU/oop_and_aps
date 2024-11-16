import random

class Ball:
    def __init__(self, mass):
        self.mass = mass
        self.image = "NMX"

    def get_random_model(self):
        cj = ['Nike', 'Adidas', 'Reebok', 'Puma', 'Converse']

        res = random.choice(cj)
        return res

ball = Ball(10)

print(ball.mass, ball.image)
print(ball.get_random_model())