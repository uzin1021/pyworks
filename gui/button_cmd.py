from  tkinter import *

def click():
    print("hello.python")

root = Tk()
root.title("hello")
root.geometry("300x100+300+400")

frame = Frame(root)
frame.pack()

Button(frame, text="확인", command=click).grid(row = 1, column = 1)
# click옆 () 생략 이유 : 버튼 누를때만 함수 작동, ()있을 경우 함수 생성시점으로 이동해서 작동x

root.mainloop()