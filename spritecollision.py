import pygame,sys,random,time
pygame.init()
W , H = 640 , 480
screen = pygame.display.set_mode(W , H)
Clock = pygame.time.Clock
font = pygame.font.SysFont(None, 40)
player_img = pygame.transform.scale(pygame.image.load("yay.jpeg"),(50,50))
target_img = pygame.transform.scale(pygame.image.load("download.jpeg"),(50,50))
player = player_img.get_rect(topleft = (100,100))
target = target_img.get_rect(topleft = (random.randint(0,W-50),random.randint(0,H-50)))
won = False
start = time.time()
while True:  
  for e in pygame.event.get():
    if e.type == pygame.QUIT: pygame.quit(); sys.exit()
  keys = pygame.key.get_pressed()
  if not won:
      player.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT])
      player.y +=  (keys[pygame.K_DOWN]-keys[pygame.K_UP])
      player.clamp_ip(screen.get_rect())
  if player.colliderect(target):
     won = True
     win_time = round(time.time()-start,2)
  screen.fill(220,220,255)
  screen.blit(target_img,target)
  screen.blit(player_img,player)
if won :
   txt - font.render(f"You win in {win_time}s!",True,(0,150,0))
else:
   txt - font.render(f"Time:{round}",True,(0,150,0))