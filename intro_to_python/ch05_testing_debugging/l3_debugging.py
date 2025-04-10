#!/usr/bin/env python3


def take_magic_damage(health, resist, amp, spell_power):
    new_spell_power = spell_power * amp
    total_damage = new_spell_power - resist
    new_health = health - total_damage
    return new_health
