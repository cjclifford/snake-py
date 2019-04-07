import sys, pygame, time, random
import player, food

pygame.init()

size = width, height = 640, 480

screen = pygame.display.set_mode(size)

game_speed = 1

player = player.Player(size = 10)
food = food.Food(x = random.randrange(0, width, 10), y = random.randrange(0, height, 10))

def left():
    player.turn(-1, 0)
def right():
    player.turn(1, 0)
def up():
    player.turn(0, -1)
def down():
    player.turn(0, 1)

directions = { 
            pygame.K_LEFT : left,
            pygame.K_RIGHT : right,
            pygame.K_UP : up,
            pygame.K_DOWN : down
}

def processInput():
    turned = False
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            sys.exit()
        if event.type is pygame.KEYDOWN and not turned:
            if event.key is pygame.K_ESCAPE:
                sys.exit()
            if event.key in directions:
                directions[event.key]()
                turned = True

while 1:
    current_time = time.time()

    processInput()
    player.update()
    if player.eat(food):
        food.update()
        player.grow()

    screen.fill([0, 0, 0])
    player.render(screen)
    food.render(screen)
    pygame.display.flip()
    
    time.sleep((current_time + game_speed / 10 - time.time()))