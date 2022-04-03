import urllib.request
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import json


root = Tk()
root.title('Конвертер валют')
root.geometry('400x300+400+250')
root.resizable(False, False)

start_sum = 1000


#FUNC
try:
    html= urllib.request.urlopen('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')
    data = html.read()
    JSON_object = json.loads(data)
except:
    messagebox.showerror('Ошибка при выполнении')

def excange():
    entry_r.delete(1 , END)
    entry_b.delete(1 , END)
    entry_u.delete(1 , END)
    try:
        entry_r.insert(0 ,round(float(entry_uah.get()) / float(JSON_object[0]['sale']), 2))
        entry_u.insert(0, round(float(entry_uah.get()) / float(JSON_object[1]['sale']), 2))
        entry_b.insert(0, round(float(entry_uah.get()) / float(JSON_object[0]['sale']) / float(JSON_object[2]['sale']), 2))
    except:
        messagebox.showerror('Warning ', 'Проверьте введенную сумму')



# HEADER FRAME
header = Frame(root)
header.pack(fill=X)
header.grid_columnconfigure(0, weight=1)
header.grid_columnconfigure(1, weight=1)
header.grid_columnconfigure(2, weight=1)

start = Label(header, text='Валюта', font='Arial 12 bold', bg='#808080').grid(row=0, column=0, sticky=EW)
start = Label(header, text='Покупка', font='Arial 12 bold', bg='#808080').grid(row=0, column=1, sticky=EW)
start = Label(header, text='Продажа', font='Arial 12 bold', bg='#808080').grid(row=0, column=2, sticky=EW)

# Label
usd_l = Label(header, text='USD', bg='#A9A9A9', font='Arial 10 ').grid(row=1, column=0, sticky=EW)
eur_l = Label(header, text='EUR', bg='#C0C0C0', font='Arial 10 ').grid(row=2, column=0, sticky=EW)
rur_l = Label(header, text='BTC $', bg='#D3D3D3', font='Arial 10 ').grid(row=3, column=0, sticky=EW)

# Buy
usd_c = Label(header, text=round(float(JSON_object[0]['buy']),2), bg='#A9A9A9', font='Arial 10 ').grid(row=1, column=1, sticky=EW)
eur_c = Label(header, text=round(float(JSON_object[1]['buy']),2), bg='#C0C0C0', font='Arial 10 ').grid(row=2, column=1, sticky=EW)
rur_c = Label(header, text=round(float(JSON_object[2]['buy']),), bg='#D3D3D3', font='Arial 10 ').grid(row=3, column=1, sticky=EW)

# Sale

usd_s = Label(header, text=round(float(JSON_object[0]['sale']),2), bg='#A9A9A9', font='Arial 10 ').grid(row=1, column=2, sticky=EW)
eur_s = Label(header, text=round(float(JSON_object[1]['sale']),2), bg='#C0C0C0', font='Arial 10 ').grid(row=2, column=2, sticky=EW)
btc_s = Label(header, text=round(float(JSON_object[2]['sale']),), bg='#D3D3D3', font='Arial 10 ').grid(row=3, column=2, sticky=EW)

# Calc Frame
calc_frame = Frame(root, bg="#778899")
calc_frame.pack(expand=1, fill=BOTH)
calc_frame.grid_columnconfigure(1, weight=1)

price_uah = Label(calc_frame, text='Гривна :', font='Arial 10 bold', bg='#778899')
price_uah.grid(row=0, column=0, pady=10, padx=10)

entry_uah = ttk.Entry(calc_frame, justify=CENTER)
entry_uah.insert(0 , start_sum )
entry_uah.grid(row=0, columnspan=1, column=1, pady=5, sticky=EW, padx=10)

button = ttk.Button(calc_frame, text='Обменять' , command=excange)
button.grid(row=1, columnspan=1, column=1, sticky=EW, padx=10)

# Final Frame
final_frame = Frame(root, bg='#808080')
final_frame.pack(expand=1, fill=BOTH)
final_frame.grid_columnconfigure(1, weight=1)
final_frame.grid_columnconfigure(1, weight=2)
final_frame.grid_columnconfigure(1, weight=3)

usd_f = Label(final_frame, text='USD:', font='Arial 10 ', bg='#808080').grid(row=0, column=0, padx=10)
eur_f = Label(final_frame, text='EUR:', font='Arial 10 ', bg='#808080').grid(row=1, column=0, padx=10)
rur_f = Label(final_frame, text='BTC:', font='Arial 10 ', bg='#808080').grid(row=2, column=0, padx=10)

entry_r = ttk.Entry(final_frame, justify=CENTER)
entry_r.insert(0 , 1000)
entry_r.grid(row=0, columnspan=1, column=1, pady=5, sticky=EW, padx=30)
entry_u = ttk.Entry(final_frame, justify=CENTER)
entry_u.insert(0 , 2000)
entry_u.grid(row=1, columnspan=1, column=1, pady=5, sticky=EW, padx=30)
entry_b = ttk.Entry(final_frame, justify=CENTER)
entry_b.insert(0 , 2500)
entry_b.grid(row=2, columnspan=1, column=1, pady=5, sticky=EW, padx=30)

root.mainloop()
