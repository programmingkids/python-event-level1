import tkinter
import chapter10.player as player
import chapter10.data as data
import chapter10.fight as fight
import tkinter.messagebox

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

# 画面を表示します
root.mainloop()
