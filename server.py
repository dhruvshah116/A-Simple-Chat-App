import socket
import tkinter as tk

s=socket.socket()
s.bind(('localhost',5555))
print('Server Up ')
s.listen(1)

root=tk.Tk()
root.geometry("400x200")
root.title("Chat App Server Side")
root.configure(bg="black")

c,addr=s.accept()

print("Connected to: ",addr)

def send():
    global msg
    msg=x.get()
    c.send(bytes(msg,'utf-8'))

def income():
    x=c.recv(1024).decode()
    l.configure(text=x)

x=tk.StringVar()

l=tk.Label(root,text='')
l.place(x=40,y=55)

e=tk.Entry(root,textvariable=x)
e.place(x=4,y=105,height=30,width=320)

b=tk.Button(root,text="Send",command=send,bg="red",fg="white")
b.place(x=160,y=140,height=40,width=80)

b2=tk.Button(root,text="Refresh",command=income,bg="red",fg="white")
b2.place(x=260,y=140,height=20,width=40)

root.mainloop()
