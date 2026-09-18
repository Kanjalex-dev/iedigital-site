#!/usr/bin/env python3
"""Rastérise la marque IE DIGITAL depuis sa géométrie, pas depuis une image.

La marque n'est faite que de rectangles : on la dessine directement à la
taille demandée plutôt que de redimensionner un PNG, ce qui garantit des
arêtes nettes à 32 px comme à 1024. Le suréchantillonnage ×4 sert uniquement
aux coordonnées non entières (10,5 et 13,5 dans la grille de 32).
"""
from PIL import Image, ImageDraw

INK = (18, 24, 26, 255)        # --ink    #12181A
GROUND = (241, 243, 241, 255)  # --ground #F1F3F1
ACCENT = (15, 107, 74, 255)    # --accent #0F6B4A
SS = 4                         # suréchantillonnage

# Grille de 32 : la marque seule, telle qu'elle est dans mark.svg.
BARS_32 = [
    (4,  4.0,  4, 24.0, INK),
    (11, 7.0,  4, 18.0, INK),
    (18, 10.5, 4, 11.0, INK),
    (25, 13.5, 3,  5.0, ACCENT),
]

# Grille de 88 : l'icône carrée, barres évidées sur fond encre.
BARS_88 = [
    (18, 20, 9, 48, GROUND),
    (33, 26, 9, 36, GROUND),
    (48, 33, 9, 22, GROUND),
    (63, 39, 7, 10, ACCENT),
]


def render(size: int, grid: int, bars, background) -> Image.Image:
    big = size * SS
    img = Image.new("RGBA", (big, big), background)
    d = ImageDraw.Draw(img)
    k = big / grid
    for x, y, w, h, fill in bars:
        d.rectangle([x * k, y * k, (x + w) * k - 1, (y + h) * k - 1], fill=fill)
    return img.resize((size, size), Image.LANCZOS)


OUT = [
    ("favicon-32.png", 32, 32, BARS_32, GROUND),
    ("favicon-64.png", 64, 32, BARS_32, GROUND),
    ("apple-touch-icon.png", 180, 88, BARS_88, INK),
    ("icon-512.png", 512, 88, BARS_88, INK),
    ("icon-1024.png", 1024, 88, BARS_88, INK),
]

if __name__ == "__main__":
    for name, size, grid, bars, bg in OUT:
        render(size, grid, bars, bg).save(name)
        print(f"{name:24} {size}×{size}")
