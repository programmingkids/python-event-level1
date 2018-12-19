from chapter11complete.player import *
from chapter11complete.data import *
from chapter11complete.fight import *
from tkinter import *
from tkinter import messagebox


def draw_map():
    # マップ画像をキャンバスに表示します
    for x in range(WINDOW_X):
        for y in range(WINDOW_Y):
            image_index = map_data[y][x]
            canvas.create_image(32 + x * 64, 32 + y * 64, image=map_images[image_index])


def draw_player():
    # プレイヤ画像を表示
    image = player.image
    x = player.location[0]
    y = player.location[1]
    canvas.create_image(32 + x * 64, 32 + y * 64, image=image, tag="player")


def draw_monster():
    # モンスター画像を表示
    for monster in monster_data:
        x = monster.location[0]
        y = monster.location[1]
        image = monster.image
        name = monster.name
        canvas.create_image(32 + x * 64, 32 + y * 64, image=image, tag=name)


def move_player():
    # プレイヤ画像を再表示します
    x = player.location[0]
    y = player.location[1]
    canvas.coords("player", 32 + x * 64, 32 + y * 64)


def click_up_event(event):
    # 上キーでYが1減少
    x = player.location[0]
    y = player.location[1]
    check_move_player(x, y - 1)


def click_down_event(event):
    # 下キーでYが1増加
    x = player.location[0]
    y = player.location[1]
    check_move_player(x, y + 1)


def click_left_event(event):
    # 左キーでXが1減少
    x = player.location[0]
    y = player.location[1]
    check_move_player(x - 1, y)


def click_right_event(event):
    # 右キーでXが1増加
    x = player.location[0]
    y = player.location[1]
    check_move_player(x + 1, y)


def check_move_player(x, y):
    # ウィンドウから、はみ出すかどうかのチェック
    if x < 0 or x >= WINDOW_X or y < 0 or y >= WINDOW_Y:
        # はみ出す場合、移動しない
        return
    # マップデータ内のインデックスが「2,3,7,8」は移動できないこととする
    if map_data[y][x] == 2 or map_data[y][x] == 3 or map_data[y][x] == 7 or map_data[y][x] == 8 or map_data[y][x] == 10:
        # 移動しない
        return
    # 移動後の座標をプレイヤに代入
    player.location = [x, y]
    # プレイヤ画像の移動
    move_player()
    # 移動後にモンスターと出会っているかどうかを判定
    check_monster()


def check_monster():
    # プレイヤの座標にモンスターが存在するかどうかをチェックする
    player_x = player.location[0]
    player_y = player.location[1]
    for monster in monster_data:
        monster_x = monster.location[0]
        monster_y = monster.location[1]
        if player_x == monster_x and player_y == monster_y:
            # プレイヤ座標にモンスターがいるので戦闘開始
            fight.start(player, monster, fight_end)


def fight_end(status, monster):
    if status == "escape":
        # 逃げるなら何もしない
        return
    elif status == "win":
        # 戦闘に勝った場合、モンスターでリストから削除
        monster_data.remove(monster)
        # キャンバスから削除
        canvas.delete(monster.name)
    elif status == "lost":
        # 戦闘に負けた場合、メッセージを出す
        message = player.name + "は負けました"
        messagebox.showwarning("ゲームオーバー", message)
        # ウィンドウを終了
        root.quit()

    # モンスターデータが空なら全てのモンスターを倒したことになる
    if not monster_data:
        # 全てのモンスターを倒したのでゲームクリア
        message = player.name + "は全てのモンスターを倒しました"
        messagebox.showinfo("おめでとう", message)


# ウィンドウの座標幅
WINDOW_X = 14
WINDOW_Y = 10

WINDOW_WIDTH = 896
WINDOW_HEIGHT = 640

# tkinterを初期化する
root = Tk()
# タイトルを設定する
root.title("RPG")
# ウィンドウのサイズの設定
root.geometry(str(WINDOW_WIDTH) + "x" + str(WINDOW_HEIGHT))
# ウィンドウの最小サイズの設定（このサイズより小さくなりません）
root.minsize(WINDOW_WIDTH, WINDOW_HEIGHT)
# ウィンドウの最大サイズの設定（このサイズより大きくなりません）
root.maxsize(WINDOW_WIDTH, WINDOW_HEIGHT)

# キーボードイベントを登録する
frame = Frame(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
frame.bind("<Up>", click_up_event)
frame.bind("<Down>", click_down_event)
frame.bind("<Left>", click_left_event)
frame.bind("<Right>", click_right_event)
frame.focus_set()
frame.pack()

# キャンバスを作成 背景色は「白」、幅と高さはウィンドウと同じサイズにする
canvas = Canvas(bg="white",width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
# キャンバスをウィンドウに配置
canvas.place(x=0, y=0)

# マップ画像を読み込みます
map_images = get_map_images()
map_data = get_map()

# プレイヤ画像を読み込み
player = Player("レイナ", 40, 20, PhotoImage(file="../images/chara02.png"), [13, 9])

# モンスターデータを読み込み
monster_data = get_monster()

# マップの初期表示
draw_map()
# プレイヤ画像の初期表示
draw_player()
# モンスター画像の初期表示
draw_monster()
# 戦闘画面の初期化
fight = Fight(WINDOW_WIDTH, WINDOW_HEIGHT)

# 画面を表示します
root.mainloop()
