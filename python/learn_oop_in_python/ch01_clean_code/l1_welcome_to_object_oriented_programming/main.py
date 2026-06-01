#!/usr/bin/env python3


def destroy_walls(wall_health):
    health = []
    for walls in wall_health:
        if walls > 0:
            health.append(walls)
    return health
