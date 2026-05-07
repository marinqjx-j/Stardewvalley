import os
import os as _os
import pygame
import sys
import random
import math

pygame.init()

# ─────────────────────────────────────────────
#  WINDOW
# ─────────────────────────────────────────────
WIDTH, HEIGHT = 1250, 770
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pydew Valley")
clock = pygame.time.Clock()
