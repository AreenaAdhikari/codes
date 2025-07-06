import pygame
import random
pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space invaders with sprites")
clock = pygame.time.Clock()

# Load and scale images
player_img = pygame.image.load("dow.png")
enemy_img = pygame.image.load("yay.jpeg")
bullet_img = pygame.image.load("download.jpeg")
player_img = pygame.transform.scale(player_img, (50, 40))
enemy_img = pygame.transform.scale(enemy_img, (40, 40))
bullet_img = pygame.transform.scale(bullet_img, (5, 20))

# Create player and bullet
player_rect = player_img.get_rect(midbottom=(300, 390))
bullet_rect = bullet_img.get_rect(center=(-100, -100))

# Create multiple enemies (5 in this case)
enemies = []
for _ in range(5):
    enemy_rect = enemy_img.get_rect(topleft=(random.randint(0, 560), random.randint(50, 150)))
    enemies.append(enemy_rect)

running = True
bullet_active = False

while running:
    clock.tick(60)
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= 5
    if keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
        player_rect.x += 5
    
    # Bullet firing
    if keys[pygame.K_SPACE] and not bullet_active:
        bullet_rect.center = player_rect.midtop
        bullet_active = True
    
    # Bullet movement
    if bullet_active:
        bullet_rect.y -= 7
        if bullet_rect.bottom < 0:
            bullet_active = False
        screen.blit(bullet_img, bullet_rect)
    
    # Check for collisions with all enemies
    for enemy in enemies[:]:  # Create a copy of the list for iteration
        if bullet_active and bullet_rect.colliderect(enemy):
            enemy.x = random.randint(0, 560)
            enemy.y = random.randint(50, 150)
            bullet_active = False
    
    # Draw everything
    screen.blit(player_img, player_rect)
    for enemy in enemies:
        screen.blit(enemy_img, enemy)
    
    pygame.display.flip()

pygame.quit()