from tkinter import *
import math,random,os
from tkinter import messagebox
class Bill:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1000x700+0+0")
        self.root.title("Billing")
        title=Label(self.root,text="KFC",bd=12,relief=GROOVE,bg="yellow",fg="red",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        self.piz=IntVar()
        self.bur=IntVar()
        self.fre=IntVar()
        self.chi=IntVar()
        self.pep=IntVar()
        self.tot=StringVar()
        self.tax=StringVar()
        self.total=StringVar()
        self.cn=StringVar()
        self.cph=StringVar()
        self.biln=StringVar()
        x=random.randint(1000,9999)
        self.biln.set(str(x))
        self.search=StringVar()
        f1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",fg="black",font=("times new roman",30,"bold"),bg="yellow")
        f1.place(x=0,y=70,relwidth=5)

        cname=Label(f1,text="CustomerName",fg="black",relief=GROOVE,font=("times new roman",25,"bold"),bg="violet").grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(f1,width=10,textvariable=self.cn,fg="black",font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)
        cph=Label(f1,text="Customer Phno",fg="black",relief=GROOVE,font=("times new roman",25,"bold"),bg="violet").grid(row=0,column=2,padx=20,pady=5)
        cph_txt=Entry(f1,width=10,textvariable=self.cph,fg="black",font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=5)
        cbill=Label(f1,text="Bill No",fg="black",relief=GROOVE,font=("times new roman",25,"bold"),bg="violet").grid(row=0,column=4,padx=20,pady=5)
        cbill_txt=Entry(f1,width=10,textvariable=self.search,fg="black",font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,padx=10,pady=5)
        billbtn=Button(f1,text="Search",command=self.find,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=10)
        f2=LabelFrame(self.root,bd=10,relief=GROOVE,text="MENU",fg="black",font=("times new roman",30,"bold"),bg="yellow")
        f2.place(x=0,y=190,width=500,height=410)
        food=Label(f2,text="Pizza     \t\t-300/-",font=("times new roman",30,"bold"),bg="yellow",fg="red").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        food1=Label(f2,text="Burger  \t\t-250/-",font=("times new roman",30,"bold"),bg="yellow",fg="red").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        food2=Label(f2,text="French Fries\t-150/-",font=("times new roman",30,"bold"),bg="yellow",fg="red").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        food3=Label(f2,text="Chicken Wings(4pcs)-600/-",font=("times new roman",30,"bold"),bg="yellow",fg="red").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        food5=Label(f2,text="Pepsi  \t\t-90/-",font=("times new roman",30,"bold"),bg="yellow",fg="red").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        f3=LabelFrame(self.root,bd=10,relief=GROOVE,text="ORDER",fg="black",font=("times new roman",30,"bold"),bg="yellow")
        f3.place(x=500,y=190,width=420,height=410)
        food=Label(f3,text="Pizza",font=("times new roman",30,"bold"),bg="yellow",fg="red").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        food_txt=Entry(f3,width=7,textvariable=self.piz,fg="black",font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)
        food1=Label(f3,text="Burger",font=("times new roman",30,"bold"),bg="yellow",fg="red").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        food1_txt=Entry(f3,width=7,textvariable=self.bur,fg="black",font="arial 15",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=5)
        food2=Label(f3,text="French Fries",font=("times new roman",30,"bold"),bg="yellow",fg="red").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        food2_txt=Entry(f3,width=7,textvariable=self.fre,fg="black",font="arial 15",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=5)
        food3=Label(f3,text="Chicken Wings",font=("times new roman",30,"bold"),bg="yellow",fg="red").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        food3_txt=Entry(f3,width=7,textvariable=self.chi,fg="black",font="arial 15",bd=7,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=5)
        food4=Label(f3,text="Pepsi",font=("times new roman",30,"bold"),bg="yellow",fg="red").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        food4_txt=Entry(f3,width=7,textvariable=self.pep,fg="black",font="arial 15",bd=7,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=5)
        f4=LabelFrame(self.root,bd=10,relief=GROOVE)
        f4.place(x=920,y=190,width=360,height=410)
        label=Label(f4,bd=10,text="BILL",relief=GROOVE,font="arial 15 bold").pack(fill=X)
        scrol=Scrollbar(f4,orient=VERTICAL)
        self.txtarea=Text(f4,yscrollcommand=scrol.set)
        scrol.pack(side=RIGHT,fill=Y)
        scrol.config(command=self.txtarea.yview)
        self.txtarea.pack()
        f5=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",fg="black",font=("times new roman",20,"bold"),bg="yellow")
        f5.place(x=0,y=600,relwidth=1,height=140)
        m1=Label(f5,text="Total",bg="yellow",font=("times new roman",30,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(f5,width=10,textvariable=self.tot,font="arial 20 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=20,pady=1)
        c1=Label(f5,text="Tax",bg="yellow",font=("times new roman",30,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        c1_txt=Entry(f5,width=10,textvariable=self.tax,font="arial 20 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=20,pady=1)
        btnf=Frame(f5,bd=7,relief=GROOVE)
        btnf.place(x=660,width=585,height=105)
        totalbtn=Button(btnf,command=self.tota,text="Total",bg="yellow",fg="black",pady=15,width=9,bd=7,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5)
        genbtn=Button(btnf,command=self.billare,text="Generate Bill",bg="yellow",fg="black",pady=15,width=11,bd=7,font="arial 15 bold").grid(row=0,column=2,padx=5,pady=5)
        clrbtn=Button(btnf,text="Clear",command=self.clear,bg="yellow",fg="black",pady=15,width=9,bd=7,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=5)
        extbtn=Button(btnf,text="Exit",command=self.exit,bg="yellow",fg="black",pady=15,width=9,bd=7,font="arial 15 bold").grid(row=0,column=4,padx=5,pady=5)
        self.welcome_bill()
    def tota(self):
        self.p=self.piz.get()*300
        self.b=self.bur.get()*250
        self.f=self.fre.get()*150
        self.c=self.chi.get()*600
        self.pe=self.pep.get()*90
        self.grand=float(
                        (self.p)+
                        (self.b)+
                        (self.f)+
                        (self.c)+
                        (self.pe)
                        )
        self.tot.set("Rs. "+str(self.grand))
        self.grandy=round((self.grand*0.02),2)
        self.tax.set("Rs. "+str(self.grandy))
        self.total_b=float(self.grand + self.grandy)
        self.total.set("Rs. "+str(self.total_b))
    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\t  Mini KFC bill\n")
        self.txtarea.insert(END,f"\n Bill Number :{self.biln.get()}")
        self.txtarea.insert(END,f"\n Customer Name :{self.cn.get()}")
        self.txtarea.insert(END,f"\n Phone Number :{self.cph.get()}")
        self.txtarea.insert(END,f"\n=======================================")
        self.txtarea.insert(END,f"\n Products\t\tQty\t\tPrice")
        self.txtarea.insert(END,f"\n=======================================")
    def billare(self):
        if self.cn.get()=="" or self.cph.get()=="":
            messagebox.showerror("Error","Customer details are must")
        else:
            self.welcome_bill()
            if self.piz.get()!=0:
                self.txtarea.insert(END,f"\n Pizza\t\t{self.piz.get()}\t\t{self.p}")
            if self.bur.get()!=0:
                self.txtarea.insert(END,f"\n Burger\t\t{self.bur.get()}\t\t{self.b}")
            if self.fre.get()!=0:
                self.txtarea.insert(END,f"\n French Fries\t\t{self.fre.get()}\t\t{self.f}")
            if self.chi.get()!=0:
                self.txtarea.insert(END,f"\n Chicken Wings\t\t{self.chi.get()}\t\t{self.c}")
            if self.pep.get()!=0:
                self.txtarea.insert(END,f"\n Pepsi\t\t{self.pep.get()}\t\t{self.pe}")
            self.txtarea.insert(END,f"\n---------------------------------------")
            self.txtarea.insert(END,f"\n Tax\t\t\t  {self.tax.get()}")
            self.txtarea.insert(END,f"\n Bill\t\t\t {self.tot.get()}")
            self.txtarea.insert(END,f"\n Total Bill\t\t\t {self.total.get()}")
            self.txtarea.insert(END,f"\n---------------------------------------")
            self.save_bill()
    def save_bill(self):
        op=messagebox.askyesno("Save Bill"," Do you want to save the bill?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            h1=open("bill/"+str(self.biln.get())+".txt","w")
            h1.write(self.bill_data)
            h1.close()
            messagebox.showinfo("Saved",f"Bill no: {self.biln.get()} Saved Successfully")
        else:
            return
    def find(self):
        present="no"
        for i in os.listdir("bill/"):
            if i.split('.')[0]==self.search.get():
                h1=open(f"bill/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in h1:
                    self.txtarea.insert(END,d)
                h1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill No")
    def clear(self):
        op=messagebox.askyesno("Exit","Do you really want to clear?")
        if op>0:
            self.piz.set(0)
            self.bur.set(0)
            self.fre.set(0)
            self.chi.set(0)
            self.pep.set(0)
            self.tot.set("")
            self.tax.set("")
            self.cn.set("")
            self.cph.set("")
            self.biln.set("")
            x=random.randint(1000,9999)
            self.biln.set(str(x))
            self.search.set("")
            self.welcome_bill()
    def exit(self):
        op=messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.root.destroy()
root=Tk()
o=Bill(root)
root.mainloop()
