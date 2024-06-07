import pygame
import sys
import random

global speed
speed = 10

#Window size

frameSize_x = 1380
frameSize_y = 840

pg = pygame
checkError = pg.init()
print('checkError: ', checkError)

if checkError[1] > 0:
    print("ERROR" + checkError[1])

else:
    print('Game succesfully initialized')

#initilise game window
pg.display.set_caption('Snake Game')
print('frameSize_x: ', frameSize_x)
print('frameSize_y: ', frameSize_y)
gameWindow = pg.display.set_mode((frameSize_x, frameSize_y))

#colors
backGroundColor = pg.Color(237, 192, 192)
scoreColor = pg.Color(15, 14, 14)
food = pg.Color(45, 26, 214)
snakeColor = pg.Color(214, 26, 26)


fpsController = pg.time.Clock()



#snake square size
squarSize = 30


def initVars():
    global headPos, snakeBody, foodPos, foodSpawn, score, direction

    direction = 'RIGHT'
    headPos = [120, 60]
    snakeBody = [[120, 60]]
    foodPos = [
        random.randrange(1, (frameSize_x // squarSize)) * squarSize,
        random.randrange(1, (frameSize_y // squarSize)) * squarSize
    ]
    foodSpawn = True
    score = 0

initVars()


def showScore(choice, color, font, size):
    scoreFont = pg.font.SysFont(font, size)
    scoreSurface = scoreFont.render('Score: ' + str(score), True, color)
    scoreRect = scoreSurface.get_rect()

    if choice == 1:
        scoreRect.midtop = (frameSize_x/10, 15)
    else:
        scoreRect.midtop = (frameSize_x/2, frameSize_y/1.25)

    gameWindow.blit(scoreSurface, scoreRect)

#game loop


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        elif event.type == pg.KEYDOWN:
            if (event.key == pg.K_UP or event.key == ord("w") and direction != "DOWN"):
                direction = "UP"

            elif (event.key == pg.K_DOWN or event.key == ord("s") and direction != "UP"):
                direction = "DOWN"

            elif (event.key == pg.K_LEFT or event.key == ord("a") and direction != "RIGHT"):
                direction = "LEFT"

            elif (event.key == pg.K_RIGHT or event.key == ord("d") and direction != "LEFT"):
                direction = "RIGHT"

    if direction == "UP":
        headPos[1] -= squarSize

    elif direction == "DOWN":
        headPos[1] += squarSize

    elif direction == "LEFT":
        headPos[0] -= squarSize

    else:
        headPos[0] += squarSize

    
    if headPos[0] < 0:
        headPos[0] = frameSize_x - squarSize
    elif headPos[0] > frameSize_x - squarSize:
        headPos[0] = 0
    elif headPos[1] < 0:
        headPos[1] = frameSize_y - squarSize
    elif headPos[1] > frameSize_y - squarSize:
        headPos[1] = 0 

    # eat food 
    snakeBody.insert(0, list(headPos))

    if headPos[0] == foodPos[0] and headPos[1] == foodPos[1]:
        score += 1
        speed += 1
        foodSpawn = False
    else:
        snakeBody.pop()          

    #spawm food
    if not foodSpawn:

        foodPos = [
        random.randrange(1, (frameSize_x // squarSize)) * squarSize,
        random.randrange(1, (frameSize_y // squarSize)) * squarSize
    ]
        foodSpawn = True
    
    #GFX condition 
    gameWindow.fill(backGroundColor)
    for pos in snakeBody:
        pg.draw.rect(gameWindow, snakeColor, pg.Rect(
            pos[0] + 2, pos[1] + 2,
            squarSize - 2, squarSize - 2
        ))

    pg.draw.rect(gameWindow, food, pg.Rect(foodPos[0],
                                          foodPos[1], squarSize, squarSize))

    # Game over condition

    for block in snakeBody[1:]:
        if headPos[0] == block[0] and headPos[1] == block[1]:
            speed = 10
            initVars()

    showScore(1, scoreColor, 'consolas', 20)
    pg.display.update()
    fpsController.tick(speed)