try:
    import Tkinter
except ImportError: #python2
    import tkinter

import os    

mainwindow = tkinter.Tk()
mainwindow.title("Grid Demo")
mainwindow.geometry("640x480-8-200")
mainwindowPadding = 8
mainwindow['padx'] = mainwindowPadding

label = tkinter.Label(mainwindow, text = "Tkinter Grid Demo")
label.grid(row= 0, column=0, columnspan=3)


mainwindow.columnconfigure(0,weight=100)
mainwindow.columnconfigure(1,weight=1)
mainwindow.columnconfigure(2,weight=1000)
mainwindow.columnconfigure(3,weight=600)
mainwindow.columnconfigure(4,weight=1000)

mainwindow.rowconfigure(0, weight=1)
mainwindow.rowconfigure(1, weight=10)
mainwindow.rowconfigure(2, weight=1)
mainwindow.rowconfigure(3, weight=3)
mainwindow.rowconfigure(4, weight=4)

filelist = tkinter.Listbox(mainwindow)
filelist.grid(row=1, column=0, sticky='nsew', rowspan=2)
filelist.configure(border=2, relief='sunken')

for zone in os.listdir('C:\Windows\System32'):
    filelist.insert(tkinter.END, zone)

listscroll = tkinter.Scrollbar(mainwindow, orient=tkinter.VERTICAL, command=filelist.yview)
listscroll.grid(row=1, column=1, sticky='nsw',rowspan=2)
filelist['yscrollcommand'] = listscroll.set

#frame for the radio buttons 

optionFrame =tkinter.LabelFrame(mainwindow, text="file details")
optionFrame.grid(row=1, column=2,stick='ne')

reValue = tkinter.IntVar()
reValue.set(1)

#radio buttons
radio1 = tkinter.Radiobutton(optionFrame, text='filename', value=1, variable=reValue)
radio2 = tkinter.Radiobutton(optionFrame, text='path', value=2, variable=reValue)
radio3 = tkinter.Radiobutton(optionFrame, text='timestamp', value=3, variable=reValue)
radio1.grid(row=0,column=0,sticky='w')
radio2.grid(row=1,column=0,sticky='w')
radio3.grid(row=2,column=0,sticky='w')

resultlabel = tkinter.Label(mainwindow, text="result")
resultlabel.grid(row=2, column=2, sticky='nw')
result = tkinter.Entry(mainwindow)
result.grid(row=2,column=2,sticky='sw')

#frame for the time spinners
timeframe = tkinter.LabelFrame(mainwindow,text=" time ")
timeframe.grid(row=3,column=0, sticky='new')

#time spinners
hour = tkinter.Spinbox(timeframe,width=2,values=tuple(range(0,24)))
minutes = tkinter.Spinbox(timeframe,width=2, from_=0, to=59)
seconds = tkinter.Spinbox(timeframe,width=2,from_=0,to=59)
hour.grid(row=0,column=0)
tkinter.Label(timeframe,text=':').grid(row=0,column=1)
minutes.grid(row=0,column=2)
tkinter.Label(timeframe,text=':').grid(row=0,column=3)
seconds.grid(row=0,column=4)

timeframe["padx"] = 36

#frame for the date
dateframe = tkinter.LabelFrame(mainwindow, text =" date ")
dateframe.grid(row=4,column=0,sticky='enw')

#date labels
datelabel = tkinter.Label(dateframe, text='day')
monthlabel = tkinter.Label(dateframe, text='month')
yearlabel = tkinter.Label(dateframe, text='year')
datelabel.grid(row=0,column=0,sticky='w')
monthlabel.grid(row=0,column=1,sticky='w')
yearlabel.grid(row=0,column=2,sticky='w')

#date spinners
day = tkinter.Spinbox(dateframe, width=5, from_=1,to=31)
month = tkinter.Spinbox(dateframe, width=5, values=("jan","feb","march","april","may","june","july","aug","sep","oct","nov","dec"))
year = tkinter.Spinbox(dateframe, width=5, from_=2002 ,to=2021)
day.grid(row=1, column=0)
month.grid(row=1, column=1)
year.grid(row=1, column=2)

#buttons
ok = tkinter.Button(mainwindow, text='OK')
cancel = tkinter.Button(mainwindow, text='CANCEL', command=mainwindow.destroy)
ok.grid(row=4,column=3,sticky='e')
cancel.grid(row=4,column=4,sticky='w')


mainwindow.update()
mainwindow.minsize(filelist.winfo_width()+timeframe.winfo_width()+dateframe.winfo_width()+mainwindowPadding,filelist.winfo_height()+result.winfo_height()+timeframe.winfo_height()+label.winfo_height()+dateframe.winfo_height())
mainwindow.maxsize(filelist.winfo_width()+timeframe.winfo_width()+dateframe.winfo_width()+mainwindowPadding+50, 50+filelist.winfo_height()+timeframe.winfo_height() + label.winfo_height()+dateframe.winfo_height())


mainwindow.mainloop()