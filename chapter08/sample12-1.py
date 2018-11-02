import tkinter


def draw_map():
    # マップ画像をキャンバスに表示します
    for x in range(14):
        for y in range(10):
            canvas.create_image(32 + x * 64, 32 + y * 64, image=map)


# tkinterを初期化する
root = tkinter.Tk()

# タイトルを設定する
root.title("サンプル12")
# ウィンドウのサイズの設定
root.geometry("896x640")
# ウィンドウの最小サイズの設定（このサイズより小さくなりません）
root.minsize(896, 640)
# ウィンドウの最大サイズの設定（このサイズより大きくなりません）
root.maxsize(896, 640)

# マップ画像を読み込みます
map = tkinter.PhotoImage(file="../images/map01.png")

# キャンバスを作成 背景色は「青」、幅と高さはウィンドウと同じサイズにする
canvas = tkinter.Canvas(bg="white",width=896, height=640)
# キャンバスをウィンドウに配置
canvas.place(x=0, y=0)

# マップの初期表示
draw_map()

# 画面を表示します
root.mainloop()
