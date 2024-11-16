import random

class Ball:
    def __init__(self, mass):
        self.mass = mass
        self.image = "NMX"
        self.x, self.y = 0, 0

    def get_random_model(self):
        cj = ['Nike', 'Adidas', 'Reebok', 'Puma', 'Converse']

        res = random.choice(cj)
        return res

    def get_random_num(self, max_length):
        return random.randint(1, max_length)

    def drop(self):
        self.y += 1
        return 'Я подбросился на', self.y
    def kick(self):
        self.x += 1
        return "Меня пнули на ", self.x

ball = Ball(10)

print(ball.mass, ball.image)
print(ball.get_random_model())

print(ball.get_random_num(max_length=100))
for _ in range(10):
    print(ball.drop(), ball.y)
    print(ball.x, ball.y)
