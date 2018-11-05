import tkinter

# tkinterを初期化する
root = tkinter.Tk()

# タイトルを設定する
root.title()
# ウィンドウのサイズの設定
root.geometry("896x640")
# ウィンドウの最小サイズの設定（このサイズより小さくなりません）
root.minsize(896, 640)
# ウィンドウの最大サイズの設定（このサイズより大きくなりません）
root.maxsize(896, 640)

# キャンバスを作成 背景色は「青」、幅と高さはウィンドウと同じサイズにする
canvas = tkinter.Canvas(bg="white",width=896, height=640)
# キャンバスをウィンドウに配置
canvas.place(x=0, y=0)

# 画像ファイルを読み込みます


# 画像をキャンバスに表示します




# 画面を表示します
root.mainloop()
