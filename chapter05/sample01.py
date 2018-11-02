import tkinter

# tkinterを初期化する
root = tkinter.Tk()
# タイトルを設定する
root.title("サンプル01")
# ウィンドウのサイズの設定
root.geometry("500x400")
# ウィンドウの最小サイズの設定（このサイズより小さくなりません）
root.minsize(500, 400)
# ウィンドウの最大サイズの設定（このサイズより大きくなりません）
root.maxsize(500, 400)
# 画面を表示します
root.mainloop()
