import tkinter

# tkinterを初期化する
root = tkinter.Tk()

# タイトルを設定する
root.title("サンプル03")
# ウィンドウのサイズの設定
root.geometry("500x400")
# ウィンドウの最小サイズの設定（このサイズより小さくなりません）
root.minsize(500, 400)
# ウィンドウの最大サイズの設定（このサイズより大きくなりません）
root.maxsize(500, 400)

# キャンバスを作成 背景色は「青」、幅と高さはウィンドウと同じサイズにする
canvas = tkinter.Canvas(bg="blue",width=500, height=400)
# キャンバスをウィンドウに配置
canvas.place(x=0, y=0)

# 画像ファイルを読み込みます
image = tkinter.PhotoImage(file="../images/robot.png")
# 画像をキャンバスに表示します
canvas.create_image(32, 32, image=image)

# 画面を表示します
root.mainloop()
