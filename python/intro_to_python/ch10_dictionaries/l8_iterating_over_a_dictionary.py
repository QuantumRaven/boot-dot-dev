#!/usr/bin/env python3


def get_most_common_enemy(enemies_dict):
    max_count = 0
    enemy_with_max_count = None
    for enemy, count in enemies_dict.items():
        if count > max_count:
            max_count = count
            enemy_with_max_count = enemy
    return enemy_with_max_count
