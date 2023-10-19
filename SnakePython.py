import cv2 as cv
import numpy as np
import random as rand
#comment
class SnakeHead:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.prevx: int
        self.prevy: int
        self.direction = direction
    def update(self):
        self.prevx = self.x
        self.prevy = self.y
        if self.direction == 'w':
            self.x -= 1
        elif self.direction == 's':
            self.x += 1
        elif self.direction == 'a':
            self.y -= 1
        elif self.direction == 'd':
            self.y += 1

    
class SnakeBody:
    def __init__(self, x, y, ahead):
        self.x = x
        self.y = y
        self.prevx: int
        self.prevy: int
        self.ahead = ahead
    def update(self):
        self.prevx = self.x
        self.prevy = self.y
        self.x = self.ahead.prevx
        self.y = self.ahead.prevy


head = SnakeHead(10, 10, "w")
snakeArray = []
snakeArray.append(head)
CELL_SIZE = 20
BOARD_SIZE = 20
SNAKE_SPEED = 5
gameOver = False
ax = 12
ay = 12
score = 0
appleIsEaten = False


def updateBoard(snakeArray, ax, ay):
    img = np.zeros((CELL_SIZE * BOARD_SIZE,CELL_SIZE * BOARD_SIZE,3), np.uint8)
    for segment in snakeArray:
        xi = segment.x * CELL_SIZE
        yi = segment.y * CELL_SIZE
        img[xi: (xi + CELL_SIZE), yi: (yi + CELL_SIZE)] = [255, 0, 0]
    axi = ax * CELL_SIZE
    ayi = ay * CELL_SIZE
    img[axi: (axi + CELL_SIZE), ayi: (ayi + CELL_SIZE)] = [0, 0, 255]
    cv.imshow("Snake", np.uint8(img))

while (True):
    
    #update apple
    if (snakeArray[0].x == ax and snakeArray[0].y == ay):
        snakeArray.append(SnakeBody(snakeArray[len(snakeArray) - 1].prevx, snakeArray[len(snakeArray) - 1].prevy, snakeArray[len(snakeArray) - 1]))
        #generate array of all possible spaces
        locate = [[i for i in range(BOARD_SIZE)] for j in range(BOARD_SIZE)]
        #each space that has a head or body object is removed
        locate[snakeArray[0].x][snakeArray[0].y] = 20
        for body in snakeArray[1:]:
            locate[body.x][body.y] = 20
        for i in range(len(locate)):
            bound = len(locate[i])
            j = 0
            while (j < bound):
                if locate[i][j] == 20:
                    locate[i].pop(j)
                    bound -= 1
                else:
                    j += 1

        #randomly select next apple coords from remaining spaces and update screen
        row = rand.randint(0, BOARD_SIZE - 1)
        column = rand.choice(locate[row])
        ax = row
        ay = column

    updateBoard(snakeArray, ax, ay)
    for segment in snakeArray:
        segment.update()
        
    pressed = cv.waitKey(int(1000/SNAKE_SPEED))

    if pressed == ord("k"):
        break
    elif pressed == ord("w"):
        snakeArray[0].direction = "w"
    elif pressed == ord("s"):
        snakeArray[0].direction = "s"
    elif pressed == ord("a"):
        snakeArray[0].direction = "a"
    elif pressed == ord("d"):
        snakeArray[0].direction = "d"
    
    dead = False
    if snakeArray[0].x < 0 or snakeArray[0].x > 19:
        dead = True
    if snakeArray[0].y < 0 or snakeArray[0].y > 19:
        dead = True
    for body in snakeArray[1:]:
        if snakeArray[0].x == body.x and snakeArray[0].y == body.y:
            dead = True
            break
    if dead:
        break





                

    


 