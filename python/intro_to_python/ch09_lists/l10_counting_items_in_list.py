#!/usr/bin/env python3


def get_item_counts(items):
    potion_count = 0
    bread_count = 0
    shortsword_count = 0

    # don't touch above this line

    for i in range(0, len(items)):
        current_items = items[i]
        if current_items == "Potion":
            potion_count += 1
        elif current_items == "Bread":
            bread_count += 1
        elif current_items == "Shortsword":
            shortsword_count += 1

    # don't touch below this line

    return potion_count, bread_count, shortsword_count
