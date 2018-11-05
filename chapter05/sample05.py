import tkinter


def talk():




# tkinterを初期化する
root = tkinter.Tk()

# タイトルを設定する
root.title("サンプル05")
# ウィンドウのサイズの設定
root.geometry("600x550")
# ウィンドウの最小サイズの設定（このサイズより小さくなりません）
root.minsize(600, 550)
# ウィンドウの最大サイズの設定（このサイズより大きくなりません）
root.maxsize(600, 550)
# フォント
root.option_add("*font",["System", 20])

# フレームの作成
frame = tkinter.Frame(root)
frame.pack()

# 表示ボックス
listbox = tkinter.Listbox(frame, width=40, height=19)
listbox.pack(side=tkinter.LEFT)

# 表示ボックスにスクロールバーを表示する
scrollbar = tkinter.Scrollbar(frame, orient=tkinter.VERTICAL)
scrollbar.config(command=listbox.yview)
scrollbar.pack(side=tkinter.LEFT, fill=tkinter.Y)

# フレームの作成
frame2 = tkinter.Frame(root, width=40)
frame2.pack(side=tkinter.TOP, pady=10)

# 入力ボックスの作成
entry = tkinter.Entry(frame2, width=30, bd=2)
entry.pack(side=tkinter.LEFT, padx=10)
entry.focus_set()

# 話すボタン
button = tkinter.Button(frame2, text='話す')
button.pack(side=tkinter.LEFT)
# 話すボタンがクリックされたときの動作
button["command"] = talk

# 画面を表示します
root.mainloop()
