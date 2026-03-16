import pygame


def handle_movement(keys, trainer):
    if keys[pygame.K_w] :
        trainer.coordinates[1] += 1
    if keys[pygame.K_s]:
        trainer.coordinates[1] -= 1
    if keys[pygame.K_a]:
        trainer.coordinates[0] -= 1
    if keys[pygame.K_d]:
        trainer.coordinates[0] += 1

