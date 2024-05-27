import pygame
import random
import os

# place Pygame window at a specific location
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (50, 50)

class Vehicle:
    def __init__(self, color: str = "blue", x: int = 400, y: int = 400) -> None:
        self.img_path: str = "sedan_" + color + ".png"
        self.location: tuple[int, int] = (x, y)
        self.draw()

    def draw(self):
        # load image and set its location
        self.img = pygame.image.load(self.img_path)
        self.img_location = self.img.get_rect(center=self.location)

class Truck(Vehicle):
    def __init__(self, x, y, kind="truck_tractor") -> None:
        self.kind = kind
        super().__init__(color="green", x=x, y=y)
        self.img_path = self.kind + ".png"
        self.draw()

class Police(Vehicle):
    def __init__(self, x, y) -> None:
        super().__init__(color="green", x=x, y=y)
        self.img_path = "police_car.png"
        self.draw()

# pygame settings
pygame.init()
screen = pygame.display.set_mode((800, 800))
running = True

cars = []
for i in range(10):
    color = random.choice(["blue", "red", "green"])
    x = random.randint(0, 800)
    y = random.randint(0, 800)
    car_class = random.choice(["sedan", "truck", "police"])
    if car_class == "sedan":
        cars.append(Vehicle(color, x, y))
    elif car_class == "truck":
        truck_kind = random.choice(["truck_tractor", "box_truck"])
        cars.append(Truck(x, y, truck_kind))
    elif car_class == "police":
        cars.append(Police(x, y))

# set background color
screen.fill("white")
# place image on the screen
for car in cars:
    screen.blit(car.img, car.img_location)

# start game loop
while running:
    # if we click on the "exit" button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # stop game loop
            running = False
    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()
