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

def handle_poke_catch(trainer , pokemon ):
    # assuming player will be asked to choose the pokeball he wants to use
    pokeball = trainer.pokeball[0]
    if trainer.catch_pokemon(pokemon , pokeball):
        return f"Hoo !! You Caught the {pokemon.name}"
    else :
        return f"Uh-oh you missed the {pokemon.name}"


