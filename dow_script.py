import os
import threading
import tkinter as tk
from tkinter import ttk

#https://yogapan.github.io/2017/08/16/Youtube-dl%E6%BF%83%E7%B8%AE%E6%95%99%E5%AD%B8%E7%AD%86%E8%A8%98/

url_list=[]
def thread_it(func,*args):
		#mutlithreading
		print('Number of threads:',end='')
		print(threading.active_count())
		
		added_t1 = threading.Thread(target=func,args=args)
		added_t1.start()

def add_node(url):
    url_list.append(url)
    e1_var.set('')

    c1['value']=url_list
    c1.grid(column=0,columnspan=3,row=2)

def download():
    for url in url_list:
        #os.system("youtube-dl -x --audio-format mp3 --embed-thumbnail  --metadata-from-title\"%(aaaa)s - %(bbbb)s\""+url)
        os.system("youtube-dl -x --audio-format mp3 --embed-thumbnail --add-metadata "+url)
        print('done!!') 


root=tk.Tk()
root.title('Welcome to Youtube Downloader')
root.geometry('400x100')
tk.Label(root,text="請貼上網址").grid(column=0,row=0)

e1_var=tk.StringVar()
e1_var.set('')
e1=tk.Entry(root,width=50,textvariable=e1_var)
e1.grid(column=0,columnspan=3,row=1)

tk.Button(root,text="Add",command=lambda :add_node(e1.get())).grid(column=3,row=1)

c1_var=tk.StringVar()
c1=ttk.Combobox(root,width=50,textvariable=c1_var,state='readonly')
c1['value']=url_list
c1.grid(column=0,columnspan=3,row=2)

tk.Button(root,text="Start Download",command=lambda :thread_it(download)).grid(column=1,row=3)



root.mainloop()