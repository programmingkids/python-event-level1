import tkinter

# tkinterを初期化する
root = tkinter.Tk()
# タイトルを設定する
root.title("サンプル02")
# ウィンドウのサイズの設定
root.geometry("500x400")
# ウィンドウの最小サイズの設定（このサイズより小さくなりません）
root.minsize(500, 400)
# ウィンドウの最大サイズの設定（このサイズより大きくなりません）
root.maxsize(500, 400)
# フォント
root.option_add("*font",["System", 20])

# 画面に文字を表示
label = tkinter.Label(root, text="Hello Python")
# 画面に表示する位置の設定
label.place(x=0, y=0)

# 画面を表示します
root.mainloop()
