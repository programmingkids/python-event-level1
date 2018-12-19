from tkinter import PhotoImage
from chapter11.monster import Monster


def get_map_images():
    map_images = [
        PhotoImage(file="../images/map01.png"),  # 0
        PhotoImage(file="../images/map02.png"),  # 1
        PhotoImage(file="../images/map04.png"),  # 2
        PhotoImage(file="../images/map05.png"),  # 3
        PhotoImage(file="../images/map15.png"),  # 4
        PhotoImage(file="../images/map16.png"),  # 5
        PhotoImage(file="../images/map17.png"),  # 6
        PhotoImage(file="../images/map07.png"),  # 7
        PhotoImage(file="../images/map18.png"),  # 8
    ]
    return map_images


def get_map():
    map_data = [
        [1, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2],
        [1, 1, 1, 1, 1, 1, 1, 1, 2, 6, 5, 6, 7, 2],
        [3, 3, 3, 3, 3, 3, 3, 1, 2, 4, 8, 4, 7, 2],
        [3, 1, 1, 1, 1, 1, 1, 1, 2, 4, 8, 4, 7, 2],
        [3, 1, 3, 3, 3, 3, 3, 3, 2, 4, 8, 4, 7, 2],
        [3, 1, 1, 1, 1, 1, 1, 1, 2, 4, 8, 4, 7, 2],
        [3, 3, 3, 3, 3, 3, 3, 1, 2, 4, 8, 4, 7, 2],
        [3, 1, 1, 1, 3, 1, 1, 1, 1, 4, 8, 4, 7, 2],
        [3, 1, 3, 1, 1, 1, 3, 2, 1, 6, 5, 6, 5, 0],
        [3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 0, 0],
    ]
    return map_data


def get_monster():
    monster_data = [
        Monster("スライムA", 10, 2, PhotoImage(file="../images/enemy01.png"), [11, 7]),
        Monster("スライムB", 10, 2, PhotoImage(file="../images/enemy01.png"), [11, 5]),
        Monster("スライムC", 10, 2, PhotoImage(file="../images/enemy01.png"), [11, 3]),
        Monster("毒蛇", 15, 5, PhotoImage(file="../images/enemy02.png"), [10, 8]),
        Monster("赤鬼A", 20, 7, PhotoImage(file="../images/enemy03.png"), [8, 7]),
        Monster("赤鬼B", 20, 7, PhotoImage(file="../images/enemy03.png"), [4, 3]),
        Monster("魔導士A", 30, 10, PhotoImage(file="../images/enemy04.png"), [3, 7]),
        Monster("魔導士B", 30, 10, PhotoImage(file="../images/enemy04.png"), [7, 1]),
        Monster("悪魔の騎士", 15, 12, PhotoImage(file="../images/enemy05.png"), [1, 5]),
        Monster("ドラゴン", 40, 15, PhotoImage(file="../images/enemy06.png"), [0, 0]),
    ]
    return monster_data
