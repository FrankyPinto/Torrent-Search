import tkinter as tk
import selenium
from selenium import webdriver

/* Selenium library required */

win1=tk.Tk()
win1.title("TORRENT SEARCH")
k=tk.Frame(win1)
k.place(height=2100,width=2100)
ent1=tk.Entry(k)
ent1.place(x=1,y=40,width=195,height=25)
def sub(event):
	fran=ent1.get()
	browser=webdriver.Chrome('D:/chromedriver')     /* Your webdriver location here */
	browser.get("https://1337xto.to/")              /* Site you want to target */
	ele=browser.find_element_by_id('autocomplete')
	ele.send_keys(fran)
	entbut=browser.find_element_by_class_name('i-search')
	entbut.click()
but4=tk.Button(k,bg="red",fg="white",text="Submit")
but4.place(x=40,y=80)
but4.bind("<Button-1>",sub)
but4.bind_all("<Return>",sub)
def quiit():
	win1.destroy()
but5=tk.Button(k,text="Quit",command=quiit)
but5.place(x=100,y=80)
win1.mainloop()

/* Download the webdriver as per your system and browser */
/* If code does not output result you need to check if your browser version and webdriver version match */
