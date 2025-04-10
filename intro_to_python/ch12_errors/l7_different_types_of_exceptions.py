#!/usr/bin/env python3


def process_player_record(player_id):
    try:
        # Try to get the player record
        return get_player_record(player_id)
    except IndexError:
        # Handle the specific case of index being too high
        return "index is too high"
    except Exception as e:
        # Handle any other exceptions
        return e


# Don't edit below this line


def get_player_record(player_id):
    if player_id < 0:
        raise Exception("negative ids not allowed")
    players = [
        {"name": "Slayer", "level": 128},
        {"name": "Dorgoth", "level": 300},
        {"name": "Saruman", "level": 4000},
    ]
    return players[player_id]
