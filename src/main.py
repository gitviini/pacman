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
    if key == pygame.K_RIGHT:
        entity["vel"]["x"] = 1
        entity["vel"]["y"] = 0
    elif key == pygame.K_LEFT:
        entity["vel"]["x"] = -1
        entity["vel"]["y"] = 0
    elif key == pygame.K_UP:
        entity["vel"]["y"] = -1
        entity["vel"]["x"] = 0
    elif key == pygame.K_DOWN:
        entity["vel"]["y"] = 1
        entity["vel"]["x"] = 0


def main():
    player = {
        "pos": {"x": 20, "y": 0},
        "len": {"x": 20, "y": 20},
        "vel": {"x": 0, "y": 0},
        "color": (255, 255, 0),
        "is_collide": False,
    }
    tilemap = [
        {
            "pos": {"x": 40, "y": 40},
            "len": {"x": 20, "y": 20},
            "color": (0, 0, 255),
            "is_collide": False,
        }
    ]
    key_list = []
    _display_surf = None
    size = weight, height = 640, 400
    _running = True
    square_size = 5

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
            if event.type == pygame.KEYUP:
                key_list.remove(event.key)

        _display_surf.fill((0, 0, 0))
        draw_tilemap(surface=_display_surf, tilemap=tilemap)

        for key in key_list:
            handle_move(key=key, entity=player)
        if(not is_collision(player, tilemap)):
            move_entity(player)
        else:
            player["vel"]["x"] = 0
            player["vel"]["y"] = 0

        print(is_collision(player, tilemap))
        draw_rect(_display_surf, player)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
