#Josh Muszka
#PROJECT START DATE: June 15, 2023
#LAST UPDATED: June 15, 2023
#GOAL: to make an Emulation hub for Nintendo games. Simply choose a game and play

import os
from shutil import copy
from emulator import *
from game import *

#GLOBAL CONSOLE VARIABLES
NES = "nes"
SNES = "snes"
N64 = "n64"


#Generate JSON file for emulator
def make_emulator(name, command, system=""):
    emu_dict = {"system":system, "command":command}

    with open(f'{os.getcwd()}/core/json/{name}.json', "w") as json_file:
        json.dump(emu_dict, json_file)

    return f'core/json/{name}.json'


#Generate JSON file for game, and move ROM file
def make_game(file, directory, system, name="", release=""):

    #check if a valid game system was entered
    if (system != NES and system != SNES and system != N64):
        raise Exception("Invalid console")

    #TODO: copy roms to respective folder
    new_dir = f'{os.getcwd()}/core/{system}/{file}'
    copy(directory, new_dir)

    #make json file
    file_name = file.split(".")[0]
    game_dict = {"name":name, "system":system, "release":release, "directory":directory}
    with open(f'{os.getcwd()}/core/json/{file_name}.json', "w") as json_file:
        json.dump(game_dict, json_file)

    return f'core/json/{file_name}.json'


#Set up games
mario1 = make_game("supermariobros.nes", "/home/jmuszka/Downloads/supermariobros.nes", NES, "Super Mario Bros.", "1985")
mario2 = make_game("lostlevels.nes", "/home/jmuszka/Downloads/lostlevels.nes", NES, "Super Mario Bros. The Lost Levels", "1986")
tetris = make_game("tetris.nes", "/home/jmuszka/Downloads/tetris.nes", NES, "Tetris", "1984")
marioworld = make_game("supermarioworld.smc", "/home/jmuszka/Downloads/supermarioworld.smc", SNES, "Super Mario World", "1990")
mario64 = make_game("supermario64.z64", "/home/jmuszka/Downloads/supermario64.z64", N64, "Super Mario 64", "1996")

mario1 = Game(mario1)
mario2 = Game(mario2)
tetris = Game(tetris)
marioworld = Game(marioworld)
mario64 = Game(mario64)


#Set up emulator
nes_json = make_emulator(NES, "fceux", "Nintendo Entertainment System")
nes = Emulator(nes_json)

snes_json = make_emulator(SNES, "flatpak run com.snes9x.Snes9x", "Super NES")
snes = Emulator(snes_json)

n64_json = make_emulator(N64, "mupen64plus", "Nintendo 64")
n64 = Emulator(n64_json)

#Play!
n64.play(mario64)