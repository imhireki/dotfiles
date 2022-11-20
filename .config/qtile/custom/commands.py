from libqtile.command.client import InteractiveCommandClient

import sys


def change_to_layout(index: str) -> None:
    qtile = InteractiveCommandClient()
    qtile.to_layout_index(int(index))


if __name__ == '__main__':
    if sys.argv[1] == 'change_to_layout':
        change_to_layout(sys.argv[2])


