import os
import sys

vendor_path = os.path.join(os.path.dirname(__file__), 'vendor/picotool')
sys.path.append(vendor_path)

from pico8.game import game

XML_PREAMBLE = """<?xml version="1.0" encoding="UTF-8"?>
<map version="1.0" tiledversion="1.1.6" orientation="orthogonal" renderorder="right-down" width="128" height="64" tilewidth="8" tileheight="8" infinite="0" nextobjectid="1">
 <tileset firstgid="1" source="tileset.tsx"/>
 <layer name="Tile Layer 1" width="128" height="64">
  <data encoding="csv">
"""

XML_POSTAMBLE = """</data>
 </layer>
</map>
"""


def main():
    g = game.Game.from_filename(sys.argv[1])  # type: pico8.game
    lines = []
    for y in range(64):
        tiles = []
        for x in range(128):
            tile = g.map.get_cell(x, y) + 1
            if tile == 1:
                tile = 0
            tiles.append(str(tile))
        line = ",".join(tiles)
        lines.append(line)

    with open(sys.argv[2], 'w') as f:
        f.write(XML_PREAMBLE)
        f.write(",\r\n".join(lines))
        f.write(XML_POSTAMBLE)

    print("Wrote {}".format(sys.argv[2]))


if __name__ == '__main__':
    main()
