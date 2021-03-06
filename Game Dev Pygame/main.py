import pygame
import time
pygame.init()

display_width = 800
display_height = 600
wood_width = 64
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('ICHOT')
clock = pygame.time.Clock()

woodImg = pygame.image.load('image/wood.png')


def wood(x, y):
    gameDisplay.blit(woodImg, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, 'black')
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurface, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurface, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()


def crash():
    message_display('Game Crach')


def game_loop():

    x = (display_width * 0.5)
    y = (display_height * 0.5)

    x_change = 0
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gameDisplay.fill('white')
        wood(x, y)
        if x > display_width - wood_width or x < 0:
            crash()
        pygame.display.update()
        clock.tick(30)


game_loop()
pygame.quit()
quit()
