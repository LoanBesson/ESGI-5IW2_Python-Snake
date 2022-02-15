import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 600
dis_height = 400


dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game - Groupe 4 - 5IW2')

clock = pygame.time.Clock()

snake_block = 10
wall_block = 10
snake_speed = 10

font_style = pygame.font.SysFont("bahnschrift", 30)
score_font = pygame.font.SysFont("comicsansms", 15)


def Your_score(score):
    value = score_font.render("Votre Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


def Write_file(currentScore):
    f = open("score.txt", "w")
    f.close()
    f = open("score.txt", "r")
    bestScore = f.read()
    if(currentScore > bestScore):
        f = open('score.txt', "w")
        f.write(currentScore)
    f.close()

def Best_score():
    f = open("score.txt", "r")
    value = score_font.render("Meilleur score: " + str(f.read()), True, yellow)
    dis.blit(value, [20, 0])

def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    wall1x = round(random.randrange(1, dis_width - wall_block) / 10.0) * 10.0
    wall1y = round(random.randrange(1, dis_width - wall_block) / 10.0) * 10.0

    wall2x = round(random.randrange(1, dis_width - wall_block) / 10.0) * 10.0
    wall2y = round(random.randrange(1, dis_width - wall_block) / 10.0) * 10.0

    wall3x = round(random.randrange(1, dis_width - wall_block) / 10.0) * 10.0
    wall3y = round(random.randrange(1, dis_width - wall_block) / 10.0) * 10.0

    wall4x = round(random.randrange(1, dis_width - wall_block) / 10.0) * 10.0
    wall4y = round(random.randrange(1, dis_width - wall_block) / 10.0) * 10.0

    wall5x = round(random.randrange(1, dis_width - wall_block) / 10.0) * 10.0
    wall5y = round(random.randrange(1, dis_width - wall_block) / 10.0) * 10.0

    wall6x = round(random.randrange(1, dis_width - wall_block) / 10.0) * 10.0
    wall6y = round(random.randrange(1, dis_width - wall_block) / 10.0) * 10.0

    while not game_over:
       while game_close == True:
            dis.fill(black)
            message("Tu as perdu ! \n Rejouer : C \n Quitter : Q", red)
            Your_score(Length_of_snake - 1)
            Write_file(Length_of_snake - 1)
            Best_score()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change

        dis.fill(black)

        pygame.draw.rect(dis, yellow, [foodx, foody, snake_block, snake_block])
        pygame.draw.rect(dis, red, [wall1x, wall1y, wall_block, wall_block])
        pygame.draw.rect(dis, red, [wall2x, wall2y, wall_block, wall_block])
        pygame.draw.rect(dis, red, [wall3x, wall3y, wall_block, wall_block])
        pygame.draw.rect(dis, red, [wall4x, wall4y, wall_block, wall_block])

        if (Length_of_snake > 5):
            pygame.draw.rect(
                dis, red, [wall5x, wall5y, wall_block, wall_block])
            pygame.draw.rect(
                dis, red, [wall6x, wall6y, wall_block, wall_block])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(
                0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(
                0, dis_height - snake_block) / 10.0) * 10.0
            wall1x = round(random.randrange(
                0, dis_width - wall_block) / 10.0) * 10.0
            wall1y = round(random.randrange(
                0, dis_height - wall_block) / 10.0) * 10.0
            wall2x = round(random.randrange(
                0, dis_width - wall_block) / 10.0) * 10.0
            wall2y = round(random.randrange(
                0, dis_height - wall_block) / 10.0) * 10.0
            wall3x = round(random.randrange(
                0, dis_width - wall_block) / 10.0) * 10.0
            wall3y = round(random.randrange(
                0, dis_height - wall_block) / 10.0) * 10.0
            wall4x = round(random.randrange(
                0, dis_width - wall_block) / 10.0) * 10.0
            wall4y = round(random.randrange(
                0, dis_height - wall_block) / 10.0) * 10.0
            wall5x = round(random.randrange(
                0, dis_width - wall_block) / 10.0) * 10.0
            wall5y = round(random.randrange(
                0, dis_height - wall_block) / 10.0) * 10.0
            wall6x = round(random.randrange(
                0, dis_width - wall_block) / 10.0) * 10.0
            wall6y = round(random.randrange(
                0, dis_height - wall_block) / 10.0) * 10.0
            Length_of_snake += 1

        if (x1 == wall1x and y1 == wall1y) or (x1 == wall2x and y1 == wall2y) or (x1 == wall3x and y1 == wall3y) or (x1 == wall4x and y1 == wall4y) or (x1 == wall5x and y1 == wall5y) or (x1 == wall6x and y1 == wall6y):
            game_close = True

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
