from __future__ import annotations

import random
from typing import Iterator, List, Tuple, TYPE_CHECKING

import tcod
import numpy as np

from game_map import GameMap
import tile_types

if TYPE_CHECKING:
    from entity import Entity


def generate_map(map_width, map_height):

    map = GameMap(map_width, map_height)
    total_cells = map_width * map_height
    on_cells = int(total_cells * 0.45)
    arr = np.full(total_cells, tile_types.wall)
    arr[:on_cells] = tile_types.floor
    np.random.shuffle(arr)
    map.tiles = np.reshape(arr, (map_width, map_height))

    return map
