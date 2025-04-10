#!/usr/bin/env python3


def get_player_record(player_id):
    if player_id == 1:
        return {"name": "Slayer", "level": 128}
    if player_id == 2:
        return {"name": "Dorgoth", "level": 300}
    if player_id == 3:
        return {"name": "Saruman", "level": 4000}
    raise Exception("player id not found")


try:
    get_player_record(0)
    get_player_record(4)
    get_player_record(5)
except Exception as e:
    print(f"player id not found {e}")
