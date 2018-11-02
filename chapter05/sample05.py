import tkinter


def talk():
    # 入力ボックスの文字を取得
    value = entry.get()
    if not value:
        # 何も入力されていない場合
        value = "python >  なに?"
        # 表示ボックスに書き込み
        listbox.insert(tkinter.END, value)
    else:
        # 表示ボックスに書き込み
        listbox.insert(tkinter.END, value)
        # pythonによる自動レスポンス
        response = "python >  "
        if value == "おはよう":
            response += "おはよう。今日も頑張ろう"
        elif value == "こんにちは":
            response += "元気ですか？"
        elif value == "元気です":
            response += "よかった"
        else :
            response = "なんだかな～"
        # 表示ボックスに書き込み
        listbox.insert(tkinter.END, response)
    # 入力ボックスを空にします
    entry.delete(0,tkinter.END)
    # 表示エリアを一番下にスクロール
    listbox.yview('moveto', 1.0)


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
