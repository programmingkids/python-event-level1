import tkinter
import random
import time


class Fight:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def create_frame(self):
        # メインフレームの作成
        self.main_frame = tkinter.Frame()
        self.main_frame.place(x=0, y=0, width=self.width, height=self.height)

        top_frame = tkinter.Frame(self.main_frame)
        top_frame.pack(side=tkinter.TOP,fill=tkinter.X, padx=30,pady=40)

        # メッセージボックス
        self.listbox = tkinter.Listbox(top_frame, width=40, height=20)

        # メッセージボックスにスクロールバーを表示する
        scrollbar = tkinter.Scrollbar(top_frame, orient=tkinter.VERTICAL)
        scrollbar.config(command=self.listbox.yview)
        scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        self.listbox.pack(side=tkinter.RIGHT)

        # 画像を表示するキャンバス
        self.canvas = tkinter.Canvas(self.main_frame, width=200, height=600)
        self.canvas.place(x=0, y=0)

        labelfont = ('System', 18)
        label_monster_a = tkinter.Label(top_frame, text="敵の名前", justify="left")
        label_monster_a.config(font=labelfont)
        label_monster_a.place(x=230, y=50)

        label_monster_b = tkinter.Label(top_frame, text="敵のHP", justify="left")
        label_monster_b.place(x=230, y=90)
        label_monster_b.config(font=labelfont)

        # モンスターの名前を表示するラベル
        self.label_monster_name = tkinter.Label(top_frame, justify="left")
        self.label_monster_name.config(font=labelfont)
        self.label_monster_name.place(x=350, y=50)

        # モンスターのHPを表示するラベル
        self.label_monster_hp = tkinter.Label(top_frame, justify="left")
        self.label_monster_hp.place(x=350, y=90)
        self.label_monster_hp.config(font=labelfont)

        label_player_a = tkinter.Label(top_frame, text="名前", justify="left")
        label_player_a.config(font=labelfont)
        label_player_a.place(x=230, y=220)

        label_player_b = tkinter.Label(top_frame, text="HP", justify="left")
        label_player_b.place(x=230, y=260)
        label_player_b.config(font=labelfont)

        #  プレイヤの名前を表示するラベル
        self.label_player_name = tkinter.Label(top_frame, justify="left")
        self.label_player_name.config(font=labelfont)
        self.label_player_name.place(x=350, y=220)

        # プレイヤのHPを表示するラベル
        self.label_player_hp = tkinter.Label(top_frame, justify="left")
        self.label_player_hp.place(x=350, y=260)
        self.label_player_hp.config(font=labelfont)

        # 下側のボタンを配置するフレーム
        bottom_frame = tkinter.Frame(self.main_frame, bg="black")
        bottom_frame.pack(side=tkinter.BOTTOM)

        # 攻撃ボタン
        self.button_attack = tkinter.Button(bottom_frame, text="攻撃する", width=30, height=2)
        self.button_attack.pack( side=tkinter.LEFT, padx=20, pady=20)
        self.button_attack["command"] = self.fight

        # 待つ＆回復ボタン
        self.button_wait = tkinter.Button(bottom_frame, text="待つ＆回復", width=30, height=2)
        self.button_wait.pack( side=tkinter.LEFT, padx=20, pady=20)
        self.button_wait["command"] = self.wait

        # 逃げるボタン
        self.button_escape = tkinter.Button(bottom_frame, text="逃げる", width=30, height=2)
        self.button_escape.pack( side=tkinter.LEFT, padx=20, pady=20)
        self.button_escape["command"] = self.escape

    def start(self, player, monster, fight_end):
        # フレームを作成
        self.create_frame()
        # プレイヤを表示
        self.player = player
        self.player_image = self.player.image.zoom(2)
        self.canvas.create_image(100, 300, image=self.player_image)
        self.label_player_name["text"] = self.player.name
        self.label_player_hp["text"] = self.player.hp

        # モンスターを表示
        self.monster = monster
        self.monster_image = self.monster.image.zoom(2)
        self.canvas.create_image(100, 100, image=self.monster_image)
        self.label_monster_name["text"] = self.monster.name
        self.label_monster_hp["text"] = self.monster.hp

        # 戦闘終了時の処理を代入
        self.fight_end = fight_end
        self.main_frame.place(x=0, y=0, width=self.width, height=self.height)

        # メッセージ
        self.add_message(self.monster.name + "が現れた")
        self.add_message("===========")

    def fight(self):
        self.disable_button()
        # プレイヤーの攻撃
        self.attack_player()

        self.main_frame.update()
        time.sleep(1)

        # モンスターを倒した
        if self.monster.hp <= 0:
            self.normal_button()
            self.add_message(self.monster.name + "を倒した")
            self.add_message("===========")
            self.close_main_frame()
            self.fight_end("win", self.monster)
            return

        # モンスターの攻撃
        self.attack_monster()
        # プレイヤが負けた
        if self.player.hp <= 0:
            self.normal_button()
            self.add_message(self.player.name + "は負けた")
            self.close_main_frame()
            self.fight_end("lost", self.monster)
            return
        self.add_message("===========")
        self.normal_button()

    def wait(self):
        self.disable_button()
        self.recover_player()

        self.main_frame.update()
        time.sleep(1)

        # モンスターの攻撃
        self.attack_monster()
        # プレイヤが負けた
        if self.player.hp <= 0:
            self.normal_button()
            self.add_message(self.player.name + "は負けた")
            self.close_main_frame()
            self.fight_end("lost", self.monster)
            return
        self.add_message("===========")
        self.normal_button()

    def escape(self):
        self.disable_button()
        self.add_message(self.player.name + "は逃げ出した")
        self.add_message("===========")
        self.normal_button()
        self.close_main_frame()
        self.fight_end("escape", self.monster)

    def close_main_frame(self):
        self.main_frame.update()
        time.sleep(2)
        self.listbox.delete(0, tkinter.END)
        self.main_frame.destroy()

    def add_message(self, message):
        self.listbox.insert(tkinter.END, message)
        self.listbox.yview('moveto', 1.0)

    def disable_button(self):
        self.button_attack["state"] = "disabled"
        self.button_wait["state"] = "disabled"
        self.button_escape["state"] = "disabled"

    def normal_button(self):
        self.button_attack["state"] = "normal"
        self.button_wait["state"] = "normal"
        self.button_escape["state"] = "normal"

    def attack_player(self):
        # 乱数でプレイヤの攻撃値を作成
        attack = random.randint(0,self.player.attack)
        self.add_message(self.player.name + "の攻撃")
        self.add_message(str(attack) + "のダメージを与えた")
        # モンスターのHPを減少させる
        self.monster.hp -= attack
        if self.monster.hp < 0:
            self.monster.hp = 0
        self.label_monster_hp["text"] = self.monster.hp

    def attack_monster(self):
        # 乱数でモンスターの攻撃値を作成
        attack = random.randint(0,self.monster.attack)
        self.add_message(self.monster.name + "の攻撃")
        self.add_message(str(attack) + "のダメージを受けた")
        # プレイヤのHPを減少させる
        self.player.hp -= attack
        if self.player.hp < 0:
            self.player.hp = 0
        self.label_player_hp["text"] = self.player.hp

    def recover_player(self):
        # 固定値で「10」回復させる
        hp = 10
        self.add_message(self.player.name + "の体力が" + str(hp) +"回復した")
        self.player.hp += hp
