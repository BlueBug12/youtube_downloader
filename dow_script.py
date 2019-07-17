# -*- coding: utf-8 -*-
import os
import threading
import tkinter as tk
from tkinter import ttk
from bs4 import BeautifulSoup
import requests

url_list=[]
name_list=[]
def thread_it(func,*args):
		#mutlithreading
		print('Number of threads:',end='')
		print(threading.active_count())
		
		added_t1 = threading.Thread(target=func,args=args)
		added_t1.start()

def add_node(url):
	request=requests.get(url)
	context = request.content
	soup=BeautifulSoup(context,"html.parser")
	video_name = soup.select('h1.watch-title-container')[0].get_text();
	video_name = video_name.replace('\n','')
	video_name = video_name.replace(' ','')
	name_list.append(video_name)
	url_list.append(url)
	e1_var.set('')
	c1['value']=name_list
	c1.grid(padx=10,column=1,columnspan=3,row=2)

def delete_node(index):
	del url_list[index]
	del name_list[index]
	c1_var.set("                                       (如需刪除再點選)")
	c1['value']=name_list
	c1.grid(ipadx=10,column=1,columnspan=3,row=2)
	

def download(destination):
	for url in url_list:
		destination = "\""+destination+"\""
		os.system("youtube-dl --output /%(title)s.%(ext)s -x --audio-format mp3 "+url)
		print('done!!') 
	name_list=[]
	global url_list
	url_list=[]
	c1_var.set("                                       (如需刪除再點選)")
	c1['value']=[]
	c1.grid(ipadx=10,column=1,columnspan=3,row=2)


root=tk.Tk()
root.title('Welcome to Youtube Downloader')
root.geometry('650x200')
tk.Label(root,text="請貼上網址: ").grid(column=0,row=1)
tk.Label(root,text="下載列表:   ").grid(column=0,row=2)

e1_var=tk.StringVar()
e1_var.set('')
e1=tk.Entry(root,width=50,textvariable=e1_var)
e1.grid(ipadx=10,column=1,columnspan=3,row=1)

tk.Button(root,text="加入",command=lambda :add_node(e1.get())).grid(column=4,row=1)

c1_var=tk.StringVar()
c1_var.set("                                       (如需刪除再點選)")
c1=ttk.Combobox(root,width=50,textvariable=c1_var,state='readonly')
c1['value']=name_list
c1.grid(padx=10,column=1,columnspan=3,row=2)

tk.Button(root,text="刪除",command=lambda :delete_node(c1.current())).grid(column=4,row=2)

tk.Button(root,text="開始下載",command=lambda :thread_it(download("C:/Users/User/Desktop"))).grid(column=2,row=3)

root.mainloop()