import requests,hashlib,ctypes
from tkinter import *
ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 2 )

def passcheck():
    password=e.get()
    url='https://api.pwnedpasswords.com/range/'
    password=password.encode('utf-8')
    new_pass=hashlib.sha1(password).hexdigest().upper()
    tail=new_pass[5:]
    url=url+new_pass[0:5]
    try:
        res=requests.get(url)
        if(res.status_code!=200 and res.status_code!=400):
            lf['text']="  Connection error!try again later."
            lf['fg']="blue"
            #lf.grid(row=2,column=1)
            return
        feedback=res.text
        hashes=(line.split(':') for line in feedback.splitlines())
        for h,count in hashes:
            if(h==tail):
                temp="Caution!Password has been comprimised {} times".format(count)
                lf['text']=temp
                lf['fg']='red'
                #lf.grid(row=2,column=1)
                return
        lf['text']="Yay! Yo password's secure!"
        lf['fg']='green'
        #lf.grid(row=2,column=1)
    except:
        lf['text']="Oops!There's something wrong with the internet connection!"
        lf['fg']='blue'
        #lf.grid(row=2,column=1)

def getpass():
    b=Button(root,text="Check",command=passcheck)
    b.grid(row=3,column=1)

root=Tk()
root.title("PyPassword")
root.iconbitmap("icon.ico")
l0=Label(root,text="Password Checker".upper())
l1=Label(root,text="Enter password to check:")
lf=Label(root)
l0.grid(row=0,column=1)
l1.grid(row=1,column=0)
lf.grid(row=2,column=1)
e=Entry(root,width=60)
e.grid(row=1,column=1)
getpass()
root.mainloop()

