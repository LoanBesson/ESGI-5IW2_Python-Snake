from select import select
import pygame
import time
import random

pygame.init()

# Couleurs
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Taille de la fenêtre
dis_width = 600
dis_height = 400

# Ouverture de la fenêtre
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game - Groupe 4 - 5IW2')
clock = pygame.time.Clock()

# Définition des tailles d'éléments
snake_block = 10
wall_block = 10
snake_speed = 10

# Police d'écriture
font_style = pygame.font.SysFont("bahnschrift", 30)
score_font = pygame.font.SysFont("comicsansms", 15)

# Menu de démarrage
menu=True

# Fonction d'affichage du score
def Your_score(score):
    value = score_font.render("Votre Score: " + str(score), True, yellow)
    dis.blit(value, [5, 5])

# Fonction d'affichage du serpent en fonction de sa taille
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

# Fonction d'affichage d'un message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

# Fonction de sauvegarde et affichage du meilleur score
def Best_score(currentScore):
    # Enregistre le score du joueur
    f = open("scores.txt", "a")
    f.write(str(currentScore) + "\n")
    f.close()

    # Récupère la liste des scores
    scores = []
    f = open("scores.txt", 'r')
    for score in f.readlines():
        if(len(score.strip()) > 0):
            scores.append(int(score.strip()))

    # S'il n'y a pas de score, bestScore à 0
    if len(scores) > 0:
        bestScore = max(scores)
    else:
        bestScore = 0

    # Liste des 5 derniers scores
    if len(scores) >= 5:
        lastScores = [scores[len(scores)-1], scores[len(scores)-2], scores[len(scores)-3], scores[len(scores)-4], scores[len(scores)-5]]
    elif len(scores) == 4:
        lastScores = [scores[len(scores)-1], scores[len(scores)-2], scores[len(scores)-3], scores[len(scores)-4]]
    elif len(scores) == 3:
        lastScores = [scores[len(scores)-1], scores[len(scores)-2], scores[len(scores)-3]]
    elif len(scores) == 2:
        lastScores = [scores[len(scores)-1], scores[len(scores)-2]]
    elif len(scores) == 1:
        lastScores = scores
    else:
        lastScores = []

    # Affichage du meilleur score
    bestScoreMessage = score_font.render("Meilleur score : " + str(bestScore), True, yellow)
    dis.blit(bestScoreMessage, [5, 25])

    # Affichage des 5 derniers scores
    lastScoresMessage = score_font.render("Liste des 5 derniers scores : " + str(lastScores), True, yellow)
    dis.blit(lastScoresMessage, [5, 45])

# La boucle du jeu
def gameLoop():
    # Variables de fonctionnement du jeu
    game_over = False
    game_close = False
    
    # Blocage de l'écriture du score
    writeScore = True

    # Position au centre de la fenêtre
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0

    # Serpent
    snake_List = []
    Length_of_snake = 1

    # Emplacement aléatoire de la pomme
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    # Emplacements aléatoires des murs
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

    # Tant que le jeu n'est pas terminé
    while not game_over:
        # Lorsque le joueur a perdu
        while game_close == True:
            # Affichage du message pour rejouer ou quitter
            dis.fill(black)
            message("Tu as perdu ! Rejouer : C / Quitter : Q", red)
            
            if writeScore == True:
                # Affichage du score ainsi que du meilleur score
                Your_score(Length_of_snake - 1)
                Best_score(Length_of_snake - 1)
                pygame.display.update()
                writeScore = False

            # Écoute le joueur pour rejouer ou quitter
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        writeScore = True
                        gameLoop()

        # Écoute le joueur pour diriger le serpent ou quitter le jeu
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

        # Si le serpent sort de la fenêtre, on le téléporte à l'opposé
        if x1 >= dis_width:
            x1 = 0
        elif x1 < 0:
            x1 = dis_width
        elif y1 >= dis_height:
            y1 = 0
        elif y1 < 0:
            y1 = dis_height

        # Affectation du nouvel emplacement du serpent
        x1 += x1_change
        y1 += y1_change

        # Fond d'écran
        dis.fill(black)

        # Affichage de la pomme ainsi que les murs
        pygame.draw.rect(dis, yellow, [foodx, foody, snake_block, snake_block])
        pygame.draw.rect(dis, red, [wall1x, wall1y, wall_block, wall_block])
        pygame.draw.rect(dis, red, [wall2x, wall2y, wall_block, wall_block])
        pygame.draw.rect(dis, red, [wall3x, wall3y, wall_block, wall_block])
        pygame.draw.rect(dis, red, [wall4x, wall4y, wall_block, wall_block])

        # Si le serpent fait plus de 5 cases, on rajoute deux murs
        if (Length_of_snake > 5):
            pygame.draw.rect(
                dis, red, [wall5x, wall5y, wall_block, wall_block])
            pygame.draw.rect(
                dis, red, [wall6x, wall6y, wall_block, wall_block])

        # Déplacement du serpent
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        # Suppression de la dernière case du serpent pour effectuer le déplacement
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Si le serpent se mord la queue, le joueur perd
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # Affichage du score
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        pygame.display.update()

        # Si le serpent mange une pomme, on déplace aléatoirement les murs et la pomme et on augmente la taille du serpent de 1 case
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

        # Si le serpent touche un mur, le joueur perd
        if (x1 == wall1x and y1 == wall1y) or (x1 == wall2x and y1 == wall2y) or (x1 == wall3x and y1 == wall3y) or (x1 == wall4x and y1 == wall4y) or (x1 == wall5x and y1 == wall5y) or (x1 == wall6x and y1 == wall6y):
            game_close = True

        # Ticks du jeu
        clock.tick(snake_speed)

    pygame.quit()
    quit()

while menu:
    # Lit le meilleur score enregistré et s'il n'y en a pas, affecte 0
    # Récupère la liste des scores
    scores = []
    f = open("scores.txt", 'r')
    for score in f.readlines():
        if(len(score.strip()) > 0):
            scores.append(int(score.strip()))

    # S'il n'y a pas de score, bestScore à 0
    if len(scores) > 0:
        bestScore = max(scores)
    else:
        bestScore = 0

    # Liste des 5 derniers scores
    if len(scores) >= 5:
        lastScores = [scores[len(scores)-1], scores[len(scores)-2], scores[len(scores)-3], scores[len(scores)-4], scores[len(scores)-5]]
    elif len(scores) == 4:
        lastScores = [scores[len(scores)-1], scores[len(scores)-2], scores[len(scores)-3], scores[len(scores)-4]]
    elif len(scores) == 3:
        lastScores = [scores[len(scores)-1], scores[len(scores)-2], scores[len(scores)-3]]
    elif len(scores) == 2:
        lastScores = [scores[len(scores)-1], scores[len(scores)-2]]
    elif len(scores) == 1:
        lastScores = scores
    else:
        lastScores = []

    print(
        """
            1. Jouer
            2. Quitter

            Meilleur score : """
        + str(bestScore) +
        """

            Liste des 5 derniers scores : """
        + str(lastScores)
    )

    selection = input("\nQue voulez-vous faire ?\n")

    if selection == "1":
        gameLoop()
    elif selection == "2":
        quit() 
    else:
        print("\n Choix invalide veuillez recommencer")