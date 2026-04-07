import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('"First Project" ahh game')
clock = pygame.time.Clock()

# Game state
game_active = True
pause = False
score = 0
draw_line = False
ray = None

# Load and scale images
sky = pygame.image.load("pygame/graphics/sky.png").convert_alpha()
sky = pygame.transform.scale(sky, (800, 300))
sky_rect = sky.get_rect(midtop=(400, 0))

ground = pygame.image.load("pygame/graphics/ground.png").convert_alpha()
ground = pygame.transform.scale(ground, (800, 100))
ground_rect = ground.get_rect(midbottom=(400, 400))

ghost = pygame.image.load("pygame/graphics/ghost.png").convert_alpha()
ghost = pygame.transform.scale(ghost, (40, 40))
ghost_rect = ghost.get_rect()
ghost_rect.midbottom = ground_rect.topright

player = pygame.image.load("pygame/graphics/player.png").convert_alpha()
player = pygame.transform.scale(player, (45, 65))
player_rect = player.get_rect()
player_rect.midbottom = ground_rect.midtop
player_gravity = 0

# Fonts
score_font = pygame.font.Font(None, 50)
game_over_font = pygame.font.Font(None, 74)
restart_font = pygame.font.Font(None, 50)

while True:
    for event in pygame.event.get():
        #Take the input (in this case, quitting the program)
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #Check if mouse is clicked or not
        if event.type == pygame.MOUSEBUTTONDOWN:
            draw_line = True
 
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_UP or event.key == pygame.K_SPACE) and player_rect.bottom == 300:
                player_gravity = -15
            if event.key == pygame.K_r and game_active == False:  # Restart when pressing R
                game_active = True
                ghost_rect.x = 830
                player_rect.midbottom = ground_rect.midtop
                score = 0
            if event.key == pygame.K_p:
                pause = not pause

    if pause:
        # Draw pause screen
        game_over_text = game_over_font.render("Game Paused", True, "Red")
        game_over_rect = game_over_text.get_rect(center=(400, 100))
        screen.blit(game_over_text, game_over_rect)
        
        restart_text = restart_font.render("Press P to Continue", True, "White")
        restart_rect = restart_text.get_rect(center=(400, 200))
        screen.blit(restart_text, restart_rect)

    elif game_active:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player_rect.x -= 5
        if keys[pygame.K_d]:
            player_rect.x += 5


        #If run out of screen, teleport back
        ghost_rect.left -= 1
        if ghost_rect.left < -80:
            ghost_rect.left = 780

        #Display the regular surface on the display surface
        screen.blit(ground, ground_rect)
        screen.blit(sky, sky_rect)

        #Ghost
        screen.blit(ghost, ghost_rect)

        #Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        if player_rect.left <= 0:
            player_rect.left = 1
        if player_rect.right >= 800:
            player_rect.right = 799
        screen.blit(player, player_rect)

        #This is to get the mouse postition and drawn the line and imediately erase it
        mouse_pos = pygame.mouse.get_pos()
        if draw_line:
            ray = pygame.draw.line(screen, "Gold", player_rect.midright, mouse_pos, 3)
        #Check if the line is there and collide with the ghost, the ghost disapear
            if ghost_rect.clipline(player_rect.midright, mouse_pos):
                ghost_rect.left = 850
                score += 1
            draw_line = False
        ray = None

        if ghost_rect.colliderect(player_rect):
            game_active = False

        # Display score
        score_text = score_font.render(f"Score: {score}", True, "White")
        score_rect = score_text.get_rect(topleft=(10, 10))
        screen.blit(score_text, score_rect)
    else:
        screen.fill("Black")
        # Draw game over screen
        game_over_text = game_over_font.render("Game Over", True, "Red")
        game_over_rect = game_over_text.get_rect(center=(400, 100))
        screen.blit(game_over_text, game_over_rect)
        
        restart_text = restart_font.render("Press R to Restart", True, "White")
        restart_rect = restart_text.get_rect(center=(400, 200))
        screen.blit(restart_text, restart_rect)

        score_text = score_font.render(f"Score: {score}", True, "White")
        score_rect = score_text.get_rect(center=(400, 20))
        screen.blit(score_text, score_rect)



    #Update stuff to the screen
    pygame.display.update()
    #FPS
    clock.tick(60)


