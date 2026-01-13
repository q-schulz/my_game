import pygame

#pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
running = True
dt = 0
test_font = pygame.font.Font('font/Pixeltype.ttf', 100)

test_surface = pygame.Surface((100,200))
test_surface.fill('Red')
text_surface = test_font.render("My Game", False, 'Black')
player_pos = pygame.Vector2((screen.get_width() / 2) - 100, (screen.get_height() / 2))

#Background Surfaces
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/Ground.png').convert()

#Player Surface
snail_pos = pygame.Vector2((600, 270))
alien_surface = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(topleft = snail_pos)
alien_rect = alien_surface.get_rect(topleft = player_pos)

#snail_dir == True means snail is moving left, False right
snail_dir = True

while running:
    pygame.display.update()
    #poll for events
    #pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    #RENDER YOUR GAME HERE

    #Render Background Surfaces
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))

    #Render Text
    screen.blit(text_surface, (300,50))

    #Render Player
    screen.blit(alien_surface,alien_rect)
    screen.blit(snail_surface, snail_rect)
    

    #snail logic
    if snail_pos.x == 0:
        snail_dir = False
    elif snail_pos.x >= 728:
        snail_dir = True

    if snail_dir:
        snail_pos.x -= 3
    else:
        snail_pos.x += 3
    snail_rect.x = snail_pos.x
    

    #Player Movement Logic
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
    alien_rect.topleft = player_pos

    #Collision Logic
    if alien_rect.colliderect(snail_rect):
        player_pos.y -= 100

    #flip() the display to put your work on screen
    pygame.display.flip()




    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()