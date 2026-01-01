import pygame
from pygame.locals import *

def move_entity(entity):
    entity["pos"]["x"] += entity["vel"]["x"]
    entity["pos"]["y"] += entity["vel"]["y"]

def draw_tilemap(node_tilemap, init_pos, square_size, surface):
    tilemap = []
    for y in range(len(node_tilemap)):
        for x in range(len(node_tilemap[0])):
            node = node_tilemap[y][x]
            node_pos = {"x": init_pos["x"] + x * square_size,"y": init_pos["y"] + y * square_size}
            tile = {
                    "pos": node_pos,
                    "len": {"x": square_size, "y": square_size},
                    "color": (0, 0, 0),
                    "collision": {"is_collide":False,"type":None},
                }
            if(node == 1):
                tile["color"] = (0,0,255)
                tile["collision"]["type"] = "bearer"
            pygame.draw.rect(surface, tile["color"], (node_pos["x"], node_pos["y"], square_size, square_size))
            tilemap.append(tile)
    return tilemap

def draw_entities(entities, surface):
    for entity in entities:
        pygame.draw.rect(surface, entity["color"], (entity["pos"]["x"], entity["pos"]["y"], entity["len"]["x"], entity["len"]["y"]))

def is_collision(target, obstacles):
    is_target_collide = False
    tgt_pos = {"x": target["pos"]["x"], "y": target["pos"]["y"]}
    tgt_area = {"x": target["len"]["x"] + tgt_pos["x"], "y": target["len"]["y"] + tgt_pos["y"]}

    target["collision"]["type"] = None
    for obstacle in obstacles:
        obs_pos = {"x": obstacle["pos"]["x"], "y": obstacle["pos"]["y"]}
        obs_area = {"x": obstacle["pos"]["x"] + obstacle["len"]["x"], "y": obstacle["pos"]["y"] + obstacle["len"]["y"]}

        obstacle["collision"]["is_collide"] = False
        if(not (tgt_area["x"] >= obs_pos["x"] and tgt_pos["x"] <= obs_area["x"] and
           tgt_area["y"] >= obs_pos["y"] and tgt_pos["y"] <= obs_area["y"])):
            continue

        if(obstacle["collision"]["type"] == "bearer"):
           if(target["pos"]["x"] == obs_area["x"] or target["pos"]["x"] + target["len"]["x"] == obs_pos["x"]):
               target["vel"]["x"] = 0
           elif(target["pos"]["y"] == obs_area["y"] or target["pos"]["y"] + target["len"]["y"] == obs_pos["y"]):
               target["vel"]["y"] = 0

        is_target_collide = True
        target["collision"]["type"] = obstacle["collision"]["type"]
        obstacle["collision"]["is_collide"] = True

    target["collision"]["is_collide"] = is_target_collide
    return is_target_collide
