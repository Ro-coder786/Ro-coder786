from tkinter import *
app=Tk()
app.title("EBC")
app.geometry("500x500")
app.configure(bg='skyblue')

def result():
    bill.delete(0,END)
    unitt=unit1.get()
    try:
        unit=float(unitt)
        if unit<=50:
            amount=unit*0.50

        elif unit>50 and unit<=150:
            amount=25+(unit-50)*0.75            #(unit-50) already calculate 50 unit.

        elif unit>150 and unit<=250:
            amount=100+(unit-150)*1.20          #(unit-150) already calculate 150 unit.

        else:
            amount=220+(unit-250)*1.50          #(unit-250) already calculate 250 unit.
        surcharge=amount*0.20
        total=surcharge+amount
        bill.insert(END, str(total))
    except:
        msg="Enter Unit Number."
        bill.insert(END, str(msg))


def reset():
    unit1.delete(0,END)
    bill.delete(0,END)

label0=Label(app,text="Electricity Bill Calculator",font=("Aachen-Bold",15),background='skyblue')
label0.pack(side=TOP,padx=10,pady=10)

frame0=Frame(app)
frame0.pack(padx=10,pady=10)
label1=Label(frame0,text="Enter Unit:",font=("Aachen-Bold",10))
label1.pack(side=LEFT,expand=True,fill='both')
# label1.config(anchor=CENTER)
unit1=Entry(frame0,bd=3)
unit1.pack(side=LEFT,expand=True,fill='both')


frame1=Frame(app)
frame1.pack(padx=10,pady=10)
label2=Label(frame1,text="Total Bill:",font=("Aachen-Bold",10))
label2.pack(side=LEFT,expand=YES,fill='both')
bill=Entry(frame1,bd=3)
bill.pack(side=LEFT,expand=YES,fill='both')

frame = Frame(app)  
frame.pack(padx=10,pady=10)

btn=Button(frame,text="Check",bd=3,activebackground = "red",command=result)
btn.pack(side=LEFT,expand=True,fill='both')

btn2=Button(frame,text="Reset",bd=3,activebackground = "red",command=reset)
btn2.pack(side=LEFT,expand=True,fill='both')




app.mainloop()