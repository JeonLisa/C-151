from tkinter import *
root=Tk()
root.title("Sales Application")
root.geometry("800x800")
root.configure(background="lightblue")
label_month=Label(root)
label_profit=Label(root)
label_max=Label(root)
label_min=Label(root)
label_month.place(relx=0.5,rely=0.2,anchor=CENTER)
label_profit.place(relx=0.5,rely=0.3,anchor=CENTER)
label_max.place(relx=0.5,rely=0.5,anchor=CENTER)
label_min.place(relx=0.5,rely=0.7,anchor=CENTER)
month=("January","February","March","April","May","June","July","August","September","October","November","December")
label_month["text"]="Months:"+str(month)
profit=(22000,44000,77000,55000,88000,23000,100000,290000,190000,128000,458700,1100000)
label_profit["text"]="Show Profits"+str(profit)
def calMaxProfit():
    MaximumProfit=max(profit)
    MaximumProfitIndex=profit.index(MaximumProfit)
    MaximumProfitMonth=month[MaximumProfitIndex]
    label_max["text"]="maximum profit of "+str(MaximumProfit)+" In The Month Of "+str(MaximumProfitMonth)
    
def calMinProfit():
    MinimumProfit=min(profit)
    MinimumProfitIndex=profit.index(MinimumProfit)
    MinimumProfitMonth=month[MinimumProfitIndex]
    label_min["text"]="minimum profit of "+str(MinimumProfit)+" In The Month Of "+str(MinimumProfitMonth)
    
button_max_profit=Button(root,text="Maximum Profit Month",command=calMaxProfit)
button_max_profit.place(relx=0.5,rely=0.4,anchor=CENTER)
button_min_profit=Button(root,text="Minimum Profit Month",command=calMinProfit)
button_min_profit.place(relx=0.5,rely=0.6,anchor=CENTER)

root.mainloop()