#!/usr/bin/env python3


def remove_duplicates(spells):
    track_spells = set()
    unique_spells = []
    for spell in spells:
        if spell not in track_spells:
            track_spells.add(spell)
            unique_spells.append(spell)
    return unique_spells
