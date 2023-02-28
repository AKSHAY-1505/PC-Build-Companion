from tkinter import *
from PIL import ImageTk
from GoogleNews import GoogleNews
from tkinter import ttk
import pandas as pd
import webbrowser
from tkinter import messagebox
import sqlite3
import tkinter


bg_colour = "#3d6466"

def openlink(url):
   webbrowser.open_new_tab(url)

def print_answers():
    print("Selected Option: {}".format(amd_selected.get()))
    return None

def guide():
    openlink("file:///C:/Users/aksha/Desktop/How%20to%20Build%20a%20PC%20E%20Book.pdf")


def createnewsbtn(link):
    Button(news_frame, text="Read Full News", font=("TkHeadingFont", 25), bg="#28393a", fg="white", cursor="hand2",
           activebackground="#badee2", activeforeground="black", command=lambda: openlink(link)).pack()


def load_adminframe():
    admin_frame.tkraise()
    admin_frame.pack_propagate(False)

    def insertcomp():
        insertwindow=Toplevel()
        insertwindow.geometry("800x500")
        insertwindow.configure(bg=bg_colour)
        insertwindow.resizable(False, False)
        def submitcomp():
            conn = sqlite3.connect('pcbuild.db')
            c = conn.cursor()

            c.execute("INSERT INTO components VALUES(:cname, :cprice, :pfno, :clink);",{'cname':comp_name.get(),'cprice':comp_price.get(),'pfno':comp_pltfm.get(),'clink':comp_link.get()})
            messagebox.showinfo("", "Component Added Successfully")

            conn.commit()
            conn.close()
            comp_pltfm.delete(0, END)
            comp_name.delete(0, END)
            comp_price.delete(0, END)
            comp_link.delete(0, END)
            insertwindow.destroy()
        #create text boxes
        comp_pltfm=Entry(insertwindow,width=30,font=("TkMenuFont", 20))
        comp_pltfm.grid(row=0,column=1,padx=50,pady=20)
        comp_name=Entry(insertwindow,width=30,font=("TkMenuFont", 20))
        comp_name.grid(row=1,column=1,padx=50,pady=20)
        comp_price=Entry(insertwindow,width=30,font=("TkMenuFont", 20))
        comp_price.grid(row=2,column=1,padx=50,pady=20)
        comp_link=Entry(insertwindow,width=30,font=("TkMenuFont", 20))
        comp_link.grid(row=3,column=1,padx=50,pady=20)
        #create text box label
        comp_pltfm_label=Label(insertwindow,text="Component Platform\n(1.AMD 0.Intel)",bg=bg_colour, fg="black", font=("TkMenuFont", 20))
        comp_pltfm_label.grid(row=0,column=0)
        comp_name_label=Label(insertwindow,text="Component Name",bg=bg_colour, fg="black", font=("TkMenuFont", 20))
        comp_name_label.grid(row=1,column=0)
        comp_price_label=Label(insertwindow,text="Component Price",bg=bg_colour, fg="black", font=("TkMenuFont", 20))
        comp_price_label.grid(row=2,column=0)
        comp_link_label=Label(insertwindow,text="Component Link",bg=bg_colour, fg="black", font=("TkMenuFont", 20))
        comp_link_label.grid(row=3,column=0)

        #create submit button
        sub_btn=Button(insertwindow,text="Add component to database",command=submitcomp,font=("TkHeadingFont", 20), bg="#28393a", fg="white", cursor="hand2",
              activebackground="#badee2", activeforeground="black")
        sub_btn.grid(row=4,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

    def deletecomp():
        deletewindow=Toplevel()
        deletewindow.geometry("1280x720")
        deletewindow.configure(bg=bg_colour)
        deletewindow.resizable(False, False)
        def delete():
            conn = sqlite3.connect('pcbuild.db')
            c = conn.cursor()

            c.execute("DELETE FROM components WHERE oid="+delete_box.get())
            messagebox.showinfo("", "Component Deleted Successfull")

            conn.commit()
            conn.close()
            delete_box.delete(0, END)
            deletewindow.destroy()


        conn = sqlite3.connect('pcbuild.db')
        c = conn.cursor()

        Style = ttk.Style()
        Style.theme_use("clam")
        Style.configure("Treeview", background="silver", foreground="black", rowheight=35, fieldbackground="#70D6AA")
        Style.map("Treeview", background=[("selected", "green")])
        tree = ttk.Treeview(deletewindow, column=("Component ID", "Component Name", "Price", "Platform", "Link"),show='headings')
        tree.column("#1", anchor=tkinter.CENTER)
        tree.heading("#1", text="Component ID")
        tree.column("#2", anchor=tkinter.CENTER)
        tree.heading("#2", text="Component Name")
        tree.column("#3", anchor=tkinter.CENTER)
        tree.heading("#3", text="Price")
        tree.column("#4", anchor=tkinter.CENTER)
        tree.heading("#4", text="Platform")
        tree.column("#5", anchor=tkinter.CENTER)
        tree.heading("#5", text="Link")
        c.execute("SELECT oid,* FROM components")
        rows = c.fetchall()
        tree.tag_configure('oddrow', background="white")
        tree.tag_configure('evenrow', background="lightgreen")
        global count
        count = 0
        for row in rows:
            if count % 2 == 0:
                tree.insert("", tkinter.END, values=row, tags=('evenrow',))
            else:
                tree.insert("", tkinter.END, values=row, tags=('oddrow',))
            count = count + 1
        tree.pack()

        delete_btn=Button(deletewindow,text="Delete Component from database",font=("TkHeadingFont", 25), bg="#28393a", fg="white", cursor="hand2",
           activebackground="#badee2", activeforeground="black",command=delete)
        delete_btn.place(x=400,y=650)
        delete_box=Entry(deletewindow,width=28,font=("TkHeadingFont", 25))
        delete_box.place(x=400,y=600)
        Label(deletewindow,text="Enter ID of Component", bg=bg_colour, fg="black", font=("TkMenuFont", 15)).place(x=190,y=600)

        conn.commit()
        conn.close()

    Label(admin_frame, text="Administrator Menu", bg=bg_colour, fg="black", font=("TkMenuFont", 30)).place(x=475,y=100)
    Button(admin_frame, text="Insert Component", font=("TkHeadingFont", 25), bg="#28393a", fg="white", cursor="hand2",
           activebackground="#badee2", activeforeground="black",command=insertcomp).place(x=500,y=200)
    Button(admin_frame, text="Delete Component", font=("TkHeadingFont", 25), bg="#28393a", fg="white", cursor="hand2",
           activebackground="#badee2", activeforeground="black", command=deletecomp).place(x=500,y=300)
    Button(admin_frame, text="Main Menu", font=("TkHeadingFont", 20), bg="#28393a", fg="white", cursor="hand2",
           activebackground="#badee2", activeforeground="black", command=lambda: frame1.tkraise()).place(x=10, y=10)


def load_loginframe():
    def passcheck(user, passw):
        if user == "Akshay" and passw == "admin":
            messagebox.showinfo("", "Login Successfull")
            load_adminframe()
        else:
            messagebox.showerror("", "Invalid Username or Password\n\nTry Again!")
            username.delete(0, END)
            password.delete(0, END)

    login_frame.tkraise()
    login_frame.pack_propagate(False)
    Label(login_frame, text="Username", bg=bg_colour, fg="black", font=("TkMenuFont", 20)).place(x=315,y=150)
    username=Entry(login_frame,width=20,borderwidth=3,font=("TkMenuFont", 20))
    username.pack(pady=150)
    Label(login_frame, text="Password", bg=bg_colour, fg="black", font=("TkMenuFont", 20)).place(x=315, y=250)
    password = Entry(login_frame, width=20, borderwidth=3,show="*", font=("TkMenuFont", 20))
    password.place(x=485, y=250)
    Button(login_frame, text="Login", font=("TkHeadingFont", 25), bg="#28393a", fg="white", cursor="hand2",
           activebackground="#badee2", activeforeground="black", command=lambda: passcheck(username.get(),password.get())).pack(pady=10)
    Button(login_frame, text="Main Menu", font=("TkHeadingFont", 20), bg="#28393a", fg="white", cursor="hand2",
           activebackground="#badee2", activeforeground="black", command=lambda: frame1.tkraise()).place(x=10, y=10)


def load_news_frame():
    news_frame.tkraise()
    news_frame.pack_propagate(False)
    print("NEWS")
    news = GoogleNews(period='1d')
    news.search("Ryzen Intel Nvidia")
    result = news.result()
    data = pd.DataFrame.from_dict(result)
    data = data.drop(columns=["img"])
    data.head()
    loop=0
    for i in result:
        Label(news_frame, text=i["title"], bg=bg_colour, fg="black", font=("TkMenuFont", 20)).pack()
        Label(news_frame, text=i["desc"], bg=bg_colour, fg="white", font=("TkMenuFont", 20)).pack()
        createnewsbtn(i["link"])
        Label(news_frame, text="\n", bg=bg_colour, fg="white", font=("TkMenuFont", 20)).pack()
        print("Title : ", i["title"])
        print("News : ", i["desc"])
        print("Read Full News : ", i["link"])
        loop=loop+1
        if loop==3:
            break
    back_btn = Button(news_frame, text="Main Menu",font=("TkHeadingFont", 10), bg="#28393a", fg="white", cursor="hand2",
              activebackground="#badee2", activeforeground="black", command=lambda :frame1.tkraise()).place(x=10,y=10)

def load_frame3():
    amdwindow = Toplevel()
    amdwindow.geometry("1270x700")
    amdwindow.configure(bg=bg_colour)
    amdwindow.resizable(False, False)

    logo_img = ImageTk.PhotoImage(file="Photo.png")
    logo_widget = Label(amdwindow, image=logo_img, bg=bg_colour)
    logo_widget.image = logo_img

    Label(amdwindow, text="Select CPU:  ", bg=bg_colour, fg="black", font=("TkMenuFont", 20)).grid(row=0,column=0,padx=10,pady=20)
    Label(amdwindow, text="Select CPU Cooler:  ", bg=bg_colour, fg="black", font=("TkMenuFont", 20)).grid(row=1, column=0,padx=10,pady=10)
    Label(amdwindow, text="Select Motherboard:  ", bg=bg_colour, fg="black", font=("TkMenuFont", 20)).grid(row=2,column=0,padx=10,pady=10)
    Label(amdwindow, text="Select Memory:  ", bg=bg_colour, fg="black", font=("TkMenuFont", 20)).grid(row=3, column=0,padx=10,pady=10)
    Label(amdwindow, text="Select Storage:  ", bg=bg_colour, fg="black", font=("TkMenuFont", 20)).grid(row=4,column=0,padx=10,pady=10)
    Label(amdwindow, text="Select GPU:  ", bg=bg_colour, fg="black", font=("TkMenuFont", 20)).grid(row=5, column=0,padx=10,pady=10)
    Label(amdwindow, text="Select Case:  ", bg=bg_colour, fg="black", font=("TkMenuFont", 20)).grid(row=6,column=0,padx=10,pady=10)
    Label(amdwindow, text="Select Power Supply:  ", bg=bg_colour, fg="black", font=("TkMenuFont", 20)).grid(row=7, column=0,padx=10,pady=10)

    conn = sqlite3.connect('pcbuild.db')
    c = conn.cursor()

    cpures = c.execute("SELECT comp_name from components where comp_pltfm=10;")
    cpulist = [r for r, in cpures]
    cpuclicked=StringVar()
    cpuclicked.set("Select")
    cpudrop=OptionMenu(amdwindow,cpuclicked, *cpulist)
    cpudrop.grid(row=0, column=1)

    cpucores = c.execute("SELECT comp_name from components where comp_pltfm=11;")
    cpucolist = [r for r, in cpucores]
    cpucoclicked=StringVar()
    cpucoclicked.set("Select")
    cpucodrop=OptionMenu(amdwindow,cpucoclicked, *cpucolist)
    cpucodrop.grid(row=1, column=1)

    mobores = c.execute("SELECT comp_name from components where comp_pltfm=12;")
    mobolist = [r for r, in mobores]
    moboclicked=StringVar()
    moboclicked.set("Select")
    mobodrop=OptionMenu(amdwindow,moboclicked, *mobolist)
    mobodrop.grid(row=2, column=1)

    memres = c.execute("SELECT comp_name from components where comp_pltfm=99;")
    memlist = [r for r, in memres]
    memclicked = StringVar()
    memclicked.set("Select")
    memdrop = OptionMenu(amdwindow, memclicked, *memlist)
    memdrop.grid(row=3, column=1)

    stres = c.execute("SELECT comp_name from components where comp_pltfm=3;")
    stlist = [r for r, in stres]
    stclicked=StringVar()
    stclicked.set("Select")
    stdrop=OptionMenu(amdwindow,stclicked, *stlist)
    stdrop.grid(row=4, column=1)

    gpures = c.execute("SELECT comp_name from components where comp_pltfm=4;")
    gpulist = [r for r, in gpures]
    print(gpulist)
    gpuclicked=StringVar()
    gpuclicked.set("Select")
    gpudrop=OptionMenu(amdwindow,gpuclicked, *gpulist)
    gpudrop.grid(row=5, column=1)

    cseres = c.execute("SELECT comp_name from components where comp_pltfm=7;")
    cselist = [r for r, in cseres]
    cseclicked=StringVar()
    cseclicked.set("Select")
    csedrop=OptionMenu(amdwindow,cseclicked, *cselist)
    csedrop.grid(row=6, column=1)

    psures = c.execute("SELECT comp_name from components where comp_pltfm=6;")
    psulist = [r for r, in psures]
    psuclicked=StringVar()
    psuclicked.set("Select")
    print(psulist)
    psudrop = OptionMenu( amdwindow , psuclicked , *psulist)
    psudrop.grid(row=7, column=1)

    Button(amdwindow, text="Submit", font=("TkHeadingFont", 25), bg="#28393a", fg="white", cursor="hand2",activebackground="#badee2", activeforeground="black",
           command=lambda: amdsummary()).grid(row=8,column=2,padx=150,pady=40)

    logo_widget.place(x=550, y=50)

    def amdsummary():
        conn = sqlite3.connect('pcbuild.db')
        c = conn.cursor()
        flag=0
        for clicked in {cpuclicked.get(),cpucoclicked.get(),moboclicked.get(),memclicked.get(),stclicked.get(),gpuclicked.get(),cseclicked.get(),psuclicked.get()}:
            if clicked=="Select":
                flag=1
        if flag==1:
            return
        else:
            amdwindow.destroy()
            amdsummarywindow = Toplevel()
            amdsummarywindow.geometry("1920x1080")
            amdsummarywindow.configure(bg=bg_colour)

            c.execute("SELECT comp_price from components where comp_name='"+cpuclicked.get()+"'")
            cpuprice = int(str(c.fetchall())[2:-3])
            c.execute("SELECT link from components where comp_name='" + cpuclicked.get() + "'")
            cpulink=str(c.fetchall())[3:-4]
#          cpulink=cpulink[3:-4]

            c.execute("SELECT comp_price from components where comp_name='"+cpucoclicked.get()+"'")
            cpucoprice = int(str(c.fetchall())[2:-3])
            c.execute("SELECT link from components where comp_name='" + cpucoclicked.get() + "'")
            cpucolink=str(c.fetchall())[3:-4]
 #           cpucolink=cpucolink[3:-4]

            c.execute("SELECT comp_price from components where comp_name='"+moboclicked.get()+"'")
            moboprice = int(str(c.fetchall())[2:-3])
            c.execute("SELECT link from components where comp_name='" + moboclicked.get() + "'")
            mobolink=str(c.fetchall())[3:-4]
            #mobolink=mobolink[3:-4]

            c.execute("SELECT comp_price from components where comp_name='"+memclicked.get()+"'")
            memprice = int(str(c.fetchall())[2:-3])
            c.execute("SELECT link from components where comp_name='" + memclicked.get() + "'")
            memlink=str(c.fetchall())[3:-4]
            #memlink=memlink[3:-4]

            c.execute("SELECT comp_price from components where comp_name='"+stclicked.get()+"'")
            stprice = int(str(c.fetchall())[2:-3])
            c.execute("SELECT link from components where comp_name='" + stclicked.get() + "'")
            stlink=str(c.fetchall())[3:-4]
            #stlink=stlink[3:-4]

            c.execute("SELECT comp_price from components where comp_name='"+gpuclicked.get()+"'")
            gpuprice = int(str(c.fetchall())[2:-3])
            c.execute("SELECT link from components where comp_name='" + gpuclicked.get() + "'")
            gpulink=str(c.fetchall())[3:-4]
            #gpulink=gpulink[3:-4]

            c.execute("SELECT comp_price from components where comp_name='"+cseclicked.get()+"'")
            cseprice = int(str(c.fetchall())[2:-3])
            c.execute("SELECT link from components where comp_name='" + cseclicked.get() + "'")
            cselink=str(c.fetchall())[3:-4]
            #cselink=cselink[3:-4]

            c.execute("SELECT comp_price from components where comp_name='"+psuclicked.get()+"'")
            psuprice = int(str(c.fetchall())[2:-3])
            c.execute("SELECT link from components where comp_name='" + psuclicked.get() + "'")
            psulink=str(c.fetchall())[3:-4]
            #psulink=psulink[3:-4]

            Label(amdsummarywindow, text="           SUMMARY", bg=bg_colour, fg="black", font=("TkMenuFont", 30)).grid(row=0,column=0,columnspan=100,padx=50)
            Label(amdsummarywindow, text="CPU: ", bg="#28393a", fg="black", font=("TkMenuFont", 25)).grid(row=1,column=0,padx=10,pady=20)
            Label(amdsummarywindow, text="CPU Cooler: ", bg="#28393a", fg="black", font=("TkMenuFont", 25)).grid(row=2, column=0, padx=10, pady=20)
            Label(amdsummarywindow, text="Motherboard:  ", bg="#28393a", fg="black", font=("TkMenuFont", 25)).grid(row=3, column=0, padx=10, pady=20)
            Label(amdsummarywindow, text="Memory:  ", bg="#28393a", fg="black", font=("TkMenuFont", 25)).grid(row=4, column=0, padx=10, pady=20)
            Label(amdsummarywindow, text="Storage:  ", bg="#28393a", fg="black", font=("TkMenuFont", 25)).grid(row=5, column=0, padx=10, pady=20)
            Label(amdsummarywindow, text="GPU:  ", bg="#28393a", fg="black", font=("TkMenuFont", 25)).grid(row=6, column=0, padx=10, pady=20)
            Label(amdsummarywindow, text="Case:  ", bg="#28393a", fg="black", font=("TkMenuFont", 25)).grid(row=7, column=0, padx=10, pady=20)
            Label(amdsummarywindow, text="PSU:  ", bg="#28393a", fg="black", font=("TkMenuFont", 25)).grid(row=8, column=0, padx=10, pady=20)
            Label(amdsummarywindow, text="      TOTAL: Rs "+str(cpuprice+cpucoprice+moboprice+memprice+stprice+cseprice+gpuprice+psuprice), bg=bg_colour, fg="black", font=("TkMenuFont", 30)).grid(row=4,column=3,pady=10)

            Label(amdsummarywindow, text=str(cpuclicked.get()), bg=bg_colour, fg="black", font=("TkMenuFont", 20)).grid(row=1,column=1,padx=10,pady=20)
            Label(amdsummarywindow, text=str(cpucoclicked.get()), bg=bg_colour, fg="black", font=("TkMenuFont", 20)).grid(row=2, column=1, padx=10, pady=20)
            Label(amdsummarywindow, text=str(moboclicked.get()), bg=bg_colour, fg="black", font=("TkMenuFont", 20)).grid(row=3, column=1, padx=10, pady=20)
            Label(amdsummarywindow, text=str(memclicked.get()), bg=bg_colour, fg="black", font=("TkMenuFont", 20)).grid(row=4, column=1, padx=10, pady=20)
            Label(amdsummarywindow, text=str(stclicked.get()), bg=bg_colour, fg="black", font=("TkMenuFont", 20)).grid(row=5, column=1, padx=10, pady=20)
            Label(amdsummarywindow, text=str(gpuclicked.get()), bg=bg_colour, fg="black", font=("TkMenuFont", 20)).grid(row=6, column=1, padx=10, pady=20)
            Label(amdsummarywindow, text=str(cseclicked.get()), bg=bg_colour, fg="black", font=("TkMenuFont", 20)).grid(row=7, column=1, padx=10, pady=20)
            Label(amdsummarywindow, text=str(psuclicked.get()), bg=bg_colour, fg="black", font=("TkMenuFont", 20)).grid(row=8, column=1, padx=10, pady=20)

            Label(amdsummarywindow, text="  Rs "+str(cpuprice), bg=bg_colour, fg="black", font=("TkMenuFont", 20)).grid(row=1,column=2,padx=10,pady=20)
            Label(amdsummarywindow, text="  Rs "+str(cpucoprice), bg=bg_colour, fg="black", font=("TkMenuFont", 20)).grid(row=2, column=2, padx=10, pady=20)
            Label(amdsummarywindow, text="  Rs "+str(moboprice), bg=bg_colour, fg="black", font=("TkMenuFont", 20)).grid(row=3, column=2, padx=10, pady=20)
            Label(amdsummarywindow, text="  Rs "+str(memprice), bg=bg_colour, fg="black", font=("TkMenuFont", 20)).grid(row=4, column=2, padx=10, pady=20)
            Label(amdsummarywindow, text="  Rs "+str(stprice), bg=bg_colour, fg="black", font=("TkMenuFont", 20)).grid(row=5, column=2, padx=10, pady=20)
            Label(amdsummarywindow, text="  Rs "+str(gpuprice), bg=bg_colour, fg="black", font=("TkMenuFont", 20)).grid(row=6, column=2, padx=10, pady=20)
            Label(amdsummarywindow, text="  Rs "+str(cseprice), bg=bg_colour, fg="black", font=("TkMenuFont", 20)).grid(row=7, column=2, padx=10, pady=20)
            Label(amdsummarywindow, text="  Rs "+str(psuprice), bg=bg_colour, fg="black", font=("TkMenuFont", 20)).grid(row=8, column=2, padx=10, pady=20)

            Button(amdsummarywindow, text="BUY", font=("TkHeadingFont", 25), bg="#28393a", fg="white", cursor="hand2",
                   activebackground="#badee2", activeforeground="black",
                   command=lambda: amdbuy()).grid(row=5, column=3)

            def amdbuy():
                amdsummarywindow.destroy()
                amdbuywindow = Toplevel()
                amdbuywindow.geometry("1920x1080")
                amdbuywindow.configure(bg=bg_colour)
                Button(amdbuywindow, text="GUIDE", font=("TkHeadingFont", 25), bg="#28393a", fg="white",
                       cursor="hand2", activebackground="#badee2", activeforeground="black",
                       command=lambda: guide()).place(x=1050, y=340)
                Label(amdbuywindow, text="Trouble Building Your PC ?", bg=bg_colour, fg="Black",
                      font=("TkMenuFont", 18)).place(x=990, y=310)
                Label(amdbuywindow, text="CPU: ", bg="#28393a", fg="black", font=("TkMenuFont", 25)).grid(row=1,column=0,padx=10,pady=20)
                Label(amdbuywindow, text="CPU Cooler: ", bg="#28393a", fg="black", font=("TkMenuFont", 25)).grid(row=2, column=0, padx=10, pady=20)
                Label(amdbuywindow, text="Motherboard:  ", bg="#28393a", fg="black", font=("TkMenuFont", 25)).grid(row=3, column=0, padx=10, pady=20)
                Label(amdbuywindow, text="Memory:  ", bg="#28393a", fg="black", font=("TkMenuFont", 25)).grid(row=4,column=0,padx=10,pady=20)
                Label(amdbuywindow, text="Storage:  ", bg="#28393a", fg="black", font=("TkMenuFont", 25)).grid(row=5, column=0, padx=10, pady=20)
                Label(amdbuywindow, text="GPU:  ", bg="#28393a", fg="black", font=("TkMenuFont", 25)).grid(row=6,column=0,padx=10,pady=20)
                Label(amdbuywindow, text="Case:  ", bg="#28393a", fg="black", font=("TkMenuFont", 25)).grid(row=7,column=0,padx=10,pady=20)
                Label(amdbuywindow, text="PSU:  ", bg="#28393a", fg="black", font=("TkMenuFont", 25)).grid(row=8,column=0,padx=10,pady=20)

                def openlink(url):
                    webbrowser.open_new_tab(url)

                link1=Label(amdbuywindow, text=cpulink, fg="blue", cursor="hand2",bg=bg_colour,font= ('Helvetica 20 underline'))
                link1.grid(row=1,column=1)
                link1.bind("<Button-1>", lambda e: openlink(cpulink))

                link2=Label(amdbuywindow, text=cpucolink, fg="blue", cursor="hand2",bg=bg_colour,font= ('Helvetica 20 underline'))
                link2.grid(row=2,column=1)
                link2.bind("<Button-1>", lambda e: openlink(cpucolink))

                link3=Label(amdbuywindow, text=mobolink, fg="blue", cursor="hand2",bg=bg_colour,font= ('Helvetica 20 underline'))
                link3.grid(row=3,column=1)
                link3.bind("<Button-1>", lambda e: openlink(mobolink))

                link4=Label(amdbuywindow, text=memlink, fg="blue", cursor="hand2",bg=bg_colour,font= ('Helvetica 20 underline'))
                link4.grid(row=4,column=1)
                link4.bind("<Button-1>", lambda e: openlink(memlink))

                link5=Label(amdbuywindow, text=stlink, fg="blue", cursor="hand2",bg=bg_colour,font= ('Helvetica 20 underline'))
                link5.grid(row=5,column=1)
                link5.bind("<Button-1>", lambda e: openlink(stlink))

                link6=Label(amdbuywindow, text=gpulink, fg="blue", cursor="hand2",bg=bg_colour,font= ('Helvetica 20 underline'))
                link6.grid(row=6,column=1)
                link6.bind("<Button-1>", lambda e: openlink(gpulink))

                link7=Label(amdbuywindow, text=cselink, fg="blue", cursor="hand2",bg=bg_colour,font= ('Helvetica 20 underline'))
                link7.grid(row=7,column=1)
                link7.bind("<Button-1>", lambda e: openlink(cselink))

                link8=Label(amdbuywindow, text=psulink, fg="blue", cursor="hand2",bg=bg_colour,font= ('Helvetica 20 underline'))
                link8.grid(row=8,column=1)
                link8.bind("<Button-1>", lambda e: openlink(psulink))

                Label(amdbuywindow, text="Enjoy Building Your PC !", bg=bg_colour, fg="black",
                      font=("TkMenuFont", 20)).grid(row=9, column=1, padx=100, pady=20)


            conn.commit()
            conn.close()


    conn.commit()
    conn.close()



def load_frame4():
    intelwindow = Toplevel()
    intelwindow.geometry("1280x720")
    intelwindow.configure(bg=bg_colour)
    intelwindow.resizable(False, False)

    logo_img = ImageTk.PhotoImage(file="Photo.png")
    logo_widget = Label(intelwindow, image=logo_img, bg=bg_colour)
    logo_widget.image = logo_img


    Label(intelwindow, text="Select CPU:  ", bg=bg_colour, fg="black", font=("TkMenuFont", 20)).grid(row=0, column=0, padx=10, pady=20)
    Label(intelwindow, text="Select CPU Cooler:  ", bg=bg_colour, fg="black", font=("TkMenuFont", 20)).grid(row=1,column=0,padx=10,pady=10)
    Label(intelwindow, text="Select Motherboard:  ", bg=bg_colour, fg="black", font=("TkMenuFont", 20)).grid(row=2,column=0,padx=10,pady=10)
    Label(intelwindow, text="Select Memory:  ", bg=bg_colour, fg="black", font=("TkMenuFont", 20)).grid(row=3, column=0,padx=10, pady=10)
    Label(intelwindow, text="Select Storage:  ", bg=bg_colour, fg="black", font=("TkMenuFont", 20)).grid(row=4, column=0,padx=10, pady=10)
    Label(intelwindow, text="Select GPU:  ", bg=bg_colour, fg="black", font=("TkMenuFont", 20)).grid(row=5, column=0,padx=10, pady=10)
    Label(intelwindow, text="Select Case:  ", bg=bg_colour, fg="black", font=("TkMenuFont", 20)).grid(row=6, column=0,padx=10, pady=10)
    Label(intelwindow, text="Select Power Supply:  ", bg=bg_colour, fg="black", font=("TkMenuFont", 20)).grid(row=7,column=0,padx=10,pady=10)

    conn = sqlite3.connect('pcbuild.db')
    c = conn.cursor()

    cpures = c.execute("SELECT comp_name from components where comp_pltfm=67;")
    cpulist = [r for r, in cpures]
    cpuclicked = StringVar()
    cpuclicked.set("Select")
    cpudrop = OptionMenu(intelwindow, cpuclicked, *cpulist)
    cpudrop.grid(row=0, column=1)

    cpucores = c.execute("SELECT comp_name from components where comp_pltfm=11;")
    cpucolist = [r for r, in cpucores]
    cpucoclicked = StringVar()
    cpucoclicked.set("Select")
    cpucodrop = OptionMenu(intelwindow, cpucoclicked, *cpucolist)
    cpucodrop.grid(row=1, column=1)

    mobores = c.execute("SELECT comp_name from components where comp_pltfm=02;")
    mobolist = [r for r, in mobores]
    moboclicked = StringVar()
    moboclicked.set("Select")
    mobodrop = OptionMenu(intelwindow, moboclicked, *mobolist)
    mobodrop.grid(row=2, column=1)

    memres = c.execute("SELECT comp_name from components where comp_pltfm=99;")
    memlist = [r for r, in memres]
    memclicked = StringVar()
    memclicked.set("Select")
    memdrop = OptionMenu(intelwindow, memclicked, *memlist)
    memdrop.grid(row=3, column=1)

    stres = c.execute("SELECT comp_name from components where comp_pltfm=3;")
    stlist = [r for r, in stres]
    stclicked = StringVar()
    stclicked.set("Select")
    stdrop = OptionMenu(intelwindow, stclicked, *stlist)
    stdrop.grid(row=4, column=1)

    gpures = c.execute("SELECT comp_name from components where comp_pltfm=4;")
    gpulist = [r for r, in gpures]
    print(gpulist)
    gpuclicked = StringVar()
    gpuclicked.set("Select")
    gpudrop = OptionMenu(intelwindow, gpuclicked, *gpulist)
    gpudrop.grid(row=5, column=1)

    cseres = c.execute("SELECT comp_name from components where comp_pltfm=7;")
    cselist = [r for r, in cseres]
    cseclicked = StringVar()
    cseclicked.set("Select")
    csedrop = OptionMenu(intelwindow, cseclicked, *cselist)
    csedrop.grid(row=6, column=1)

    psures = c.execute("SELECT comp_name from components where comp_pltfm=6;")
    psulist = [r for r, in psures]
    psuclicked = StringVar()
    psuclicked.set("Select")
    psudrop = OptionMenu(intelwindow, psuclicked, *psulist)
    psudrop.grid(row=7, column=1)

    Button(intelwindow, text="Submit", font=("TkHeadingFont", 25), bg="#28393a", fg="white", cursor="hand2",activebackground="#badee2", activeforeground="black",command=lambda: amdsummary()).grid(row=8, column=2, padx=150, pady=40)

    logo_widget.place(x=550,y=50)
    def amdsummary():
        conn = sqlite3.connect('pcbuild.db')
        c = conn.cursor()
        flag = 0
        for clicked in {cpuclicked.get(), cpucoclicked.get(), moboclicked.get(), memclicked.get(), stclicked.get(),
                        gpuclicked.get(), cseclicked.get(), psuclicked.get()}:
            if clicked == "Select":
                flag = 1
        if flag == 1:
            return
        else:
            intelwindow.destroy()
            intelsummarywindow = Toplevel()
            intelsummarywindow.geometry("1920x1080")
            intelsummarywindow.configure(bg=bg_colour)

            c.execute("SELECT comp_price from components where comp_name='" + cpuclicked.get() + "'")
            cpuprice = int(str(c.fetchall())[2:-3])
            c.execute("SELECT link from components where comp_name='" + cpuclicked.get() + "'")
            cpulink = str(c.fetchall())[3:-4]

            c.execute("SELECT comp_price from components where comp_name='" + cpucoclicked.get() + "'")
            cpucoprice = int(str(c.fetchall())[2:-3])
            c.execute("SELECT link from components where comp_name='" + cpucoclicked.get() + "'")
            cpucolink = str(c.fetchall())[3:-4]

            c.execute("SELECT comp_price from components where comp_name='" + moboclicked.get() + "'")
            moboprice = int(str(c.fetchall())[2:-3])
            c.execute("SELECT link from components where comp_name='" + moboclicked.get() + "'")
            mobolink = str(c.fetchall())[3:-4]

            c.execute("SELECT comp_price from components where comp_name='" + memclicked.get() + "'")
            memprice = int(str(c.fetchall())[2:-3])
            c.execute("SELECT link from components where comp_name='" + memclicked.get() + "'")
            memlink = str(c.fetchall())[3:-4]

            c.execute("SELECT comp_price from components where comp_name='" + stclicked.get() + "'")
            stprice = int(str(c.fetchall())[2:-3])
            c.execute("SELECT link from components where comp_name='" + stclicked.get() + "'")
            stlink = str(c.fetchall())[3:-4]

            c.execute("SELECT comp_price from components where comp_name='" + gpuclicked.get() + "'")
            gpuprice = int(str(c.fetchall())[2:-3])
            c.execute("SELECT link from components where comp_name='" + gpuclicked.get() + "'")
            gpulink = str(c.fetchall())[3:-4]

            c.execute("SELECT comp_price from components where comp_name='" + cseclicked.get() + "'")
            cseprice = int(str(c.fetchall())[2:-3])
            c.execute("SELECT link from components where comp_name='" + cseclicked.get() + "'")
            cselink = str(c.fetchall())[3:-4]

            c.execute("SELECT comp_price from components where comp_name='" + psuclicked.get() + "'")
            psuprice = int(str(c.fetchall())[2:-3])
            c.execute("SELECT link from components where comp_name='" + psuclicked.get() + "'")
            psulink = str(c.fetchall())[3:-4]

            Label(intelsummarywindow, text="           SUMMARY", bg=bg_colour, fg="black", font=("TkMenuFont", 30)).grid(row=0, column=0, columnspan=100, padx=50)
            Label(intelsummarywindow, text="CPU: ", bg="#28393a", fg="black", font=("TkMenuFont", 25)).grid(row=1,column=0,padx=10,pady=20)
            Label(intelsummarywindow, text="CPU Cooler: ", bg="#28393a", fg="black", font=("TkMenuFont", 25)).grid(row=2,column=0,padx=10,pady=20)
            Label(intelsummarywindow, text="Motherboard:  ", bg="#28393a", fg="black", font=("TkMenuFont", 25)).grid(row=3, column=0, padx=10, pady=20)
            Label(intelsummarywindow, text="Memory:  ", bg="#28393a", fg="black", font=("TkMenuFont", 25)).grid(row=4,column=0,padx=10,pady=20)
            Label(intelsummarywindow, text="Storage:  ", bg="#28393a", fg="black", font=("TkMenuFont", 25)).grid(row=5,column=0,padx=10,pady=20)
            Label(intelsummarywindow, text="GPU:  ", bg="#28393a", fg="black", font=("TkMenuFont", 25)).grid(row=6,column=0,padx=10,pady=20)
            Label(intelsummarywindow, text="Case:  ", bg="#28393a", fg="black", font=("TkMenuFont", 25)).grid(row=7,column=0,padx=10,pady=20)
            Label(intelsummarywindow, text="PSU:  ", bg="#28393a", fg="black", font=("TkMenuFont", 25)).grid(row=8,column=0,padx=10,pady=20)
            Label(intelsummarywindow, text="      TOTAL: Rs " + str(cpuprice + cpucoprice + moboprice + memprice + stprice + cseprice + gpuprice + psuprice), bg=bg_colour,fg="black", font=("TkMenuFont", 30)).grid(row=4, column=3, pady=10)

            Label(intelsummarywindow, text=str(cpuclicked.get()), bg=bg_colour, fg="black", font=("TkMenuFont", 20)).grid(row=1, column=1, padx=10, pady=20)
            Label(intelsummarywindow, text=str(cpucoclicked.get()), bg=bg_colour, fg="black",font=("TkMenuFont", 20)).grid(row=2, column=1, padx=10, pady=20)
            Label(intelsummarywindow, text=str(moboclicked.get()), bg=bg_colour, fg="black",font=("TkMenuFont", 20)).grid(row=3, column=1, padx=10, pady=20)
            Label(intelsummarywindow, text=str(memclicked.get()), bg=bg_colour, fg="black", font=("TkMenuFont", 20)).grid(row=4, column=1, padx=10, pady=20)
            Label(intelsummarywindow, text=str(stclicked.get()), bg=bg_colour, fg="black", font=("TkMenuFont", 20)).grid(row=5, column=1, padx=10, pady=20)
            Label(intelsummarywindow, text=str(gpuclicked.get()), bg=bg_colour, fg="black", font=("TkMenuFont", 20)).grid(row=6, column=1, padx=10, pady=20)
            Label(intelsummarywindow, text=str(cseclicked.get()), bg=bg_colour, fg="black", font=("TkMenuFont", 20)).grid(row=7, column=1, padx=10, pady=20)
            Label(intelsummarywindow, text=str(psuclicked.get()), bg=bg_colour, fg="black", font=("TkMenuFont", 20)).grid(row=8, column=1, padx=10, pady=20)

            Label(intelsummarywindow, text="  Rs " + str(cpuprice), bg=bg_colour, fg="black",font=("TkMenuFont", 20)).grid(row=1, column=2, padx=10, pady=20)
            Label(intelsummarywindow, text="  Rs " + str(cpucoprice), bg=bg_colour, fg="black",font=("TkMenuFont", 20)).grid(row=2, column=2, padx=10, pady=20)
            Label(intelsummarywindow, text="  Rs " + str(moboprice), bg=bg_colour, fg="black",font=("TkMenuFont", 20)).grid(row=3, column=2, padx=10, pady=20)
            Label(intelsummarywindow, text="  Rs " + str(memprice), bg=bg_colour, fg="black",font=("TkMenuFont", 20)).grid(row=4, column=2, padx=10, pady=20)
            Label(intelsummarywindow, text="  Rs " + str(stprice), bg=bg_colour, fg="black",font=("TkMenuFont", 20)).grid(row=5, column=2, padx=10, pady=20)
            Label(intelsummarywindow, text="  Rs " + str(gpuprice), bg=bg_colour, fg="black",font=("TkMenuFont", 20)).grid(row=6, column=2, padx=10, pady=20)
            Label(intelsummarywindow, text="  Rs " + str(cseprice), bg=bg_colour, fg="black",font=("TkMenuFont", 20)).grid(row=7, column=2, padx=10, pady=20)
            Label(intelsummarywindow, text="  Rs " + str(psuprice), bg=bg_colour, fg="black",font=("TkMenuFont", 20)).grid(row=8, column=2, padx=10, pady=20)

            Button(intelsummarywindow, text="BUY", font=("TkHeadingFont", 25), bg="#28393a", fg="white", cursor="hand2",activebackground="#badee2", activeforeground="black",command=lambda: amdbuy()).grid(row=5, column=3)

            def amdbuy():
                intelsummarywindow.destroy()
                intelbuywindow = Toplevel()
                intelbuywindow.geometry("1920x1080")
                intelbuywindow.configure(bg=bg_colour)
                Label(intelbuywindow, text="CPU: ", bg="#28393a", fg="black", font=("TkMenuFont", 25)).grid(row=1,column=0,padx=10,pady=20)
                Label(intelbuywindow, text="CPU Cooler: ", bg="#28393a", fg="black", font=("TkMenuFont", 25)).grid(row=2,column=0,padx=10,pady=20)
                Label(intelbuywindow, text="Motherboard:  ", bg="#28393a", fg="black", font=("TkMenuFont", 25)).grid(row=3, column=0, padx=10, pady=20)
                Label(intelbuywindow, text="Memory:  ", bg="#28393a", fg="black", font=("TkMenuFont", 25)).grid(row=4,column=0,padx=10,pady=20)
                Label(intelbuywindow, text="Storage:  ", bg="#28393a", fg="black", font=("TkMenuFont", 25)).grid(row=5,column=0,padx=10,pady=20)
                Label(intelbuywindow, text="GPU:  ", bg="#28393a", fg="black", font=("TkMenuFont", 25)).grid(row=6,column=0,padx=10,pady=20)
                Label(intelbuywindow, text="Case:  ", bg="#28393a", fg="black", font=("TkMenuFont", 25)).grid(row=7,column=0,padx=10,pady=20)
                Label(intelbuywindow, text="PSU:  ", bg="#28393a", fg="black", font=("TkMenuFont", 25)).grid(row=8,column=0,padx=10,pady=20)

                Button(intelbuywindow, text="GUIDE", font=("TkHeadingFont", 25), bg="#28393a", fg="white",
                       cursor="hand2", activebackground="#badee2", activeforeground="black",
                       command=lambda: guide()).place(x=1050,y=340)
                Label(intelbuywindow, text="Trouble Building Your PC ?", bg=bg_colour, fg="Black",
                      font=("TkMenuFont", 18)).place(x=990, y=310)

                def openlink(url):
                    webbrowser.open_new_tab(url)

                link1 = Label(intelbuywindow, text=cpulink, fg="blue", cursor="hand2", bg=bg_colour,font=('Helvetica 20 underline'))
                link1.grid(row=1, column=1)
                link1.bind("<Button-1>", lambda e: openlink(cpulink))

                link2 = Label(intelbuywindow, text=cpucolink, fg="blue", cursor="hand2", bg=bg_colour,font=('Helvetica 20 underline'))
                link2.grid(row=2, column=1)
                link2.bind("<Button-1>", lambda e: openlink(cpucolink))

                link3 = Label(intelbuywindow, text=mobolink, fg="blue", cursor="hand2", bg=bg_colour,font=('Helvetica 20 underline'))
                link3.grid(row=3, column=1)
                link3.bind("<Button-1>", lambda e: openlink(mobolink))

                link4 = Label(intelbuywindow, text=memlink, fg="blue", cursor="hand2", bg=bg_colour,font=('Helvetica 20 underline'))
                link4.grid(row=4, column=1)
                link4.bind("<Button-1>", lambda e: openlink(memlink))

                link5 = Label(intelbuywindow, text=stlink, fg="blue", cursor="hand2", bg=bg_colour,font=('Helvetica 20 underline'))
                link5.grid(row=5, column=1)
                link5.bind("<Button-1>", lambda e: openlink(stlink))

                link6 = Label(intelbuywindow, text=gpulink, fg="blue", cursor="hand2", bg=bg_colour,font=('Helvetica 20 underline'))
                link6.grid(row=6, column=1)
                link6.bind("<Button-1>", lambda e: openlink(gpulink))

                link7 = Label(intelbuywindow, text=cselink, fg="blue", cursor="hand2", bg=bg_colour,font=('Helvetica 20 underline'))
                link7.grid(row=7, column=1)
                link7.bind("<Button-1>", lambda e: openlink(cselink))

                link8 = Label(intelbuywindow, text=psulink, fg="blue", cursor="hand2", bg=bg_colour,font=('Helvetica 20 underline'))
                link8.grid(row=8, column=1)
                link8.bind("<Button-1>", lambda e: openlink(psulink))

                Label(intelbuywindow, text="Enjoy Building Your PC !", bg=bg_colour, fg="black",font=("TkMenuFont", 20)).grid(row=9, column=1, padx=100, pady=20)

            conn.commit()
            conn.close()

    conn.commit()
    conn.close()


def load_frame2():
    frame2.tkraise()
    frame2.pack_propagate(False)
    amd_btn = ImageTk.PhotoImage(file="amd.png")
    amd_widget = Label(frame2, image=amd_btn, bg=bg_colour)
    amd_widget.image=amd_btn
    amd_widget.pack(pady=100,padx=10)
    Label(frame2, text="Choose Processor Platform", bg=bg_colour, fg="Black", font=("TkMenuFont", 25)).place(x=455,y=10)
    amd_widget.place(relx=0.3,rely=0.5,anchor='center')
    intel_btn = ImageTk.PhotoImage(file="intel.png")
    intel_widget = Label(frame2, image=intel_btn, bg=bg_colour)
    intel_widget.image = intel_btn
    intel_widget.pack(pady=100, padx=10)
    intel_widget.place(relx=0.65, rely=0.5, anchor='center')
    button1=Button(frame2, text="AMD", font=("TkHeadingFont", 25), bg="#28393a", fg="white", cursor="hand2",
              activebackground="#badee2", activeforeground="black", command=lambda: load_frame3())
    button1.place(x=350,y=550)
    button2 = Button(frame2, text="Intel", font=("TkHeadingFont", 25), bg="#28393a", fg="white", cursor="hand2",
                        activebackground="#badee2", activeforeground="black", command=lambda: load_frame4())
    button2.place(x=800, y=550)
    back_btn = Button(frame2, text="Main Menu",font=("TkHeadingFont", 10), bg="#28393a", fg="white", cursor="hand2",
              activebackground="#badee2", activeforeground="black", command=lambda :frame1.tkraise()).place(x=10,y=10)


    print("HI DA BUNDA")

def load_genie_frame():
    geniewindow = Toplevel()
    geniewindow.geometry("600x300")
    geniewindow.configure(bg=bg_colour)
    geniewindow.resizable(False, False)

    budget_label=Label(geniewindow, text="  ENTER YOUR BUDGET ", bg="#28393a", fg="black", font=("TkMenuFont", 25))
    budget_label.grid(row=1, column=0,padx=10, pady=20)
    budget_box = Entry(geniewindow, width=30, font=("TkMenuFont", 20))
    budget_box.grid(row=2, column=0, padx=50, pady=20)
    button2 = Button(geniewindow, text="FIND MY SPECS", font=("TkHeadingFont", 25), bg="#28393a", fg="white", cursor="hand2",
                     activebackground="#badee2", activeforeground="black", command=lambda: coregenie())
    button2.grid(row=3, column=0, padx=50, pady=20)

    def display(cpuname,cpuprice,cpuconame,cpucoprice,moboname,moboprice,memname,memprice,stname,stprice,gpuname,gpuprice,csename,cseprice,psuname,psuprice):
        Label(geniewindow, text="           THE BEST SPECS FOR YOUR BUDGET", bg=bg_colour, fg="black", font=("TkMenuFont", 30)).grid(
            row=0, column=0, columnspan=100, padx=50)
        Label(geniewindow, text="CPU: ", bg="#28393a", fg="black", font=("TkMenuFont", 25)).grid(row=1, column=0,
                                                                                                        padx=10,
                                                                                                        pady=20)
        Label(geniewindow, text="CPU Cooler: ", bg="#28393a", fg="black", font=("TkMenuFont", 25)).grid(row=2,
                                                                                                               column=0,
                                                                                                               padx=10,
                                                                                                               pady=20)
        Label(geniewindow, text="Motherboard:  ", bg="#28393a", fg="black", font=("TkMenuFont", 25)).grid(row=3,
                                                                                                                 column=0,
                                                                                                                 padx=10,
                                                                                                                 pady=20)
        Label(geniewindow, text="Memory:  ", bg="#28393a", fg="black", font=("TkMenuFont", 25)).grid(row=4,
                                                                                                            column=0,
                                                                                                            padx=10,
                                                                                                            pady=20)
        Label(geniewindow, text="Storage:  ", bg="#28393a", fg="black", font=("TkMenuFont", 25)).grid(row=5,
                                                                                                             column=0,
                                                                                                             padx=10,
                                                                                                             pady=20)
        Label(geniewindow, text="GPU:  ", bg="#28393a", fg="black", font=("TkMenuFont", 25)).grid(row=6,
                                                                                                         column=0,
                                                                                                         padx=10,
                                                                                                         pady=20)
        Label(geniewindow, text="Case:  ", bg="#28393a", fg="black", font=("TkMenuFont", 25)).grid(row=7,
                                                                                                          column=0,
                                                                                                          padx=10,
                                                                                                          pady=20)
        Label(geniewindow, text="PSU:  ", bg="#28393a", fg="black", font=("TkMenuFont", 25)).grid(row=8,
                                                                                                         column=0,
                                                                                                         padx=10,
                                                                                                         pady=20)
        Label(geniewindow, text="      TOTAL: Rs " + str(
            cpuprice + cpucoprice + moboprice + memprice + stprice + cseprice + gpuprice + psuprice), bg=bg_colour,
              fg="black", font=("TkMenuFont", 30)).grid(row=4, column=3, pady=10)

        Label(geniewindow, text=cpuname, bg=bg_colour, fg="black", font=("TkMenuFont", 20)).grid(
            row=1, column=1, padx=10, pady=20)
        Label(geniewindow, text=cpuconame, bg=bg_colour, fg="black", font=("TkMenuFont", 20)).grid(
            row=2, column=1, padx=10, pady=20)
        Label(geniewindow, text=moboname, bg=bg_colour, fg="black", font=("TkMenuFont", 20)).grid(
            row=3, column=1, padx=10, pady=20)
        Label(geniewindow, text=memname, bg=bg_colour, fg="black", font=("TkMenuFont", 20)).grid(
            row=4, column=1, padx=10, pady=20)
        Label(geniewindow, text=stname, bg=bg_colour, fg="black", font=("TkMenuFont", 20)).grid(
            row=5, column=1, padx=10, pady=20)
        Label(geniewindow, text=gpuname, bg=bg_colour, fg="black", font=("TkMenuFont", 20)).grid(
            row=6, column=1, padx=10, pady=20)
        Label(geniewindow, text=csename, bg=bg_colour, fg="black", font=("TkMenuFont", 20)).grid(
            row=7, column=1, padx=10, pady=20)
        Label(geniewindow, text=psuname, bg=bg_colour, fg="black", font=("TkMenuFont", 20)).grid(
            row=8, column=1, padx=10, pady=20)

        Label(geniewindow, text="  Rs " + str(cpuprice), bg=bg_colour, fg="black", font=("TkMenuFont", 20)).grid(
            row=1, column=2, padx=10, pady=20)
        Label(geniewindow, text="  Rs " + str(cpucoprice), bg=bg_colour, fg="black",
              font=("TkMenuFont", 20)).grid(row=2, column=2, padx=10, pady=20)
        Label(geniewindow, text="  Rs " + str(moboprice), bg=bg_colour, fg="black",
              font=("TkMenuFont", 20)).grid(row=3, column=2, padx=10, pady=20)
        Label(geniewindow, text="  Rs " + str(memprice), bg=bg_colour, fg="black", font=("TkMenuFont", 20)).grid(
            row=4, column=2, padx=10, pady=20)
        Label(geniewindow, text="  Rs " + str(stprice), bg=bg_colour, fg="black", font=("TkMenuFont", 20)).grid(
            row=5, column=2, padx=10, pady=20)
        Label(geniewindow, text="  Rs " + str(gpuprice), bg=bg_colour, fg="black", font=("TkMenuFont", 20)).grid(
            row=6, column=2, padx=10, pady=20)
        Label(geniewindow, text="  Rs " + str(cseprice), bg=bg_colour, fg="black", font=("TkMenuFont", 20)).grid(
            row=7, column=2, padx=10, pady=20)
        Label(geniewindow, text="  Rs " + str(psuprice), bg=bg_colour, fg="black", font=("TkMenuFont", 20)).grid(
            row=8, column=2, padx=10, pady=20)

    def coregenie():
        budget=int(budget_box.get())
        budget_label.destroy()
        budget_box.destroy()
        button2.destroy()
        geniewindow.geometry("1280x720")
        if (budget <= 50000):
            display("Intel i5 10400F",10419,"Stock Cooler",0,"MSI H410M PRO",5800,"Corsair Vengeance LPX 8GB",3249,"WD Blue NVMe 500GB",4449,"ASUS GeForce GTX 1050 Ti",15900,"Ant Esports ICE-200TG",2999,"Corsair CV550",3800)
        elif (budget > 50000 and budget <= 100000):
            display("Intel i5 12400F",14750,"Stock Cooler",0,"MSI PRO B660M-A",13350,"ADATA XPG GAMMIX D30 8GBx2",5300,"Kingston NV1 500GB NVMe",4025,"ZOTAC RTX 3060Ti Twin",37000,"SilverStone FARA R1",3399,"Corsair CX650F",5299)
        elif (budget > 100000 and budget <= 150000):
            display("AMD Ryzen 7 5700X",22750,"DeepCool AK400",4499,"MSI MAG B550M Mortar",15350,"GSkill RipJaws 16GBx2",9800,"Samsung Evo 1TB M.2 SSD",8025,"ZOTAC RTX 3070Ti Twin",47000,"NZXT H510i",6789,"Cooler Master G800",6750)
        else:
            display("Intel Core i7-12700F",33750,"DeepCool AK400",4499,"ASUS Prime B560-PLUS",16689,"Kingstun Fury DDR5 16 GB",13280,"Samsung 980 2TB NVMe SSD",16025,"Gigabyte RTX 3080",76000,"Deepcool MATRIXX 5",6999,"CORSAIR RMX RM1000X",16650)




def load_frame1():
    frame1.tkraise()
    frame1.pack_propagate(False)
    logo_img = ImageTk.PhotoImage(file="MainLogo1.png")
    logo_widget = Label(frame1, image=logo_img, bg=bg_colour)
    logo_widget.image = logo_img
    logo_widget.pack(pady=15)
    Label(frame1, text="Welcome\n\nPC Build Companion", bg=bg_colour, fg="white", font=("TkMenuFont", 25)).pack()
    Button(frame1, text="Choose Parts!", font=("TkHeadingFont", 25), bg="#28393a", fg="white", cursor="hand2",
              activebackground="#badee2", activeforeground="black", command=lambda:load_frame2()).pack(pady=40)
    Button(frame1, text="Adminstrator", font=("TkHeadingFont", 25), bg="#28393a", fg="white", cursor="hand2",
           activebackground="#badee2", activeforeground="black", command=lambda: load_loginframe()).place(x=1050,y=15)

    news_btn=Button(frame1, text="PC News!", font=("TkHeadingFont", 25), bg="#28393a", fg="white", cursor="hand2",
              activebackground="#badee2", activeforeground="black", command=lambda:load_news_frame())
    news_btn.place(x=10,y=15)
    news_btn=Button(frame1, text="PC Genie", font=("TkHeadingFont", 25), bg="#28393a", fg="white", cursor="hand2",
              activebackground="#badee2", activeforeground="black", command=lambda:load_genie_frame())
    news_btn.place(x=10,y=625)

root=Tk()
root.title("PC Build Companion")
root.eval("tk::PlaceWindow . center")
amd_selected=StringVar(root)
root.resizable(False,False)

#database
conn = sqlite3.connect('pcbuild.db')
c=conn.cursor()
#c.execute("CREATE TABLE components(comp_name text,comp_price integer,comp_pltfm integer,link text)")


conn.commit()
conn.close()


#Create A Frame Widget
frame1 = Frame(root, width=1280, height=720, bg=bg_colour)
frame2 = Frame(root, width=1280, height=720, bg=bg_colour)
frame3 = Frame(root, width=1280, height=720, bg=bg_colour)
frame4 = Frame(root, width=1280, height=720, bg=bg_colour)
news_frame = Frame(root, width=1280, height=720, bg=bg_colour)
login_frame = Frame(root, width=1280, height=720, bg=bg_colour)
admin_frame = Frame(root, width=1280, height=720, bg=bg_colour)
frame1.grid(row=0, column=0)
frame2.grid(row=0, column=0)
frame3.grid(row=0, column=0)
frame4.grid(row=0, column=0)
news_frame.grid(row=0, column=0)
login_frame.grid(row=0, column=0)
admin_frame.grid(row=0, column=0)
load_frame1()


#Run App
root.mainloop()

