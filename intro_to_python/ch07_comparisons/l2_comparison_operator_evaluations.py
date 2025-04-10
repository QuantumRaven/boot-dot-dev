#!/usr/bin/env python3


def compare_heights(edward_height, alphonse_height, winry_height, mustang_height):
    is_mustang_edward_same = edward_height == mustang_height
    is_alphones_edward_same = alphonse_height == edward_height
    is_winry_alphones_same = winry_height == alphonse_height

    return is_mustang_edward_same, is_alphones_edward_same, is_winry_alphones_same
