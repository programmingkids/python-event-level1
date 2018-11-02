import tkinter
import chapter11.monster as monster


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
        tkinter.PhotoImage(file="../images/map03.png"),  # 9
        tkinter.PhotoImage(file="../images/map06.png"),  # 10
    ]
    return map_images


def get_map():
    map_data = [
        [9, 10, 10, 10, 10, 10, 10, 2, 2, 2, 2, 2, 4, 0],
        [9, 9, 9, 9, 9, 9, 9, 0, 0, 0, 0, 0, 4, 0],
        [10, 9, 10, 9, 9, 9, 9, 5, 5, 5, 5, 5, 6, 5],
        [10, 9, 9, 9, 9, 9, 9, 0, 7, 0, 0, 0, 4, 0],
        [10, 9, 9, 9, 9, 9, 9, 0, 0, 0, 0, 0, 4, 0],
        [10, 9, 9, 10, 9, 9, 9, 0, 0, 7, 0, 0, 4, 0],
        [10, 9, 9, 9, 9, 9, 9, 0, 0, 0, 0, 0, 4, 0],
        [10, 9, 9, 9, 9, 9, 9, 0, 0, 0, 0, 0, 4, 0],
        [10, 9, 9, 9, 9, 9, 9, 0, 0, 0, 0, 0, 4, 0],
        [10, 10, 10, 10, 10, 10, 10, 2, 2, 2, 2, 2, 4, 0],
    ]
    return map_data


def get_monster():
    monster_data = [
        monster.Monster("海賊", 30, 10, tkinter.PhotoImage(file="../images/robot4.png"), [12, 8], 7),
        monster.Monster("スライムB", 10, 2, tkinter.PhotoImage(file="../images/enemy01.png"), [11, 5], 4),
        monster.Monster("スライムC", 10, 2, tkinter.PhotoImage(file="../images/enemy01.png"), [11, 3], 4),
        monster.Monster("毒蛇", 15, 5, tkinter.PhotoImage(file="../images/enemy02.png"), [10, 8], 5),
        monster.Monster("赤鬼A", 20, 7, tkinter.PhotoImage(file="../images/enemy03.png"), [8, 7], 5),
        monster.Monster("赤鬼B", 20, 7, tkinter.PhotoImage(file="../images/enemy03.png"), [4, 3], 5),
        monster.Monster("魔導士A", 30, 10, tkinter.PhotoImage(file="../images/enemy04.png"), [3, 7], 8),
        monster.Monster("魔導士B", 30, 10, tkinter.PhotoImage(file="../images/enemy04.png"), [7, 1], 8),
        monster.Monster("悪魔の騎士", 15, 12, tkinter.PhotoImage(file="../images/enemy05.png"), [1, 5], 15),
        monster.Monster("ドラゴン", 40, 15, tkinter.PhotoImage(file="../images/enemy06.png"), [0, 0], 18),
        monster.Monster("カエル", 10, 5, tkinter.PhotoImage(file="../images/robot3.png"), [9, 2], 5),
        monster.Monster("海賊", 10, 5, tkinter.PhotoImage(file="../images/robot4.png"), [9, 3], 7),
        monster.Monster("忍者", 20, 10, tkinter.PhotoImage(file="../images/robot5.png"), [9, 4], 7),
        monster.Monster("サムライ", 30, 10, tkinter.PhotoImage(file="../images/robot6.png"), [9, 5], 10),
        monster.Monster("サンダー", 30, 15, tkinter.PhotoImage(file="../images/robot7.png"), [9, 6], 10),
        monster.Monster("緑竜", 40, 20, tkinter.PhotoImage(file="../images/robot9.png"), [9, 7], 15),
    ]
    return monster_data
