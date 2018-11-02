import tkinter


def add():
    # 入力ボックス1の値を取得
    value1 = entry1.get()
    # 入力ボックス2の値を取得
    value2 = entry2.get()
    # 足し算を実行
    result = int(value1) + int(value2)
    # 入力ボックス3をいったん空にします
    entry3.delete(0,tkinter.END)
    # 入力ボックス3に計算結果を代入します
    entry3.insert(0,result)


# tkinterを初期化する
root = tkinter.Tk()

# タイトルを設定する
root.title("サンプル04")
# ウィンドウのサイズの設定
root.geometry("500x400")
# ウィンドウの最小サイズの設定（このサイズより小さくなりません）
root.minsize(500, 400)
# ウィンドウの最大サイズの設定（このサイズより大きくなりません）
root.maxsize(500, 400)
# フォント
root.option_add("*font",["System", 20])

# 入力ボックス1
entry1 = tkinter.Entry(width=5, bd=2)
entry1.pack(side="left", anchor="n")

# 「＋」のラベル
label = tkinter.Label(root, text="+")
label.pack(side="left", anchor="n")

# 入力ボックス2
entry2 = tkinter.Entry(width=5, bd=2)
entry2.pack(side="left", anchor="n")

# 「=」のボタン クリックすると足し算が実行されます
answerButton = tkinter.Button(text="=")
answerButton.pack(side="left", anchor="n")
answerButton["command"] = add

# 入力ボックス3 足し算の結果を表示するボックス
entry3 = tkinter.Entry(width=5, bd=2)
entry3.pack(side="left", anchor="n")

# 画面を表示します
root.mainloop()
