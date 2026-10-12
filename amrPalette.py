from amrShared import *
from PIL import Image

def importPalette(romFile, paletteFile):
    img = Image.open(paletteFile)
    palette = img.getpalette()
    palette_list = []
    for i in range(len(palette) // 3):
        c1 = palette[3*i+0] >> 3
        c2 = palette[3*i+1] >> 3
        c3 = palette[3*i+2] >> 3
        color = (c3 << 10) | (c2 << 5) | c1
        palette_list.append(color & 0x00FF)
        palette_list.append((color & 0xFF00) >> 8)
        color = ((color & 0xFF00) >> 8) | ((color & 0x00FF) << 8)
        print(hex(color))
    for i, v in enumerate(palette_list):
        writeValueToRom(romFile, 4960556 +  i, v, 1)