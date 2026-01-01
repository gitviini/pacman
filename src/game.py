import pygame
from pygame.locals import *

def move_entity(entity):
    entity["pos"]["x"] += entity["vel"]["x"]
    entity["pos"]["y"] += entity["vel"]["y"]

def draw_tilemap(tilemap, surface):
    for tile in tilemap:
        pygame.draw.rect(surface, tile["color"], (tile["pos"]["x"], tile["pos"]["y"], tile["len"]["x"], tile["len"]["y"]))

def draw_entities(entities, surface):
    for entity in entities:
        pygame.draw.rect(surface, entity["color"], (entity["pos"]["x"], entity["pos"]["y"], entity["len"]["x"], entity["len"]["y"]))

def is_collision(target, obstacles):
    is_target_collide = False
    tgt_pos = {"x": target["pos"]["x"] + target["vel"]["x"], "y": target["pos"]["y"] + target["vel"]["y"]}
    tgt_area = {"x": target["pos"]["x"] + tgt_pos["x"], "y": target["pos"]["y"] + tgt_pos["y"]}

    for obstacle in obstacles:
        obs_pos = {"x": obstacle["pos"]["x"], "y": obstacle["pos"]["y"]}
        obs_area = {"x": obstacle["pos"]["x"] + obstacle["len"]["x"], "y": obstacle["pos"]["y"] + obstacle["len"]["y"]}

        if(tgt_area["x"] >= obs_pos["x"] and tgt_pos["x"] <= obs_area["x"] and
           tgt_area["y"] >= obs_pos["y"] and tgt_pos["y"] <= obs_area["y"]):
            is_target_collide = True
        
    return is_target_collide
