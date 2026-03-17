import pygame
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sprites.Trainer import TrainerSprite

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280, 720))

# backgrounds
pc_floor1 = pygame.image.load("assets/pokemonCenter/center1.png")
pc_floor1 = pygame.transform.scale(pc_floor1, (1280, 720))

# trainer
trainer = TrainerSprite(
    x=640, y=360,
    sheet_path="assets/trainer/test_trainer.jpg",
    json_path="assets/trainer/test_trainer.json"
)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    trainer.update(keys)

    screen.blit(pc_floor1, (0, 0))
    trainer.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()