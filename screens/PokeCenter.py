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
pc_floor2 = pygame.image.load("assets/pokemonCenter/PokeCenter2.png")
pc_floor2 = pygame.transform.scale(pc_floor2, (1280, 720))

# trainer
trainer = TrainerSprite(
    x=610, y=650,
    sheet_path="assets/trainer/test_trainer.png",
    json_path="assets/trainer/test_trainer.json"
)

# state
current_floor = 1
fade_alpha = 0
fading_out = False
fading_in = False
next_floor = None

# stair zone same position on both floors
stair_rect1 = pygame.Rect(0, 440, 120 , 150)
stair_rect2 = pygame.Rect(0, 435, 120 , 100)

# fade surface
fade_surface = pygame.Surface((1280, 720))
fade_surface.fill((0, 0, 0))

def start_fade(to_floor):
    global fading_out, next_floor, fade_alpha
    fading_out = True
    next_floor = to_floor
    fade_alpha = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # only move when not fading
    if not fading_out and not fading_in:
        trainer.update(keys)

        # check if trainer is on stairs
        if current_floor == 1 and stair_rect1.collidepoint(trainer.x, trainer.y):
            start_fade(to_floor=2)
        elif current_floor == 2 and stair_rect2.collidepoint(trainer.x, trainer.y):
            start_fade(to_floor=1)

    # draw background
    if current_floor == 1:
        screen.blit(pc_floor1, (0, 0))
        # pygame.draw.rect(screen, (0, 0, 0), stair_rect1, 2)
    else:
        screen.blit(pc_floor2, (0, 0))
        # pygame.draw.rect(screen, (0, 0, 0), stair_rect2, 2)

    trainer.draw(screen)

    # fade logic
    if fading_out:
        fade_alpha += 5
        if fade_alpha >= 255:
            fade_alpha = 255
            fading_out = False
            fading_in = True
            current_floor = next_floor

            if current_floor == 2:
                trainer.x = 140
                trainer.y = 420
                trainer.direction = "right"
            else:
                trainer.x = 100
                trainer.y = 500
                trainer.direction = "right"

    if fading_in:
        fade_alpha -= 5  # speed of fade in
        if fade_alpha <= 0:
            fade_alpha = 0
            fading_in = False

    # draw fade overlay
    if fading_out or fading_in:
        fade_surface.set_alpha(fade_alpha)
        screen.blit(fade_surface, (0, 0))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()