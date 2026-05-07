import os
import os as _os
import pygame
import sys
import random
import math

pygame.init()

WIDTH, HEIGHT = 1250, 770

# ─────────────────────────────────────────────
#  HELPER: safe image load (returns coloured
#  placeholder if file is missing)
# ─────────────────────────────────────────────


def safe_load(path, fallback_size=(64, 64), fallback_color=(200, 100, 200)):
    try:
        return pygame.image.load(path).convert_alpha()
    except Exception:
        surf = pygame.Surface(fallback_size, pygame.SRCALPHA)
        surf.fill(fallback_color)
        return surf


def safe_scale(surf, size):
    return pygame.transform.smoothscale(surf, size)


# ─────────────────────────────────────────────
#  IMAGES
# ─────────────────────────────────────────────

start_bg = safe_scale(safe_load(
    "start.png",                   (WIDTH, HEIGHT), (10, 8, 20)),    (WIDTH, HEIGHT))


# ─────────────────────────────────────────────
#  WINDOW
# ─────────────────────────────────────────────

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pydew Valley")
clock = pygame.time.Clock()
screen.blit(start_bg, (0, 0))
