import tkinter as tk
import pygame
root = tk.Tk()
root.geometry("700x700")
root.title("Soundboard")
root.config(bg="black")
pygame.mixer.init()
def play(i):    
    pygame.mixer.music.load("source/"+str(i)+".wav")
    pygame.mixer.music.play()

b1=tk.Button(root,bg="red",font = ("Comic Sans MS",20,"bold"),text="Work it",bd=3,command=lambda : play(1))
b1.place(relwidth=0.35,relheight=0.06,relx=0.25,rely=0.2,anchor="center")

b2=tk.Button(root,bg="red",font = ("Comic Sans MS",20,"bold"),text="Make it",bd=3,command=lambda : play(2))
b2.place(relwidth=0.35,relheight=0.06,relx=0.75,rely=0.2,anchor="center")

b3=tk.Button(root,bg="orange",font = ("Comic Sans MS",20,"bold"),text="Do it",bd=3,command=lambda : play(3))
b3.place(relwidth=0.35,relheight=0.06,relx=0.25,rely=0.3,anchor="center")

b4=tk.Button(root,bg="orange",font = ("Comic Sans MS",20,"bold"),text="Makes us",bd=3,command=lambda : play(4))
b4.place(relwidth=0.35,relheight=0.06,relx=0.75,rely=0.3,anchor="center")

b5=tk.Button(root,bg="yellow",font = ("Comic Sans MS",20,"bold"),text="Harder",bd=3,command=lambda : play(5))
b5.place(relwidth=0.35,relheight=0.06,relx=0.25,rely=0.4,anchor="center")

b6=tk.Button(root,bg="yellow",font = ("Comic Sans MS",20,"bold"),text="Better",bd=3,command=lambda : play(6))
b6.place(relwidth=0.35,relheight=0.06,relx=0.75,rely=0.4,anchor="center")

b7=tk.Button(root,bg="green",font = ("Comic Sans MS",20,"bold"),text="Faster",bd=3,command=lambda : play(7))
b7.place(relwidth=0.35,relheight=0.06,relx=0.25,rely=0.5,anchor="center")

b8=tk.Button(root,bg="green",font = ("Comic Sans MS",20,"bold"),text="Stronger",bd=3,command=lambda : play(8))
b8.place(relwidth=0.35,relheight=0.06,relx=0.75,rely=0.5,anchor="center")

b9=tk.Button(root,bg="blue",font = ("Comic Sans MS",20,"bold"),text="More than",bd=3,command=lambda : play(9))
b9.place(relwidth=0.35,relheight=0.06,relx=0.25,rely=0.6,anchor="center")

b10=tk.Button(root,bg="blue",font = ("Comic Sans MS",20,"bold"),text="Hour",bd=3,command=lambda : play(10))
b10.place(relwidth=0.35,relheight=0.06,relx=0.75,rely=0.6,anchor="center")

b11=tk.Button(root,bg="indigo",font = ("Comic Sans MS",20,"bold"),text="Our",bd=3,command=lambda : play(11))
b11.place(relwidth=0.35,relheight=0.06,relx=0.25,rely=0.7,anchor="center")

b12=tk.Button(root,bg="indigo",font = ("Comic Sans MS",20,"bold"),text="Never",bd=3,command=lambda : play(12))
b12.place(relwidth=0.35,relheight=0.06,relx=0.75,rely=0.7,anchor="center")

b13=tk.Button(root,bg="violet",font = ("Comic Sans MS",20,"bold"),text="Ever",bd=3,command=lambda : play(13))
b13.place(relwidth=0.35,relheight=0.06,relx=0.25,rely=0.8,anchor="center")

b14=tk.Button(root,bg="violet",font = ("Comic Sans MS",20,"bold"),text="After",bd=3,command=lambda : play(14))
b14.place(relwidth=0.35,relheight=0.06,relx=0.75,rely=0.8,anchor="center")

b15=tk.Button(root,bg="red",font = ("Comic Sans MS",20,"bold"),text="Work is",bd=3,command=lambda : play(15))
b15.place(relwidth=0.35,relheight=0.06,relx=0.25,rely=0.9,anchor="center")

b16=tk.Button(root,bg="red",font = ("Comic Sans MS",20,"bold"),text="Over",bd=3,command=lambda : play(16))
b16.place(relwidth=0.35,relheight=0.06,relx=0.75,rely=0.9,anchor="center")

root.mainloop()
