

import pygame
import json

class TrainerSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, sheet_path, json_path):
        super().__init__()

        # load spritesheet
        self.sheet = pygame.image.load(sheet_path).convert_alpha()

        # load json data
        with open(json_path) as f:
            self.data = json.load(f)["frames"]

        # direction to sprite mapping
        # based on your sheet: row1=down, row2=left, row3=right, row4=up
        self.direction_frames = {
            "down":  ["sprite1",  "sprite2",  "sprite3",  "sprite4"],
            "left":  ["sprite5",  "sprite6",  "sprite7",  "sprite8"],
            "right": ["sprite9",  "sprite10", "sprite11", "sprite12"],
            "up":    ["sprite13", "sprite14", "sprite15", "sprite16"],
        }

        # state
        self.direction = "down"
        self.current_frame = 0
        self.animation_timer = 0
        self.animation_speed = 10  # change frame every 10 game ticks

        # position
        self.x = x
        self.y = y
        self.speed = 3

        # get first frame to set image
        self.image = self.get_frame("sprite1")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def get_frame(self, sprite_name):
        f = self.data[sprite_name]["frame"]
        surface = pygame.Surface((f["w"], f["h"]), pygame.SRCALPHA)
        surface.blit(self.sheet, (0, 0), (f["x"], f["y"], f["w"], f["h"]))
        return surface

    def update(self, keys):
        moving = False

        if keys[pygame.K_w]:
            self.y -= self.speed
            self.direction = "up"
            moving = True
        if keys[pygame.K_s]:
            self.y += self.speed
            self.direction = "down"
            moving = True
        if keys[pygame.K_a]:
            self.x -= self.speed
            self.direction = "left"
            moving = True
        if keys[pygame.K_d]:
            self.x += self.speed
            self.direction = "right"
            moving = True

        # update animation only when moving
        if moving:
            self.animation_timer += 1
            if self.animation_timer >= self.animation_speed:
                self.animation_timer = 0
                self.current_frame = (self.current_frame + 1) % 4
        else:
            self.current_frame = 0  # stand still on frame 0
            self.animation_timer = 0

        # update image and rect
        frame_name = self.direction_frames[self.direction][self.current_frame]
        self.image = self.get_frame(frame_name)
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)