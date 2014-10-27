# Description

A little application that will list *Twitch.tv* streams for your favorite game.

eg: `$ twilist`

# Install

`sudo pip install twilist`

OR

You can download the script and use `python twilist.py`

OR

`make install`

# Parameters

- `--game` (default: 'Dota 2'): is the name of the game to parse.
- `--limit` (default: 10): how many do you want to display.
- `--browser` (default: 'chromium'): which browser to open.
- `--help`: this option will make you win 10k gold on World of Warcraft !

eg: `$ twilist --game 'World of warcraft' --limit 20 --browser firefox`

# Dependencies

- Python 3, PIP (`sudo pacman -S python3 python-pip`)
- Colorama (`sudo pip install colorama`) *automatically installed by `pip` or `make`*

# Screenshot
![Alt text](/screenshot.png?raw=true "Screenshot on the fly !")



