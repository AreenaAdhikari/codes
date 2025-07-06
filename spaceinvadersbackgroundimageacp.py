import pygame
import random
pygame.init()
WIDTH , HEIGHT = 600,400
screen = pygame.display.set_mode((WIDTH , HEIGHT))
pygame.display.set_caption("Space invaderswith sprites")
clock = pygame.time.Clock()
bg_image = pygame.image.load("do.jpeg")
bg_image = pygame.transform.scale(bg_image, (WIDTH,HEIGHT))
player_img = pygame.image.load("dow.png")
enemy_img = pygame.image.load("yay.jpeg")
bullet_img = pygame.image.load("download.jpeg")
player_img = pygame.transform.scale(player_img,(50,40))
enemy_img_img = pygame.transform.scale(enemy_img,(40,40))
bullet_img = pygame.transform.scale(bullet_img,(5,20))
player_rect = player_img.get_rect(midbottom=(300,390))
enemy_rect = enemy_img.get_rect(topleft=(random.randint(0,560),50))
bullet_rect = bullet_img.get_rect(center=(-100,-100))
running = True
bullet_active = False
while running:
    clock.tick(60)
    screen.blit(bg_image, (0, 0))
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False
    keys = pygame.key.get_pressed()
    if keys [pygame.K_LEFT] and player_rect.left >0:
        player_rect.x -= 5
    if keys [pygame.K_RIGHT] and player_rect.right < WIDTH :
        player_rect.x += 5
    if keys [pygame.K_SPACE] and not bullet_active :
      bullet_rect.center = player_rect.midtop
      bullet_active = True
    if bullet_active:
        bullet_rect.y -= 7
        if bullet_rect.bottom < 0:
            bullet_active = False
        screen.blit(bullet_img,bullet_rect)
    if bullet_rect.colliderect(enemy_rect):
        enemy_rect.x = random.randint(0,560)
        bullet_active = False
    
    screen.blit(player_img,player_rect)
    screen.blit(enemy_img,enemy_rect)

    pygame.display.flip()
pygame.quit()