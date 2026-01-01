import pygame
from pygame.locals import *
from game import *


def draw_rect(surface, entity):
    pygame.draw.rect(
        surface,
        rect=(
            entity["pos"]["x"],
            entity["pos"]["y"],
            entity["len"]["x"],
            entity["len"]["y"],
        ),
        color=entity["color"],
    )


def handle_move(key, entity):
    if key in [pygame.K_RIGHT, pygame.K_d]:
        entity["vel"]["x"] = 1
        entity["vel"]["y"] = 0
    elif key in [pygame.K_LEFT, pygame.K_a]:
        entity["vel"]["x"] = -1
        entity["vel"]["y"] = 0
    elif key in [pygame.K_UP, pygame.K_w]:
        entity["vel"]["y"] = -1
        entity["vel"]["x"] = 0
    elif key in [pygame.K_DOWN, pygame.K_s]:
        entity["vel"]["y"] = 1
        entity["vel"]["x"] = 0


def main():
    tmp_player = {"vel":{"x":0,"y":0}}
    player = {
        "pos": {"x": 40, "y": 0},
        "len": {"x": 20, "y": 20},
        "vel": {"x": 0, "y": 0},
        "color": (255, 255, 0),
        "collision": {"is_collide":False,"type":None},
    }
    node_tilemap = [
    [1,0,1],
    [1,0,0],
    [1,1,1],
    ]
    tilemap = []
    key_list = []
    _display_surf = None
    size = weight, height = 640, 400
    _running = True
    square_size = 20

    pygame.init()
    clock = pygame.time.Clock()
    _display_surf = pygame.display.set_mode(size, pygame.HWSURFACE | pygame.DOUBLEBUF)
    while _running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                _running = False
            if event.type == pygame.KEYDOWN:
                key_list.append(event.key)
                for key in key_list:
                    handle_move(key=key, entity=tmp_player)
            if event.type == pygame.KEYUP:
                key_list.remove(event.key)

        _display_surf.fill((0, 0, 0))
        tilemap = draw_tilemap(surface=_display_surf, node_tilemap=node_tilemap, square_size=square_size, init_pos={"x":40, "y": 40})
        
        if(player["pos"]["x"] % square_size == 0 and player["pos"]["y"] % square_size == 0):
            player["vel"]["x"] = tmp_player["vel"]["x"]
            player["vel"]["y"] = tmp_player["vel"]["y"]    
        is_collision(player, tilemap)
        
        move_entity(player)
        print(player["pos"])

        draw_rect(_display_surf, player)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
