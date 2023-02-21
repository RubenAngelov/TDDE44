#!/usr/bin/env python
#
# A text-based adventure game, based on
# https://github.com/codinggrace/text_based_adventure_game
#
# MIT License
# Copyright (c) 2020 Coding Grace
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import gamedata
import pictures

def get_next_state(state):
    succ_states = gamedata.ADVENTURE_TREE[state]
    
    if len(succ_states) == 1:
        return succ_states[0]

    options_text = "{}  {}\n{}  {}".format("1", gamedata.OPTIONS[succ_states[0]],
                                       "2", gamedata.OPTIONS[succ_states[1]])
    print(options_text)
    inp = input(">> ")

    if inp == "1":
        return succ_states[0]
    elif inp == "2":
        return succ_states[1]

def print_pic(state):
    if state == "Start":
        pictures.print_doors()
    elif state == "Red":
        pictures.print_dragon()
    elif state == "Chest":
        pictures.print_treasure()
    elif state == "Sneak" or state == "Talk":
        pictures.print_guard()
    elif state == "Attack":
        pictures.print_game_over()

def main():
    name = input("What's your name?\n>> ")
    print("Welcome {} to the adventure of your life. Try to survive and find the \
    treasure!".format(name.upper()))

    current_state = "Start"

    while current_state != "End":
        succ_states = gamedata.ADVENTURE_TREE[current_state]
        description = gamedata.DESCRIPTIONS[current_state]
        print_pic(current_state)
        print(description)
        current_state = get_next_state(current_state)

main()