from tkinter import *
from tkinter import messagebox
import tkinter.font as font
from PIL import Image, ImageTk

class tic_tac_toe:
    def __init__(self,rt):
        self.root=rt
        
        self.window()
        self.buttons()
        
        self.root.mainloop()
        
        
    def window(self):
        
        self.root.title("TIC TAC TOE")
        self.root.geometry("600x600")
        #self.root.wm_iconbitmap("XOic.ico")
        
        #1st Frame
        self.frame=Frame(self.root,bg="#0accc2")
        self.frame.pack(fill=BOTH,expand=1)
        
        #Background Image
        """load = Image.open("XO.jpg")
        s=load.resize((600, 600))
        render= ImageTk.PhotoImage(s)
        img =Label(self.frame, image=render)
        img.image = render
        img.place(x=0, y=0)"""
        
        
    def buttons(self):
        
        myFont = font.Font(family='Helvetica', weight='bold')
        
        self.button1=Button(self.frame,text="START",padx=25,pady=8,fg="black",bg="#ccc610",activebackground="#7be000",font=myFont,command=self.board)
        self.button1.place(x=260, y=150)
        
        self.button2=Button(self.frame,text="HELP",padx=30,pady=8,fg="black",bg="#ccc610",activebackground="#7be000",font=myFont,command=self.Help)
        self.button2.place(x=260, y=230)
        
        self.button3=Button(self.frame,text="EXIT",padx=34,pady=8,fg="black",bg="#ccc610",activebackground="#7be000",font=myFont,command=self.Exit)
        self.button3.place(x=260, y=310)
        
                
    #Help Option   
    def Help(self):
        messagebox.showinfo("HOW TO PLAY", "1. The game is played on a grid that's 3 squares by 3 squares.\n\n2. You are X, your friend is O. Players take turns putting their marks in empty squares.\n\n3. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.\n\n4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.")
      
        
    #To Exit    
    def Exit(self):
        if(messagebox.askyesno('VERIFY', 'DO YOU REALLY WANT TO QUIT?')):
            self.root.destroy()
        
           
    def board(self):
        self.count=1
        self.line1=3
        self.line2=3
        self.line3=""
        self.ch=[]
        self.row,self.col=3,3
        self.arr=[[0 for i in range(self.col)] for j in range(self.row)]
        
        
        self.font=font.Font(family='Helvetica', weight='bold',size=45)
        self.font1=font.Font(family='Helvetica', weight='bold',size=15)
        self.c=Canvas(self.frame)
        
        self.lbl1=Label(self.c,text="PLAYER_1 >>>'X'",font=self.font1,fg="red")
        self.lbl1.place(x=50, y=20)
        
        self.lbl2=Label(self.c,text="PLAYER_2 >>>'O'",font=self.font1,fg="red")
        self.lbl2.place(x=380, y=20)
        
        #1st vertical line
        self.c.create_line(230,100,230,400,width=3)
        
        #2nd vertical line
        self.c.create_line(370,100,370,400,width=3)
        
        #1st horizontal line
        self.c.create_line(100,200,500,200,width=3)
        
        #2nd horizontal line
        self.c.create_line(100,300,500,300,width=3)
        
        self.c.pack(fill=BOTH,expand=1)
        self.c.bind("<Button-1>",self.action)
        
        
    def action(self,var):
        self.x1, self.y1=var.x, var.y
        self.xa=0
        self.ya=0
        if(self.count%2!=0):
            self.char="X"
        else:
            self.char="O"
        
    
        if(self.x1>=100 and self.x1<=230 and self.y1>=100 and self.y1<=200):
            if(1 not in self.ch):
                self.ch.append(1)
                self.xa=140
                self.ya=120
                self.arr[0][0]=self.char
                self.a, self.b=0, 0
                
        elif(self.x1>=230 and self.x1<=370 and self.y1>=100 and self.y1<=200):
            if(2 not in self.ch):
                self.ch.append(2)
                self.xa=275
                self.ya=120
                self.arr[0][1]=self.char
                self.a, self.b=0, 1
            
        elif(self.x1>=370 and self.x1<=500 and self.y1>=100 and self.y1<=200):
            if(3 not in self.ch):
                self.ch.append(3)
                self.xa=410
                self.ya=120
                self.arr[0][2]=self.char
                self.a, self.b=0, 2
                
        elif(self.x1>=100 and self.x1<=230 and self.y1>=200 and self.y1<=300):
            if(4 not in self.ch):
                self.ch.append(4)
                self.xa=140
                self.ya=215
                self.arr[1][0]=self.char
                self.a, self.b=1, 0
                
        elif(self.x1>=230 and self.x1<=370 and self.y1>=200 and self.y1<=300):
            if(5 not in self.ch):
                self.ch.append(5)
                self.xa=275
                self.ya=215
                self.arr[1][1]=self.char
                self.a, self.b=1, 1
                
        elif(self.x1>=370 and self.x1<=500 and self.y1>=200 and self.y1<=300):
            if(6 not in self.ch):
                self.ch.append(6)
                self.xa=410
                self.ya=215
                self.arr[1][2]=self.char
                self.a, self.b=1, 2
                
        elif(self.x1>=100 and self.x1<=230 and self.y1>=300 and self.y1<=400):
            if(7 not in self.ch):
                self.ch.append(7)
                self.xa=140
                self.ya=315
                self.arr[2][0]=self.char
                self.a, self.b=2, 0
                
        elif(self.x1>=230 and self.x1<=370 and self.y1>=300 and self.y1<=400):
            if(8 not in self.ch):
                self.ch.append(8)
                self.xa=275
                self.ya=315
                self.arr[2][1]=self.char
                self.a, self.b=2, 1
                
        elif(self.x1>=370 and self.x1<=500 and self.y1>=300 and self.y1<=400):
            if(9 not in self.ch):
                self.ch.append(9)
                self.xa=410
                self.ya=315
                self.arr[2][2]=self.char
                self.a, self.b=2, 2
                
        else:
            pass
            
            
            
        if(self.xa>0 and self.ya>0):
            self.count+=1

            #To use undo button only once
            self.no=1
            
            self.l=Label(self.c,text=self.char,font=self.font)
            self.l.place(x=self.xa, y=self.ya) 
        
        for i in range(0,3):
            for j in range(0,3):
                print(self.arr[i][j],end="")
            print()
        print()
            
            
        self.btn=Button(self.c,text="UNDO",width=10,command=self.clear)
        self.btn.place(x=260, y=450)
        
        #TO CHECK THE RESULT
        self.won=0
        self.k=3
        for i in range(0,self.k):
            j=0
            if(self.arr[i][j]==self.arr[i][j+1]==self.arr[i][j+2]==self.char):
                self.won=1
                self.line1=i
                
            elif(self.arr[j][i]==self.arr[j+1][i]==self.arr[j+2][i]==self.char):
                self.won=1
                self.line2=i
                
            else:
                continue
            
        if(self.arr[self.k-3][self.k-3]==self.arr[self.k-2][self.k-2]==self.arr[self.k-1][self.k-1]==self.char):
            self.won=1
            self.line3="a"
        elif(self.arr[self.k-3][self.k-1]==self.arr[self.k-2][self.k-2]==self.arr[self.k-1][self.k-3]==self.char):
            self.won=1
            self.line3="b"
        
        
        
        if(self.won==1):
            if(self.line3=="a"):
                self.c.create_line(100,100,500,400,width=2,fill="#d19e04")
            elif(self.line3=="b"):
                self.c.create_line(500,100,100,400,width=2,fill="#d19e04")
            elif(self.line1==0):
                self.c.create_line(100,150,500,150,width=2,fill="#d19e04")
            elif(self.line1==1):
                self.c.create_line(100,250,500,250,width=2,fill="#d19e04")
            elif(self.line1==2):
                self.c.create_line(100,350,500,350,width=2,fill="#d19e04")
            elif(self.line2==0):
                self.c.create_line(165,80,165,430,width=2,fill="#d19e04")
            elif(self.line2==1):
                self.c.create_line(300,80,300,430,width=2,fill="#d19e04")
            elif(self.line2==2):
                self.c.create_line(435,80,435,430,width=2,fill="#d19e04")
                
                
            if(self.char=="X"):
                self.player="PLAYER 1 HAS WON THE GAME!!!!"
            else:
                self.player="PLAYER 2 HAS WON THE GAME!!!!"
                
            messagebox.showinfo("RESULT",self.player)
            self.c.destroy()
            
        if(self.count==10 and self.won==0):
            messagebox.showinfo("RESULT","THE GAME HAS BEEN TIED")
            self.c.destroy()
    
    def clear(self):
        if(self.no==1):
            self.l.destroy()
            self.count-=1
            self.ch.pop(-1)
            self.arr[self.a][self.b]=0
        self.no=0
        self.btn["state"]=DISABLED
 
           
root=Tk()
t=tic_tac_toe(root)




"""
import Tkinter as tk
root = tk.Tk()

def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))

root.bind('<Motion>', motion)
root.mainloop()
 """
