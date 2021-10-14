# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 19:16:02 2020

@author: 莊紀勳
"""

"""
import
"""

import tkinter as tk
import random  as rd
from tkinter import messagebox as mb

"""
def
"""

def count():
    global num
    global MIN
    global MAX
    global tim
    var_gus=gus.get()
    
    if MIN<var_gus<MAX:
        tim+=1
        
        if var_gus<num:
            MIN=var_gus
            lbl_tim['text']='{0}'.format(tim)
            lbl_rag['text']='請猜介於{0}到{1}的整數'.format(MIN,MAX)
            lbl_gus['text']='您猜測:{0},太小了'.format(var_gus)
            
        elif var_gus>num:
            MAX=var_gus
            lbl_tim['text']='{0}'.format(tim)
            lbl_rag['text']='請猜介於{0}到{1}的整數'.format(MIN,MAX)
            lbl_gus['text']='您猜測:{0},太大了'.format(var_gus)
            
        else:
            lbl_tim['text']='{0}'.format(tim)
            lbl_gus['text']='你贏了。終極密碼:{0}'.format(num)
            mgb_rst= mb.askokcancel('你贏了 ','請問是否再玩一次？',icon = 'info')
            
            if mgb_rst==True:
                    num=rd.randint(2,99)
                    MIN=1
                    MAX=100
                    tim=0
                    lbl_rag['text']='請猜介於0到100的整數'
                    lbl_gus['text']='重新開始!'
                    lbl_tim['text']='0'
                
    else:
        mb.showwarning('請猜介於範圍內的整數','請猜介於範圍內的整數')
    lbl_tim['text']='{0}'.format(tim)
    
def restart():
    
    global num
    global MIN
    global MAX
    global tim
    num=rd.randint(2,99)
    MIN=1
    MAX=100
    tim=0
    lbl_rag['text']='請猜介於0到100的整數'
    lbl_gus['text']='重新開始!'
    lbl_tim['text']='0'

def destroy():
    win.destroy()

"""
win setting   
"""

win=tk.Tk()
win.title('終極密碼')
win.geometry('320x180')

"""
var setting
"""
gus=tk.IntVar()
num=rd.randint(2,99)
MIN=1
MAX=100
tim=0

"""
item
"""
lbl_tt1=tk.Label(win,text='終極密碼:',padx=10,pady=8)
lbl_tt2=tk.Label(win,text='猜測次數:',padx=10,pady=8)
lbl_tt3=tk.Label(win,text='請猜密碼:',padx=10,pady=8)
lbl_tt4=tk.Label(win,text='猜測結果:',padx=10,pady=8)
lbl_rag=tk.Label(win,text='請猜介於0到100的整數')
lbl_tim=tk.Label(win,text='0')
lbl_gus=tk.Label(win,text='')

but_gus=tk.Button(win,text='猜!',command=count)
but_end=tk.Button(win,text='結束遊戲',command=destroy)
but_rst=tk.Button(win,text='重新開始',command=restart)

ety_gus=tk.Entry(win,text='n=',textvariable=gus)

"""
location
"""
lbl_tt1.grid(row=0,column=0)
lbl_rag.grid(row=0,column=1)

lbl_tt2.grid(row=1,column=0)
lbl_tim.grid(row=1,column=1)

lbl_tt3.grid(row=2,column=0)
ety_gus.grid(row=2,column=1)
but_gus.grid(row=2,column=2)

lbl_tt4.grid(row=3,column=0)
lbl_gus.grid(row=3,column=1)

but_rst.grid(row=4,column=0)
but_end.grid(row=4,column=1)




"""
loop
"""

win.mainloop()