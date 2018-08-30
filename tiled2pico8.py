import re
import sys
import xml.etree.ElementTree
import os

vendor_path = os.path.join(os.path.dirname(__file__), 'vendor/picotool')
sys.path.append(vendor_path)

from pico8.game import game


def v_idx(x, y):
    return y * 128 + x


def main():
    filename = sys.argv[1]
    e = xml.etree.ElementTree.parse(filename).getroot()
    data = e.find('.//data')
    tiles = [int(tile) - 1 for tile in re.split(r'[\s,]+', data.text) if tile != '']
    if len(tiles) != 4096:
        print("Invalid tiled format")
        sys.exit(1)

    g = game.Game.from_filename(sys.argv[2])  # type: pico8.game

    for y in range(32):
        for x in range(128):
            g.map.set_cell(x, y, tiles[v_idx(x, y)])

    with open(sys.argv[3], 'wb+') as f:
        g.to_p8_file(f)
        print('Written {}'.format(f))


if __name__ == '__main__':
    main()
