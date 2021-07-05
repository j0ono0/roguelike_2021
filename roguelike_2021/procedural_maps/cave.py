from __future__ import annotations

import random
from typing import Iterator, List, Tuple, TYPE_CHECKING

import tcod
import numpy as np

from .. import entity_factories
from .game_map import GameMap
from . import tile_types

if TYPE_CHECKING:
    from ..engine import Engine


def place_entities(environment: GameMap, maximum_monsters: int):
    number_of_monsters = random.randint(0, maximum_monsters)
    while len(environment.entities) < number_of_monsters:
        x = random.randint(1, environment.width)
        y = random.randint(1, environment.height)
        if environment.tiles[x][y][0] and not environment.get_blocking_entity_at_location(x, y):
            if random.random() < 0.8:
                entity_factories.orc.spawn(environment, x, y)
            else:
                entity_factories.troll.spawn(environment, x, y)


def generate_map(map_width: int, map_height: int, max_monsters: int, engine: Engine):

    player = engine.player
    game_map = GameMap(engine, map_width, map_height, entities=[player])

    total_cells = map_width * map_height
    on_cells = int(total_cells * 0.45)

    # random setup
    arr = np.full(total_cells, 0, order="F")
    arr[:on_cells] = 1
    np.random.shuffle(arr)
    arr = np.reshape(arr, (map_width, map_height))

    for i in range(3):
        iteration1 = np.full((map_width, map_height), 0, order="F")
        for x in range(1, map_width):
            for y in range(1, map_height):
                iteration1[x][y] = 1 if np.sum(
                    arr[x-1:x+2, y-1:y+2]) >= 5 else 0
        arr = iteration1

    # update tiles in map
    for x in range(1, map_width):
        for y in range(1, map_height):
            tile = tile_types.floor if iteration1[x][y] == 0 else tile_types.wall
            game_map.tiles[x][y] = tile

    place_entities(game_map, max_monsters)

    # Find open location and place player
    for x in range(1, map_width):
        for y in range(1, map_height):
            if np.sum(arr[x-1:x+2, y-1:y+2]) == 0:
                player.place(x, y, game_map)
                return game_map
    # Try again if player cannot be placed!
    generate_map(map_width, map_height, player)
