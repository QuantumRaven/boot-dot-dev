#!/usr/bin/env python3


def calculate_flurry_crit(num_attacks, base_damage):
    for flurry in range(0, 100):
        flurry_dmg = base_damage * 2 * (num_attacks - 1)
        final_hit = base_damage * 4
        total_dmg = flurry_dmg + final_hit

        return total_dmg
