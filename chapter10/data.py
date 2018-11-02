import tkinter
import chapter10.monster as monster


def get_map_images():
    map_images = [
        tkinter.PhotoImage(file="../images/map01.png"),  # 0
        tkinter.PhotoImage(file="../images/map02.png"),  # 1
        tkinter.PhotoImage(file="../images/map04.png"),  # 2
        tkinter.PhotoImage(file="../images/map05.png"),  # 3
        tkinter.PhotoImage(file="../images/map15.png"),  # 4
        tkinter.PhotoImage(file="../images/map16.png"),  # 5
        tkinter.PhotoImage(file="../images/map17.png"),  # 6
        tkinter.PhotoImage(file="../images/map07.png"),  # 7
        tkinter.PhotoImage(file="../images/map18.png"),  # 8
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
        monster.Monster("スライムA", 10, 2, tkinter.PhotoImage(file="../images/enemy01.png"), [11, 7]),
        monster.Monster("スライムB", 10, 2, tkinter.PhotoImage(file="../images/enemy01.png"), [11, 5]),
        monster.Monster("スライムC", 10, 2, tkinter.PhotoImage(file="../images/enemy01.png"), [11, 3]),
        monster.Monster("毒蛇", 15, 5, tkinter.PhotoImage(file="../images/enemy02.png"), [10, 8]),
        monster.Monster("赤鬼A", 20, 7, tkinter.PhotoImage(file="../images/enemy03.png"), [8, 7]),
        monster.Monster("赤鬼B", 20, 7, tkinter.PhotoImage(file="../images/enemy03.png"), [4, 3]),
        monster.Monster("魔導士A", 30, 10, tkinter.PhotoImage(file="../images/enemy04.png"), [3, 7]),
        monster.Monster("魔導士B", 30, 10, tkinter.PhotoImage(file="../images/enemy04.png"), [7, 1]),
        monster.Monster("悪魔の騎士", 15, 12, tkinter.PhotoImage(file="../images/enemy05.png"), [1, 5]),
        monster.Monster("ドラゴン", 40, 15, tkinter.PhotoImage(file="../images/enemy06.png"), [0, 0]),
    ]
    return monster_data
