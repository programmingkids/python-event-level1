import tkinter
import chapter10.player as player
import chapter10.data as data
import chapter10.fight as fight
import tkinter.messagebox


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


# ウィンドウの座標幅
WINDOW_X = 14
WINDOW_Y = 10

WINDOW_WIDTH = 896
WINDOW_HEIGHT = 640

# tkinterを初期化する
root = tkinter.Tk()
# タイトルを設定する
root.title("RPG")
# ウィンドウのサイズの設定
root.geometry(str(WINDOW_WIDTH) + "x" + str(WINDOW_HEIGHT))
# ウィンドウの最小サイズの設定（このサイズより小さくなりません）
root.minsize(WINDOW_WIDTH, WINDOW_HEIGHT)
# ウィンドウの最大サイズの設定（このサイズより大きくなりません）
root.maxsize(WINDOW_WIDTH, WINDOW_HEIGHT)

# キャンバスを作成 背景色は「白」、幅と高さはウィンドウと同じサイズにする
canvas = tkinter.Canvas(bg="white",width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
# キャンバスをウィンドウに配置
canvas.place(x=0, y=0)

# マップ画像を読み込みます
map_images = data.get_map_images()
map_data = data.get_map()

# プレイヤ画像を読み込み
player = player.Player("パイソン", 30, 10, tkinter.PhotoImage(file="../images/chara01.png"), [13, 9])

# モンスターデータを読み込み
monster_data = data.get_monster()

# マップの初期表示
draw_map()
# プレイヤ画像の初期表示
draw_player()
# モンスター画像の初期表示
draw_monster()

# 画面を表示します
root.mainloop()
