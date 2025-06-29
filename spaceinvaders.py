import pygame
import random
pygame.init()
WIDTH , HEIGHT = 600,400
screen = pygame.display.set_mode((WIDTH , HEIGHT))
pygame.display.set_caption("Space invaderswith sprites")
clock = pygame.time.Clock()
player_img = pygame.image.load("dow.png")
enemy_img = pygame.image.load("yay.jpeg")
bullet_img = pygame.image.load("download.jpeg")
player_img = pygame.transform.scale(player_img(50,40))
enemy_img_img = pygame.transform.scale(enemy_img(40,40))
bullet_img = pygame.transform.scale(bullet_img(5,20))
player_rect = player_img.get_rect(midbottom=(300,390))
enemy_rect = enemy_img.get_rect(topleft=(random.randint(0,560),50))
bullet_rect = bullet_img.get_rect(center=(-100,-100))
running = True
while running:
    clock.tick(60)
    screen.fill((0,0,0))
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False