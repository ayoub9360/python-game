import time
import pygame
from pygame.locals import *
import random

module_charge = pygame.init()
print(module_charge)
# ecran = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screenSizeX = 768
screenSizeY = 1024
ecran = pygame.display.set_mode((screenSizeY, screenSizeX))
pygame.display.set_caption("Space invader 3000")
appIcon = pygame.image.load("logo.jpeg").convert()
pygame.display.set_icon(appIcon)

# ------ Variable ------
bird = pygame.image.load('bird.png')
positionY = 100
positionX = 100
tuyau = pygame.image.load('tuyaux.png')
tuyau2 = pygame.image.load('tuyaux2.png')
background = pygame.image.load("background.png")
backgroundPosition = 0
loop = True
obstacleSize = random.randrange(-200, 200, 1)
obstaclePosition = 980
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
gameSpeed = 4
failed = False

while loop:
  if positionY >= -400 + obstacleSize and positionY <= -400 + obstacleSize + 600:
    if positionX >= obstaclePosition - 80 and positionX <= obstaclePosition:
      failed = True

  if positionY >= 768 - 300 + obstacleSize and positionY <= 768 - 300 + obstacleSize + 600:
    if positionX >= obstaclePosition - 80 and positionX <= obstaclePosition:
      failed = True

  # ------ Background infinite ------
  ecran.blit(background, (backgroundPosition, 0))
  ecran.blit(background, (backgroundPosition + screenSizeX, 0))
  if not failed:
    backgroundPosition = backgroundPosition - gameSpeed
  if backgroundPosition <= (0 - screenSizeX):
    backgroundPosition = 0

  # ------ Obstacle ------
  ecran.blit(tuyau2,(obstaclePosition,-400 + obstacleSize))
  ecran.blit(tuyau,(obstaclePosition,768-300 + obstacleSize))
  if not failed:
    obstaclePosition = obstaclePosition - gameSpeed
  if obstaclePosition <= -40:
    obstaclePosition = 980
    obstacleSize = random.randrange(-200, 200, 1)
    score = score + 1
    if gameSpeed <= 13:
      gameSpeed = gameSpeed + 0.8

  # ------ Bird ------
  ecran.blit(bird,(positionX,positionY))
  if not failed:
    positionY = positionY + 2.5
  if positionY >= 900:
    positionY = 800
  if positionY <= -180:
    positionY = -130

  # ------ Score ------
  if not failed:
    scoreText = font.render("Score : " + str(score), True, (255, 255, 255))
    ecran.blit(scoreText, (30, 30))

  # ------ Fail ------
  if failed:
    failedText = font.render("Game over", True, (255, 255, 255))
    scoreText = font.render("Score : " + str(score), True, (255, 255, 255))
    ecran.blit(failedText, (400, 330))
    ecran.blit(scoreText, (400, 300))

  # ------ Event ------
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      # Deplacement
      if event.key == pygame.K_UP and not failed:
        positionY = positionY - 90
      if event.key == pygame.K_SPACE and not failed:
        positionY = positionY - 90
      # Quitter
      if event.key == pygame.K_j:
        loop = False
    if event.type == pygame.QUIT:
      loop = False

  pygame.display.flip()
pygame.quit()

print(f'Nice try but you failed, your score is {score} !')