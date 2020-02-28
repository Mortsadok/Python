import pygame
import sys
import random


class Snake:
    def __init__(self):
        self.Position = [100, 50]
        self.Body = [[100, 50], [90, 50], [80, 50]]
        self.Direction = "RIGHT"
        self.ChangeDir = self.Direction

    def ChangeDirectionTo(self, Dir):
        if Dir == "RIGHT" and not self.Direction == "LEFT":
            self.Direction = "RIGHT"
        if Dir == "LEFT" and not self.Direction == "RIGHT":
            self.Direction = "LEFT"
        if Dir == "UP" and not self.Direction == "DOWN":
            self.Direction = "UP"
        if Dir == "DOWN" and not self.Direction == "UP":
            self.Direction = "DOWN"

    def Move(self, FoodPOS):
        if self.Direction == "RIGHT":
            self.Position[0] += 10
        if self.Direction == "LEFT":
            self.Position[0] -= 10
        if self.Direction == "UP":
            self.Position[1] -= 10
        if self.Direction == "DOWN":
            self.Position[1] += 10

        self.Body.insert(0, list(self.Position))

        if self.Position == FoodPOS:
            return 1

        else:
            self.Body.pop()
            return 0

    def CheckCollision(self):
        if self.Position[0] > 490 or self.Position[0] < 0:
            return 1

        elif self.Position[1] > 490 or self.Position[1] < 0:
            return 1

        for BodyPart in self.Body[1:]:
            if self.Position == BodyPart:
                return 1
        return 0

    def GetHeadPosition(self):
        return self.Position

    def GetBody(self):
        return self.Body


class Food:
    def __init__(self):
        self.foodPosition = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]
        self.IsFoodOnScreen = True

    def foodSpawn(self):
        if not self.IsFoodOnScreen:
            self.foodPosition = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]
            self.IsFoodOnScreen = True
        return self.foodPosition

    def SetFoodOnScreen(self, b):
        self.IsFoodOnScreen = b


Window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Snake Game")
FPS = pygame.time.Clock()

Score = 0
Snake = Snake()
foodSpawn = Food()


def GameOver():
    pygame.quit()
    sys.exit()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameOver()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                Snake.ChangeDirectionTo("RIGHT")

            if event.key == pygame.K_LEFT:
                Snake.ChangeDirectionTo("LEFT")

            if event.key == pygame.K_UP:
                Snake.ChangeDirectionTo("UP")

            if event.key == pygame.K_DOWN:
                Snake.ChangeDirectionTo("DOWN")
                
    foodPos = foodSpawn.foodSpawn()
    if Snake.Move(foodPos) == 1:
        Score += 1
        foodSpawn.SetFoodOnScreen(False)

    Window.fill(pygame.Color(225, 225, 225))
    for Pos in Snake.GetBody():
        pygame.draw.rect(Window, pygame.Color(0, 225, 0), pygame.Rect(Pos[0], Pos[1], 10, 10))
    pygame.draw.rect(Window, pygame.Color(225, 0, 0), pygame.Rect(foodPos[0], foodPos[1], 10, 10))
    if Snake.CheckCollision() == 1:
        GameOver()
    pygame.display.set_caption("Snake Game: Score: " + str(Score))
    pygame.display.flip()
    FPS.tick(24)
