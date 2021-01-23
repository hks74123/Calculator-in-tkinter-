from tkinter import *#first we need to import tkinter

def comm(event):#here we define function
    global scvalue
    tct=event.widget.cget("text")#as here we have used .get() for getting text of button
    if tct=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())#to calculate as eval fn is used to evaluate string
        else:
            value=eval(ib.get())

        scvalue.set(value)#to assign value to string variable
        ib.update()#to update input box

    elif tct=="C":
        scvalue.set("")#after clicking button c clear all input
        ib.update()
    else:
        scvalue.set(scvalue.get()+ tct)#to get text of button
        ib.update()

#as we have done now let's run our code
#after that take a screen
screen= Tk()
screen.title('My Calculator')
screen.geometry('312x324')
screen.resizable(0,0)#use resizable to avoid resizing
#scvalue we have taken an string variable
scvalue=StringVar("")
#now first of all here we are going to take 6 frames
input_frame=Frame(screen,width=312,height=54)
input_frame.pack(side=TOP)



btm_frame1=Frame(screen,width=312,height=15,bg='grey')
btm_frame1.pack(side=TOP)

botm_frame=Frame(screen,width=312,height=5,bg='grey')
botm_frame.pack(side=TOP)


btm_frame2=Frame(screen,width=312,height=5)
btm_frame2.pack(side=TOP)

btm_frame3=Frame(screen,width=312,height=5)
btm_frame3.pack(side=TOP)

btm_frame4=Frame(screen,width=312,height=5)
btm_frame4.pack(side=TOP)
#here we have taken an input box in topmost frame
ib=Entry(input_frame,font=("Arial",33),textvariable=scvalue,width=300)
ib.pack()
#we have created a c button to clear all input
c=Button(btm_frame1,text="C",fg='black',bg='grey',cursor='hand2',width=30,height=3)
c.bind("<Button-1>",comm)
c.pack(side=LEFT)
#here is the division button in first frame after input box
div=Button(btm_frame1,text="/",fg='black',bg='grey',cursor='hand2',width=12,height=3)
div.bind("<Button-1>",comm)
div.pack(side=LEFT)
#now here are four buttons in third frame
b1=Button(botm_frame,text="1",bg='grey',fg='black',cursor='hand2',width=10,height=3)
b1.bind("<Button-1>",comm)
b1.pack(side=LEFT)

b2=Button(botm_frame,text="2",fg='black',bg='grey',cursor='hand2',width=10,height=3)
b2.bind("<Button-1>",comm)
b2.pack(side=LEFT)

b3=Button(botm_frame,text="3",fg='black',bg='grey',cursor='hand2',width=10,height=3)
b3.bind("<Button-1>",comm)
b3.pack(side=LEFT)

mi=Button(botm_frame,text="-",fg='black',bg='grey',cursor='hand2',width=10,height=3)
mi.bind("<Button-1>",comm)
mi.pack(side=LEFT)

#here are 4 more buttons
b4=Button(btm_frame2,text="4",fg='black',bg='grey',cursor='hand2',width=10,height=3)
b4.bind("<Button-1>",comm)
b4.pack(side=LEFT)

b5=Button(btm_frame2,text="5",fg='black',bg='grey',cursor='hand2',width=10,height=3)
b5.bind("<Button-1>",comm)
b5.pack(side=LEFT)

b6=Button(btm_frame2,text="6",fg='black',bg='grey',cursor='hand2',width=10,height=3)
b6.bind("<Button-1>",comm)
b6.pack(side=LEFT)

mu=Button(btm_frame2,text="*",fg='black',bg='grey',cursor='hand2',width=10,height=3)
mu.bind("<Button-1>",comm)
mu.pack(side=LEFT)


#next four
b7=Button(btm_frame3,text="7",fg='black',bg='grey',cursor='hand2',width=10,height=3)
b7.bind("<Button-1>",comm)
b7.pack(side=LEFT)

b8=Button(btm_frame3,text="8",fg='black',bg='grey',cursor='hand2',width=10,height=3)
b8.bind("<Button-1>",comm)
b8.pack(side=LEFT)

b9=Button(btm_frame3,text="9",fg='black',bg='grey',cursor='hand2',width=10,height=3)
b9.bind("<Button-1>",comm)
b9.pack(side=LEFT)

ad=Button(btm_frame3,text="+",fg='black',bg='grey',cursor='hand2',width=10,height=3)
ad.bind("<Button-1>",comm)
ad.pack(side=LEFT)


#last three buttons
b0=Button(btm_frame4,text="0",fg='black',bg='grey',cursor='hand2',width=21,height=3)
b0.bind("<Button-1>",comm)
b0.pack(side=LEFT)

dot=Button(btm_frame4,text=".",fg='black',bg='grey',cursor='hand2',width=10,height=3)
dot.bind("<Button-1>",comm)
dot.pack(side=LEFT)

eq=Button(btm_frame4,text="=",fg='black',bg='grey',cursor='hand2',width=10,height=3)
eq.bind("<Button-1>",comm)
eq.pack(side=LEFT)

#now as we have created all the buttons lets make an function to update in our input box
screen.mainloop()
