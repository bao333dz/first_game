import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Bubble Sort")
clock = pygame.time.Clock()
game_active = True

#Load image 
sky = pygame.image.load("graphics/sky.png").convert_alpha()
#Scale images to fit window
sky = pygame.transform.scale(sky, (800, 300))
#Make the rectangle
sky_rect = sky.get_rect(midtop = (400, 0))

ground = pygame.image.load("graphics/ground.png").convert_alpha()
ground = pygame.transform.scale(ground, (800, 100))
ground_rect = ground.get_rect(midbottom = (400,400))

ghost = pygame.image.load("graphics/ghost.png").convert_alpha()
ghost = pygame.transform.scale(ghost, (60, 60))
ghost_rect = ghost.get_rect()
ghost_rect.midbottom = ground_rect.midtop

player = pygame.image.load("graphics/player.png").convert_alpha()
player = pygame.transform.scale(player, (45, 65))
player_rect = player.get_rect()
player_rect.bottom = ground_rect.top
player_gravity = 0

# score = test_font.render("My Game", True, "Black")
# score_rect = score.get_rect()
# score_rect.center = sky_rect.center

#This is to draw the line
draw_line = False
#This is to define the ray aka the line drawn by mouse click
ray = None

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

    if game_active:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player_rect.x -= 5
        if keys[pygame.K_d]:
            player_rect.x += 5


        #If run out of screen, teleport back
        ghost_rect.left -= 1
        if ghost_rect.left < -80: ghost_rect.left = 780

        #Display the regular surface on the display surface
        screen.blit(ground, ground_rect)
        screen.blit(sky, sky_rect)

        #Ghost
        screen.blit(ghost, ghost_rect)

        #Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300
        screen.blit(player, player_rect)

        #This is to get the mouse postition and drawn the line and imediately erase it
        mouse_pos = pygame.mouse.get_pos()
        if draw_line:
            ray = pygame.draw.line(screen, "Gold", player_rect.midright, mouse_pos, 3)
        #Check if the line is there and collide with the ghost, the ghost disapear
            if ghost_rect.clipline(player_rect.midright, mouse_pos):
                ghost_rect.left = 850
            draw_line = False
        ray = None

        if ghost_rect.colliderect(player_rect):
            game_active = False
    
    else:
        # Draw a game over message
        game_over_font = pygame.font.Font(None, 74)
        game_over_text = game_over_font.render("Game Over", True, "Red")
        game_over_rect = game_over_text.get_rect(center=(400, 100))
        screen.blit(game_over_text, game_over_rect)
        
        # Draw restart instruction
        restart_font = pygame.font.Font(None, 50)
        restart_text = restart_font.render("Press R to Restart", True, "White")
        restart_rect = restart_text.get_rect(center=(400, 250))
        screen.blit(restart_text, restart_rect)


    #Update stuff to the screen
    pygame.display.update()
    #FPS
    clock.tick(60)


