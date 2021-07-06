from  tkinter import *

def click():
    en_text = entry.get()
    text.insert(END,en_text)

root = Tk()
root.title("hello")
root.geometry("300x200+300+400")

frame = Frame(root)
frame.pack()

Label(frame, text="이름: ").grid(row=0, column=0)
entry = Entry(frame,width= 10)
entry.grid(row = 0,column= 1)
Button(frame, text="확인", command=click).grid(row = 1, column = 1)
# click옆 () 생략 이유 : 버튼 누를때만 함수 작동, ()있을 경우 함수 생성시점으로 이동해서 작동x
text = Text(frame, width= 20, height=10)
text.grid(row=2, column =1)

root.mainloop()